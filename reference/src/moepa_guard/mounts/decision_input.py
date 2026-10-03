"""Document passed to the OPA bundle. Scores are not fields on this document."""

from __future__ import annotations

from moepa_guard.agents.policy.base import PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot


def policy_document(proposal: PolicyView, world: WorldSnapshot) -> dict[str, object]:
    """Build the boolean input both Rego packages read."""

    return {
        "action": proposal.action,
        "commit_eligible": proposal.commit_eligible,
        "epistemic_state": proposal.epistemic_state,
        "flags": dict(proposal.flags),
        "resources": dict(world.resources),
        "satisfiable": {name: True for name in sorted(world.satisfiable_postconditions)},
    }
