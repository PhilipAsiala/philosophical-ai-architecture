"""Discrete world the policy agents read. No scores and no model client."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from moepa_guard.mounts.bundle import OpaBundle
from moepa_guard.mounts.graph import GraphProjection
from moepa_guard.mounts.ledger import IcebergLedger


class WorldSnapshot(BaseModel):
    """Ledger plus the two deterministic mounts: graph and OPA bundle."""

    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    ledger: IcebergLedger
    graph: GraphProjection
    bundle: OpaBundle
    resources: dict[str, int]
    satisfiable_postconditions: frozenset[str] = frozenset()
    schema_id: int = Field(default=1, ge=0)
    table: str = "ontological_entity"
