# Praxeology Examples

## Why These Examples Matter

These are examples of workflow control artifacts that help leadership verify where approvals, boundaries, and recovery mechanisms actually exist.

## SPO Triple + Praxeological Metadata Envelope

This example demonstrates the substrate pattern for the Praxeology layer: the base triple lives once on the shared SPO backbone, and the praxeological metadata envelope attaches goal context, conditions, expected outcomes, and action sequences without duplicating the underlying fact.

**Process policy application — auto-approval trigger**

```json
{
  "triple": {"s": "RefundProcess:TX12345", "p": "appliesPolicy", "o": "AutoApproveHighConfidence"},
  "praxeological_metadata": {
    "goal": "EfficientCompliantProcessing",
    "conditions": ["epistemic_confidence >= 0.98"],
    "expected_outcome": {"utility": 0.95, "historical_success": 0.97},
    "action_sequence": ["verify", "approve", "notify"]
  }
}
```

The base triple `(RefundProcess:TX12345, appliesPolicy, AutoApproveHighConfidence)` is stored once in the shared SPO/quad backbone. The `praxeological_metadata` envelope is the Praxeology layer's contribution: it records *what the system should do* — the governing goal, triggering conditions (which reference the epistemic confidence established by the Epistemology layer), expected utility, and the ordered action sequence. Historical action logs, MDP/policy artifacts, and outcome telemetry are stored as time-series versioned triples or linked policy graphs in the same substrate.

## Example Governance Artifacts

- workflows/intake-to-approval.state.json
- rules/escalation/high-risk.yaml
- orchestration/tool-allowlist.yaml
- runbooks/failure-recovery.md

## Example Configuration Ideas

- SLA targets for approval turnaround
- Escalation thresholds by risk class
- Required telemetry fields per workflow transition
