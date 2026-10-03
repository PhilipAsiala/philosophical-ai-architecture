"""Final binary gate. The view carries no score."""

from __future__ import annotations

from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult, PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot


class AxiologyPolicyAgent(DeterministicPolicyAgent):
    """Commit, or block. The decision reads rules, not a numeric weight."""

    name = "axiology"

    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        if not proposal.commit_eligible or proposal.epistemic_state != "belief":
            return PolicyResult(
                agent=self.name,
                passed=False,
                rule_id="AX-REFUSE",
                detail="Refuse to act: the proposal is not a belief eligible to commit.",
            )
        if proposal.action in world.forbidden_actions:
            return PolicyResult(
                agent=self.name,
                passed=False,
                rule_id="AX-FORBID",
                detail=f"Forbid {proposal.action}: it violates a safety or compliance rule.",
            )
        return PolicyResult(
            agent=self.name,
            passed=True,
            rule_id="AX-COMMIT",
            detail=f"Commit {proposal.action}.",
        )
