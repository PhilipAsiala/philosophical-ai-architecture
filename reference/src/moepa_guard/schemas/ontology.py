"""Categorical entities, RDF triples, and Iceberg commit metadata.

Uncertainty is rejected on these types. Existence is the presence of a row.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator

# Columns of the deterministic entity table. No confidence, probability, or
# existence score. Iceberg snapshot metadata is assigned only on commit.
ENTITY_TABLE_FIELDS: tuple[str, ...] = (
    "entity_id",
    "entity_type",
    "attributes_json",
    "schema_id",
)

_LEAKED_KEYS = frozenset(
    {
        "confidence",
        "probability",
        "uncertainty",
        "existence_probability",
        "maybe",
        "score",
    }
)
_LEAKED_PREDICATES = frozenset(
    {
        "hasConfidence",
        "confidence",
        "probability",
        "existenceProbability",
    }
)


class OntologicalEntity(BaseModel):
    """A discrete individual. Attributes are categorical facts, not beliefs."""

    model_config = ConfigDict(extra="forbid")

    entity_id: str = Field(min_length=1)
    entity_type: str = Field(min_length=1)
    attributes: dict[str, str] = Field(default_factory=dict)

    @field_validator("attributes")
    @classmethod
    def _no_epistemic_leak(cls, attributes: dict[str, str]) -> dict[str, str]:
        leaked = _LEAKED_KEYS.intersection(attributes)
        if leaked:
            raise ValueError(f"entity attributes cannot store uncertainty: {sorted(leaked)}")
        return attributes


class RdfTriple(BaseModel):
    """One subject-predicate-object statement. The predicate is not a probability."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    subject: str = Field(min_length=1)
    predicate: str = Field(min_length=1)
    object: str = Field(min_length=1)

    @field_validator("predicate")
    @classmethod
    def _predicate_is_categorical(cls, predicate: str) -> str:
        if predicate in _LEAKED_PREDICATES:
            raise ValueError(f"predicate {predicate} would store uncertainty on the graph")
        return predicate


class RelationRule(BaseModel):
    """Allowed schema edge. ``object_type`` null means the object is a literal."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    subject_type: str = Field(min_length=1)
    predicate: str = Field(min_length=1)
    object_type: str | None = None


class IcebergCommitRecord(BaseModel):
    """Metadata written only after the pipeline outcome is committed.

    ``schema_id`` identifies the categorical entity schema. The record has no
    confidence column.
    """

    model_config = ConfigDict(extra="forbid")

    table: str = Field(min_length=1)
    schema_id: int = Field(ge=0)
    snapshot_id: int = Field(ge=0)
    partition: dict[str, str]
    triple: RdfTriple
    entity_id: str = Field(min_length=1)
