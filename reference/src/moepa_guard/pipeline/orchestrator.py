"""Sequential guardrail: ontology, then praxeology, then axiology."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict

from moepa_guard.agents.policy.axiology import AxiologyPolicyAgent
from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult
from moepa_guard.agents.policy.ontology import OntologyPolicyAgent
from moepa_guard.agents.policy.praxeology import PraxeologyPolicyAgent
from moepa_guard.agents.policy.world import WorldSnapshot
from moepa_guard.pipeline.collapse import CollapsedProposal, StateCollapseEngine
from moepa_guard.schemas.ontology import IcebergCommitRecord, RdfTriple
from moepa_guard.schemas.proposal import UncommittedCandidate

Outcome = Literal["committed", "blocked"]
Verdict = Literal["commit", "forbid", "refuse_to_act"]


class PipelineResult(BaseModel):
    """External outcome is binary. The audit still names the axiological verdict."""

    model_config = ConfigDict(extra="forbid")

    outcome: Outcome
    axiological_verdict: Verdict | None
    stages: list[PolicyResult]
    collapsed_action: str
    collapse_rule: str
    epistemic_confidence: float | None
    commit: IcebergCommitRecord | None = None
    blocking_rule_id: str | None = None


class GuardrailPipeline:
    """Run collapse, then the three deterministic agents, in order.

    The pipeline does not construct or call a language model. ``candidate`` is
    already an uncommitted payload.
    """

    def __init__(
        self,
        world: WorldSnapshot,
        *,
        collapse: StateCollapseEngine | None = None,
        agents: tuple[DeterministicPolicyAgent, ...] | None = None,
    ) -> None:
        self._world = world
        self._collapse = collapse or StateCollapseEngine()
        self._agents = agents or (
            OntologyPolicyAgent(),
            PraxeologyPolicyAgent(),
            AxiologyPolicyAgent(),
        )

    def run(self, candidate: UncommittedCandidate) -> PipelineResult:
        collapsed = self._collapse.collapse(candidate)
        view = collapsed.to_policy_view()
        stages: list[PolicyResult] = []
        for agent in self._agents:
            result = agent.evaluate(view, self._world)
            stages.append(result)
            if not result.passed:
                return PipelineResult(
                    outcome="blocked",
                    axiological_verdict=_verdict_for(result),
                    stages=stages,
                    collapsed_action=collapsed.action,
                    collapse_rule=collapsed.collapse_rule,
                    epistemic_confidence=collapsed.confidence,
                    commit=None,
                    blocking_rule_id=result.rule_id,
                )
        record = _commit_record(collapsed, self._world)
        self._world.ledger.commits.append(record)
        return PipelineResult(
            outcome="committed",
            axiological_verdict="commit",
            stages=stages,
            collapsed_action=collapsed.action,
            collapse_rule=collapsed.collapse_rule,
            epistemic_confidence=collapsed.confidence,
            commit=record,
            blocking_rule_id=None,
        )


def _verdict_for(result: PolicyResult) -> Verdict | None:
    if result.rule_id == "AX-FORBID":
        return "forbid"
    if result.rule_id == "AX-REFUSE":
        return "refuse_to_act"
    return None


def _commit_record(collapsed: CollapsedProposal, world: WorldSnapshot) -> IcebergCommitRecord:
    entity_id = collapsed.entity_ids[0] if collapsed.entity_ids else collapsed.proposal_id
    if collapsed.triples:
        triple = collapsed.triples[0]
    else:
        triple = RdfTriple(subject=entity_id, predicate="performs", object=collapsed.action)
    return IcebergCommitRecord(
        table=world.table,
        schema_id=world.schema_id,
        snapshot_id=_snapshot_id(collapsed.proposal_id, collapsed.action),
        partition={"action": collapsed.action},
        triple=triple,
        entity_id=entity_id,
    )


def _snapshot_id(proposal_id: str, action: str) -> int:
    """Stable positive integer derived from the committed symbols. Not random."""

    total = 0
    for character in f"{proposal_id}:{action}":
        total = (total * 33 + ord(character)) % 2_000_000_000
    return total
