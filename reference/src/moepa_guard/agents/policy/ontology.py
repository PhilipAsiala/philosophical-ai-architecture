"""Existence checks against the graph projection of the Iceberg ledger."""

from __future__ import annotations

from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult, PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot


class OntologyPolicyAgent(DeterministicPolicyAgent):
    """A node that is not in the graph does not exist."""

    name = "ontology"

    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        if not proposal.commit_eligible:
            return PolicyResult(
                agent=self.name,
                passed=True,
                rule_id="ONT-NO-WRITE",
                detail="No categorical write was proposed.",
            )
        for entity_id in proposal.entity_ids:
            if not world.graph.exists(entity_id):
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="ONT-UNGROUNDED",
                    detail=f"Entity {entity_id} is not a node in the graph.",
                )
        for triple in proposal.triples:
            breach = world.graph.relation_breach(triple.subject, triple.predicate, triple.object)
            if breach is not None:
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="ONT-RELATION",
                    detail=breach,
                )
        return PolicyResult(
            agent=self.name,
            passed=True,
            rule_id="ONT-GROUNDED",
            detail="Referenced nodes and relations are in the graph projection.",
        )
