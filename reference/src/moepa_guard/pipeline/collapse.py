"""Turn a continuous proposal into one discrete, uncommitted action.

The engine does not sample. A tie for the mode yields no commit-eligible
action. Confidence is copied onto the audit record and is not a branch.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from moepa_guard.agents.policy.base import PolicyView
from moepa_guard.schemas.epistemic import EpistemicState
from moepa_guard.schemas.ontology import RdfTriple
from moepa_guard.schemas.proposal import UncommittedCandidate


class CollapsedProposal(BaseModel):
    """Discrete action plus an audit copy of the score the agents must not read."""

    model_config = ConfigDict(extra="forbid")

    proposal_id: str
    commit_eligible: bool
    action: str
    epistemic_state: Literal["belief", "defeater", "ignorance"]
    entity_ids: tuple[str, ...]
    triples: tuple[RdfTriple, ...]
    flags: dict[str, bool]
    collapse_rule: str = Field(min_length=1)
    confidence: float | None = None

    def to_policy_view(self) -> PolicyView:
        """Drop the score before any policy agent runs."""

        return PolicyView(
            proposal_id=self.proposal_id,
            commit_eligible=self.commit_eligible,
            action=self.action,
            epistemic_state=self.epistemic_state,
            entity_ids=self.entity_ids,
            triples=self.triples,
            flags=self.flags,
        )


class StateCollapseEngine:
    """Deterministic map from an uncommitted candidate to one discrete action."""

    def collapse(self, candidate: UncommittedCandidate) -> CollapsedProposal:
        state = candidate.claim.state
        shared = {
            "proposal_id": candidate.proposal_id,
            "entity_ids": tuple(candidate.entity_ids),
            "triples": tuple(candidate.triples),
            "flags": dict(candidate.flags),
            "confidence": candidate.claim.confidence,
            "epistemic_state": state.value,
        }
        if state is not EpistemicState.BELIEF or candidate.claim.defeaters:
            return CollapsedProposal(
                commit_eligible=False,
                action="",
                collapse_rule="AX-INPUT-NOT-BELIEF",
                **shared,
            )
        distribution = candidate.claim.distribution
        if distribution is None:
            return CollapsedProposal(
                commit_eligible=True,
                action=candidate.proposed_action,
                collapse_rule="STATED-ACTION",
                **shared,
            )
        mode = _unique_mode(distribution)
        if mode is None:
            return CollapsedProposal(
                commit_eligible=False,
                action="",
                collapse_rule="NON-UNIQUE-MODE",
                **shared,
            )
        return CollapsedProposal(
            commit_eligible=True,
            action=mode,
            collapse_rule="UNIQUE-MODE",
            **shared,
        )


def _unique_mode(distribution: dict[str, float]) -> str | None:
    top = max(distribution.values())
    winners = [label for label, weight in distribution.items() if weight == top]
    if len(winners) != 1:
        return None
    return winners[0]
