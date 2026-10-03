"""Action-space checks: preconditions, postconditions, and resources."""

from __future__ import annotations

from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult, PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot


class PraxeologyPolicyAgent(DeterministicPolicyAgent):
    """Assert that the discrete operation is viable in the current world."""

    name = "praxeology"

    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        if not proposal.commit_eligible:
            return PolicyResult(
                agent=self.name,
                passed=True,
                rule_id="PRX-NO-OP",
                detail="No operation was proposed.",
            )
        spec = world.operations.get(proposal.action)
        if spec is None:
            return PolicyResult(
                agent=self.name,
                passed=False,
                rule_id="PRX-UNKNOWN-OPERATION",
                detail=f"Action {proposal.action} is not in the action space.",
            )
        for name, expected in spec.preconditions.items():
            if proposal.flags.get(name) is not expected:
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="PRX-PRECONDITION",
                    detail=f"Precondition {name}={expected} does not hold.",
                )
        for name, need in spec.required_resources.items():
            available = world.resources.get(name, 0)
            if available < need:
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="PRX-RESOURCE",
                    detail=f"Resource {name} has {available}, needs {need}.",
                )
        for name in spec.postconditions:
            if name not in world.satisfiable_postconditions:
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="PRX-POSTCONDITION",
                    detail=f"Postcondition {name} cannot be satisfied.",
                )
        return PolicyResult(
            agent=self.name,
            passed=True,
            rule_id="PRX-ADMITTED",
            detail=f"Action {proposal.action} is inside the action space.",
        )
