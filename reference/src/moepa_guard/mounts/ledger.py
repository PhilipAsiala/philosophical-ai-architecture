"""Apache Iceberg stands in as the immutable ledger for every MOEPA layer.

This reference keeps the tables in memory. A deployment writes the same rows
as Iceberg snapshots. Specialized engines mount those tables; they are not a
second source of truth.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from moepa_guard.schemas.ontology import (
    IcebergCommitRecord,
    OntologicalEntity,
    RdfTriple,
    RelationRule,
)


class PolicyRuleRow(BaseModel):
    """One versioned Rego document stored in the ledger."""

    model_config = ConfigDict(extra="forbid")

    namespace: str = Field(min_length=1)
    version: int = Field(ge=1)
    revision: str = Field(min_length=1)
    rego: str = Field(min_length=1)


class IcebergLedger(BaseModel):
    """Source-of-truth tables. Policy agents do not write these except on commit."""

    model_config = ConfigDict(extra="forbid")

    entities: list[OntologicalEntity] = Field(default_factory=list)
    triples: list[RdfTriple] = Field(default_factory=list)
    relation_rules: list[RelationRule] = Field(default_factory=list)
    policy_rules: list[PolicyRuleRow] = Field(default_factory=list)
    commits: list[IcebergCommitRecord] = Field(default_factory=list)

    def latest_rules(self) -> list[PolicyRuleRow]:
        """Highest version of each namespace."""

        chosen: dict[str, PolicyRuleRow] = {}
        for row in self.policy_rules:
            current = chosen.get(row.namespace)
            if current is None or row.version > current.version:
                chosen[row.namespace] = row
        return list(chosen.values())
