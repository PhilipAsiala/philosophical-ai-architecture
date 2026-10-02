# Axiology Examples

## Why These Examples Matter

These are examples of policy, fairness, privacy, and compliance artifacts leaders should expect when approving regulated AI initiatives.

## SPO Triple + Axiological Metadata Envelope

This example demonstrates the substrate pattern for the Axiology layer: the base triple lives once on the shared SPO backbone, and the axiological metadata envelope attaches value classifications, utility functions, ethical rules, and priority orderings without duplicating the underlying fact.

**Rights constraint — value-governed process boundary**

```json
{
  "triple": {"s": "CustomerRights", "p": "constrains", "o": "RefundProcess"},
  "axiological_metadata": {
    "value_type": "Intrinsic (Fairness, DueProcess)",
    "ethical_rules": [
      "verdict_set: commit | forbid | refuse_to_act",
      "refuse_to_act_on_ignorance",
      "refuse_to_act_on_unresolved_defeater",
      "forbid_denial_unless_human_checkpoint_admitted"
    ],
    "priority": ["CustomerBillOfRights > Efficiency"]
  }
}
```

The base triple `(CustomerRights, constrains, RefundProcess)` is stored once in the shared SPO/quad backbone. The `axiological_metadata` envelope records the deontic rules that produce a verdict. Runtime authorization is Commit, Forbid, or Refuse to Act. A preference ordering may explain why a rule exists; it is not itself a permission.

## Example Governance Artifacts

- policy/golden-master/ai-governance.rego
- fairness/thresholds/customer-outcomes.yaml
- privacy/control-matrix.csv
- compliance/evidence/quarterly-review-2026q2.md

## Example Configuration Ideas

- Policy exception workflow and approval model
- Fairness alerting thresholds and response runbooks
- Control-to-regulation mapping for audit readiness
