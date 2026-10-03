"""Praxeology mount: package moepa.praxeology in the OPA bundle."""

from __future__ import annotations

from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult, PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot
from moepa_guard.mounts.decision_input import policy_document


class PraxeologyPolicyAgent(DeterministicPolicyAgent):
    """Ask allow_action. The rule text lives in the bundle, not in this class."""

    name = "praxeology"

    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        if not proposal.commit_eligible:
            return PolicyResult(
                agent=self.name,
                passed=True,
                rule_id="PRX-NO-OP",
                detail="No operation was proposed.",
            )
        document = policy_document(proposal, world)
        allowed = world.bundle.boolean("moepa.praxeology", "allow_action", document)
        if not allowed:
            return PolicyResult(
                agent=self.name,
                passed=False,
                rule_id="PRX-IMPOSSIBLE",
                detail=f"Action {proposal.action or '(none)'} is impossible in this state.",
            )
        return PolicyResult(
            agent=self.name,
            passed=True,
            rule_id="PRX-ADMITTED",
            detail=f"Action {proposal.action} is possible.",
        )
