# Praxeology Examples

## Why These Examples Matter

These are examples of workflow control artifacts that help leadership verify where approvals, boundaries, and recovery mechanisms actually exist.

## SPO Triple + Praxeological Metadata Envelope

This example demonstrates the substrate pattern for the Praxeology layer: the base triple lives once on the shared SPO backbone, and the praxeological metadata envelope attaches goal context, conditions, expected outcomes, and action sequences without duplicating the underlying fact.

**Process policy application — admitted transition**

```json
{
  "triple": {"s": "RefundProcess:TX12345", "p": "appliesPolicy", "o": "RoutineRefund"},
  "praxeological_metadata": {
    "from_state": "verified",
    "verb": "approve",
    "admitted": true,
    "conditions": [
      "epistemic_state == belief",
      "required_evidence_present",
      "human_checkpoint_required == false"
    ],
    "action_sequence": ["verify", "await_commit", "notify"]
  }
}
```

The base triple is written only after Axiology returns Commit. The praxeological envelope records whether the transition was in the action space. Conditions are discrete. A confidence comparison is not a condition. Notification runs only on Commit.

## Example Governance Artifacts

- workflows/intake-to-approval.state.json
- rules/escalation/high-risk.yaml
- orchestration/tool-allowlist.yaml
- runbooks/failure-recovery.md

## Example Configuration Ideas

- SLA targets for approval turnaround
- Escalation thresholds by risk class
- Required telemetry fields per workflow transition
