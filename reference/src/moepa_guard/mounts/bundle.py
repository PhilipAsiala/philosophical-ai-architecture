"""Sync versioned Rego out of Iceberg and mount it as one OPA bundle.

Praxeology and axiology are separate packages inside that bundle. The
reference evaluates the boolean fragment those files use. A deployment runs
the same files with `opa eval` or an OPA server. The input document is the
decision. A score is not part of it.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from moepa_guard.mounts.ledger import IcebergLedger, PolicyRuleRow

_COMPARE = re.compile(
    r"^(input(?:\.[A-Za-z_][A-Za-z0-9_]*)*)\s*(==|>=|<)\s*(.+)$"
)


@dataclass(frozen=True)
class _Cmp:
    left: str
    op: str
    right_literal: object | None
    right_path: str | None


@dataclass(frozen=True)
class _Decision:
    default: bool
    blocks: tuple[tuple[_Cmp, ...], ...]


class OpaBundle:
    """One mounted bundle. Decisions are booleans."""

    def __init__(
        self,
        revision: str,
        files: dict[str, str],
        decisions: dict[str, _Decision],
    ) -> None:
        self.revision = revision
        self.files = files
        self._decisions = decisions

    def boolean(self, package: str, name: str, document: dict[str, object]) -> bool:
        decision = self._decisions.get(f"{package}.{name}")
        if decision is None:
            raise KeyError(f"bundle has no decision {package}.{name}")
        for block in decision.blocks:
            if all(_holds(cmp, document) for cmp in block):
                return True
        return decision.default


class BundleSync:
    """Publish the latest Rego rows from the ledger into a bundle directory."""

    def publish(self, ledger: IcebergLedger, dest: Path) -> OpaBundle:
        rows = ledger.latest_rules()
        if not rows:
            raise ValueError("ledger has no policy rules to mount")
        files: dict[str, str] = {}
        decisions: dict[str, _Decision] = {}
        revision = max(row.revision for row in rows)
        for row in rows:
            relative = _bundle_path(row.namespace)
            files[relative] = row.rego
            target = dest / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(row.rego, encoding="utf-8")
            parsed = _parse(row.namespace, row.rego)
            decisions.update(parsed)
        manifest = {"revision": revision, "roots": sorted({_root(row.namespace) for row in rows})}
        (dest / ".manifest").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        return OpaBundle(revision=revision, files=files, decisions=decisions)


def seed_rules() -> list[PolicyRuleRow]:
    """Load the authored Rego into ledger rows. The files are the seed, not the mount."""

    rego_dir = Path(__file__).resolve().parent / "rego"
    rows: list[PolicyRuleRow] = []
    for namespace, filename in (
        ("moepa.praxeology", "praxeology.rego"),
        ("moepa.axiology", "axiology.rego"),
    ):
        rows.append(
            PolicyRuleRow(
                namespace=namespace,
                version=1,
                revision="2026-10-02",
                rego=(rego_dir / filename).read_text(encoding="utf-8"),
            )
        )
    return rows


def _bundle_path(namespace: str) -> str:
    return "/".join(namespace.split(".")) + "/policy.rego"


def _root(namespace: str) -> str:
    parts = namespace.split(".")
    return "/".join(parts[:-1]) if len(parts) > 1 else namespace


def _parse(namespace: str, rego: str) -> dict[str, _Decision]:
    defaults: dict[str, bool] = {}
    blocks: dict[str, list[tuple[_Cmp, ...]]] = {}
    current: str | None = None
    current_cmps: list[_Cmp] = []

    def _close() -> None:
        nonlocal current, current_cmps
        if current is None:
            return
        blocks.setdefault(current, []).append(tuple(current_cmps))
        current = None
        current_cmps = []

    for raw in rego.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or line.startswith("package ") or line.startswith("import "):
            continue
        if line == "}":
            _close()
            continue
        default = re.match(r"default\s+([A-Za-z_][A-Za-z0-9_]*)\s*:=\s*(true|false)$", line)
        if default:
            defaults[default.group(1)] = default.group(2) == "true"
            continue
        head = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s+if\s+\{$", line)
        if head:
            _close()
            current = head.group(1)
            current_cmps = []
            continue
        if current is None:
            raise ValueError(f"unrecognized Rego line: {line}")
        current_cmps.append(_cmp(line))
    _close()
    parsed: dict[str, _Decision] = {}
    for name, rule_blocks in blocks.items():
        parsed[f"{namespace}.{name}"] = _Decision(
            default=defaults.get(name, False),
            blocks=tuple(rule_blocks),
        )
    return parsed


def _cmp(line: str) -> _Cmp:
    matched = _COMPARE.match(line)
    if matched is None:
        raise ValueError(f"unsupported comparison: {line}")
    left, op, raw_right = matched.group(1), matched.group(2), matched.group(3).strip()
    if raw_right.startswith("input.") or raw_right == "input":
        return _Cmp(left=left, op=op, right_literal=None, right_path=raw_right)
    return _Cmp(left=left, op=op, right_literal=_literal(raw_right), right_path=None)


def _literal(token: str) -> object:
    if token in {"true", "false"}:
        return token == "true"
    if token.startswith('"') and token.endswith('"'):
        return token[1:-1]
    if re.match(r"^-?\d+$", token):
        return int(token)
    raise ValueError(f"unsupported literal: {token}")


def _holds(cmp: _Cmp, document: dict[str, object]) -> bool:
    left = _lookup(document, cmp.left)
    right = _lookup(document, cmp.right_path) if cmp.right_path else cmp.right_literal
    if left is None or right is None:
        return False
    if cmp.op == "==":
        return left == right
    if isinstance(left, bool) or isinstance(right, bool):
        return False
    if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
        return False
    if cmp.op == ">=":
        return left >= right
    if cmp.op == "<":
        return left < right
    return False


def _lookup(document: dict[str, object], path: str) -> object | None:
    if not path.startswith("input"):
        return None
    current: object = document
    parts = path.split(".")[1:]
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current
