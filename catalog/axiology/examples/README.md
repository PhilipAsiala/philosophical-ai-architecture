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
    "weight": 0.85,
    "utility_function": "max(Compliance, CustomerSatisfaction) subject to Rights",
    "ethical_rules": ["NEVER_auto_deny_without_human_review_if_confidence<0.9"],
    "priority": ["CustomerBillOfRights > Efficiency"]
  }
}
```

The base triple `(CustomerRights, constrains, RefundProcess)` is stored once in the shared SPO/quad backbone. The `axiological_metadata` envelope is the Axiology layer's contribution: it records *what values govern the action* — the value classification (intrinsic vs. instrumental), relative weight, utility function, non-negotiable ethical rules, and lexicographic priority ordering. Value hierarchies, PREFERS / CONSTRAINS edge weights, and normative constraint sets are stored as linked sub-graphs in the same substrate.

## Example Governance Artifacts

- policy/golden-master/ai-governance.rego
- fairness/thresholds/customer-outcomes.yaml
- privacy/control-matrix.csv
- compliance/evidence/quarterly-review-2026q2.md

## Example Configuration Ideas

- Policy exception workflow and approval model
- Fairness alerting thresholds and response runbooks
- Control-to-regulation mapping for audit readiness
