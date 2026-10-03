"""Discrete world the policy agents read. No scores and no model client."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from moepa_guard.schemas.ontology import OntologicalEntity, RdfTriple, RelationRule


class OperationSpec(BaseModel):
    """One allowable operation: preconditions, resources, and postconditions."""

    model_config = ConfigDict(extra="forbid")

    action: str = Field(min_length=1)
    preconditions: dict[str, bool] = Field(default_factory=dict)
    required_resources: dict[str, int] = Field(default_factory=dict)
    postconditions: tuple[str, ...] = ()


class WorldSnapshot(BaseModel):
    """Committed categorical state plus the rule catalogs."""

    model_config = ConfigDict(extra="forbid")

    entities: dict[str, OntologicalEntity]
    triples: tuple[RdfTriple, ...] = ()
    relation_rules: tuple[RelationRule, ...] = ()
    operations: dict[str, OperationSpec]
    resources: dict[str, int]
    satisfiable_postconditions: frozenset[str] = frozenset()
    forbidden_actions: frozenset[str] = frozenset()
    schema_id: int = Field(default=1, ge=0)
    table: str = "ontological_entity"
