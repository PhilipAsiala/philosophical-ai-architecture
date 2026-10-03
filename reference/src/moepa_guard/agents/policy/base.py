"""Shared contract for deterministic policy agents."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from moepa_guard.agents.policy.world import WorldSnapshot
from moepa_guard.schemas.ontology import RdfTriple


class PolicyView(BaseModel):
    """Discrete inputs a policy agent may read.

    Confidence, uncertainty, and distributions are absent on purpose.
    ``epistemic_state`` is a label (belief, defeater, ignorance), not a score.
    """

    model_config = ConfigDict(extra="forbid")

    proposal_id: str = Field(min_length=1)
    commit_eligible: bool
    action: str
    epistemic_state: Literal["belief", "defeater", "ignorance"]
    entity_ids: tuple[str, ...]
    triples: tuple[RdfTriple, ...]
    flags: dict[str, bool]


class PolicyResult(BaseModel):
    """One agent's pass or fail. There is no partial credit."""

    model_config = ConfigDict(extra="forbid")

    agent: str = Field(min_length=1)
    passed: bool
    rule_id: str = Field(min_length=1)
    detail: str = Field(min_length=1)


class DeterministicPolicyAgent(ABC):
    """Rule, schema, or policy-as-code check. Subclasses must not sample."""

    name: str

    @abstractmethod
    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        """Return a pass or fail determined only by ``proposal`` and ``world``."""
