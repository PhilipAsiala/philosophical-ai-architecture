"""Uncommitted output of a proposer. Any LLM adapter stops at this type."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from moepa_guard.schemas.epistemic import EpistemicClaim, MetrologyTelemetry
from moepa_guard.schemas.ontology import RdfTriple


class UncommittedCandidate(BaseModel):
    """A proposed action and response that has not been committed.

    Adapters for a specific model provider construct this object and then
    return. The guardrail pipeline never calls the provider.
    """

    model_config = ConfigDict(extra="forbid")

    proposal_id: str = Field(min_length=1)
    query: str = Field(min_length=1)
    proposed_action: str = Field(min_length=1)
    proposed_response: str = Field(min_length=1)
    claim: EpistemicClaim
    metrology: MetrologyTelemetry
    entity_ids: list[str] = Field(default_factory=list)
    triples: list[RdfTriple] = Field(default_factory=list)
    flags: dict[str, bool] = Field(default_factory=dict)
