# Epistemology Patterns and Anti-Patterns

## Why These Patterns Matter to Leaders

Weak validation patterns create public risk. They allow plausible but unsupported outputs to appear authoritative, which is especially dangerous in regulated or customer-facing contexts.

## Durable Governance Patterns

- Propose-Then-Arbitrate: no downstream commitment without an axiological verdict
- Source-Cited Response Contracts: require evidence references by default
- Distinct epistemic states: Belief, Defeater, and Ignorance are not three bands of one probability
- Dual-Path Consistency Checks: compare independent reasoning/retrieval paths

## Named Implementation Patterns

### Pattern E-A: Grounded Response with Citation Chain
Every response includes: the answer, the records retrieved to support it, the confidence score, and a list of source citations with IDs and timestamps. Responses that cannot be grounded in owned sources are returned as "insufficient evidence" rather than as a best-guess.

### Pattern E-B: Proposal Beside the Record
The inference layer produces a proposal. Deterministic layers decide what is committed. The stored result keeps both: "model proposed X" in the epistemic envelope, and either a categorical triple (only on Commit) or no triple (Forbid or Refuse to Act).

### Pattern E-C: Distinct Epistemic States
A proposal is one of:

- **Belief** — claim, citations, and a confidence calibrated against Metrology bounds
- **Defeater** — a named reason the belief cannot stand
- **Ignorance** — "I don't know," with confidence left null

These states inform the deterministic domain. They do not select a workflow by crossing 90%, 70%, or any other cutoff. Human review, when required, is a praxeological precondition. Permission is an axiological verdict.

## Costly Patterns to Avoid

- Directly executing model output with no grounding checks
- RAG pipelines that cite sources but skip content verification
- Confidence scores without calibration or test evidence
- Prompt-only safety claims with no deterministic validators

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| No source citations on AI outputs | Cannot audit or defend decisions | "The model gave us a score of 87" |
| Verification depends on vendor data | Cannot independently confirm results | "We verify using [Vendor]'s cross-reference service" |
| Confidence scores without methodology | Numbers mean nothing; false confidence | Scores reported but not explained |
| No hallucination detection | Fabricated facts reach decision-makers | No testing for unsupported claims |
| Audit logs not immutable | Log tampering risk; compliance gap | Logs stored in editable format |

## What Leaders Should Watch For

- Citation laundering where references do not support conclusions
- Silent retrieval failures treated as high-confidence answers
- Drift in model behavior without updated quality thresholds

See [Business Value](../../docs/business-value.md) and [ARCHITECTURE.md](../../ARCHITECTURE.md) for why verified knowledge is essential to trustworthy AI decisions.
