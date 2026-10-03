"""Collapse is a pure function, and policy modules do not sample."""

from pathlib import Path

from moepa_guard.pipeline.collapse import StateCollapseEngine
from moepa_guard.schemas.epistemic import EpistemicState
from support import candidate

_POLICY_DIR = Path(__file__).resolve().parents[1] / "src" / "moepa_guard" / "agents" / "policy"
_BANNED = ("random", "sample", "confidence", "probability")


def test_unique_mode_replaces_the_stated_action() -> None:
    engine = StateCollapseEngine()
    collapsed = engine.collapse(
        candidate(
            action="record_income",
            distribution={"export_pii": 0.2, "record_income": 0.8},
        )
    )

    assert collapsed.commit_eligible is True
    assert collapsed.action == "record_income"
    assert collapsed.collapse_rule == "UNIQUE-MODE"
    assert "confidence" not in collapsed.to_policy_view().model_dump()


def test_tied_distribution_is_not_a_commit() -> None:
    engine = StateCollapseEngine()
    collapsed = engine.collapse(
        candidate(
            distribution={"record_income": 0.5, "export_pii": 0.5},
        )
    )

    assert collapsed.commit_eligible is False
    assert collapsed.action == ""
    assert collapsed.collapse_rule == "NON-UNIQUE-MODE"


def test_collapse_ignores_the_confidence_value() -> None:
    engine = StateCollapseEngine()
    low = engine.collapse(candidate(proposal_id="same", confidence=0.01))
    high = engine.collapse(candidate(proposal_id="same", confidence=0.99))

    assert low.action == high.action
    assert low.commit_eligible is high.commit_eligible is True
    assert low.confidence != high.confidence


def test_defeater_does_not_collapse_to_an_action() -> None:
    engine = StateCollapseEngine()
    collapsed = engine.collapse(
        candidate(
            state=EpistemicState.DEFEATER,
            confidence=0.4,
            defeaters=["wage record conflicts with attestation"],
        )
    )

    assert collapsed.commit_eligible is False
    assert collapsed.epistemic_state == "defeater"


def test_policy_agents_do_not_mention_scores_or_sampling() -> None:
    for name in ("ontology.py", "praxeology.py", "axiology.py"):
        source = (_POLICY_DIR / name).read_text(encoding="utf-8").lower()
        for token in _BANNED:
            assert token not in source, f"{name} contains {token}"
