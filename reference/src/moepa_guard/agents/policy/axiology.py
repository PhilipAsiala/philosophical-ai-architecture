"""Axiology mount: package moepa.axiology in the same OPA bundle."""

from __future__ import annotations

from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult, PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot
from moepa_guard.mounts.decision_input import policy_document


class AxiologyPolicyAgent(DeterministicPolicyAgent):
    """Ask deny_action. A possible act can still be denied."""

    name = "axiology"

    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        document = policy_document(proposal, world)
        denied = world.bundle.boolean("moepa.axiology", "deny_action", document)
        if denied and not proposal.commit_eligible:
            return PolicyResult(
                agent=self.name,
                passed=False,
                rule_id="AX-REFUSE",
                detail="Refuse to act: the proposal is not eligible to commit.",
            )
        if denied:
            return PolicyResult(
                agent=self.name,
                passed=False,
                rule_id="AX-FORBID",
                detail=f"Forbid {proposal.action}: denied by the axiology package.",
            )
        return PolicyResult(
            agent=self.name,
            passed=True,
            rule_id="AX-COMMIT",
            detail=f"Commit {proposal.action}.",
        )
