# High-confidence boundary block

A proposer can be almost sure and still be wrong about what the institution may do. This walkthrough matches the reference test `test_axiology_blocks_high_confidence_boundary_violation`.

The mind is probabilistic in handling evidence, and non-probabilistic in its commitments.

## The candidate

An inference adapter — not the guardrail — emits an uncommitted candidate:

| Field | Value |
|---|---|
| Proposed action | `export_pii` |
| Entity | `Applicant:TX12345` (present in the owned registry) |
| Epistemic state | Belief |
| Confidence | 0.99 |
| Evidence | A wage record the adapter cites |

The entity is real. The relation `enrolledIn` is allowed. The operation `export_pii` is in the action space, its preconditions hold, and a review slot is available. Nothing in Ontology or Praxeology fails.

## The arbiter

`AxiologyPolicyAgent` evaluates a discrete view that has no confidence field. `export_pii` is on the forbidden-action list. The agent returns rule `AX-FORBID`.

The pipeline outcome is **blocked**. No Iceberg commit record is written. The audit still stores `epistemic_confidence: 0.99` so a reviewer can see that the block was not caused by a low score.

The same action at confidence 0.01 is also blocked, with the same rule. The score never enters the decision.

## What a different failure looks like

If the candidate names `Applicant:DOES-NOT-EXIST`, `OntologyPolicyAgent` stops the pipeline at `ONT-UNGROUNDED` before Axiology runs. That is a hallucination of an entity, not a boundary violation. Both outcomes are blocks. Only the boundary case is an axiological forbid.

## Where the code lives

[reference/](../reference/) — `GuardrailPipeline` accepts an `UncommittedCandidate` and does not call a model provider.
