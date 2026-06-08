# Epistemology Patterns and Anti-Patterns

## Why These Patterns Matter to Leaders

Weak validation patterns create public risk. They allow plausible but unsupported outputs to appear authoritative, which is especially dangerous in regulated or taxpayer-facing contexts.

## Durable Governance Patterns

- Verify-Then-Act: no downstream action without validation pass
- Source-Cited Response Contracts: require evidence references by default
- Uncertainty Bands: classify confidence ranges for operational use
- Dual-Path Consistency Checks: compare independent reasoning/retrieval paths

## Costly Patterns to Avoid

- Directly executing model output with no grounding checks
- RAG pipelines that cite sources but skip content verification
- Confidence scores without calibration or test evidence
- Prompt-only safety claims with no deterministic validators

## What Leaders Should Watch For

- Citation laundering where references do not support conclusions
- Silent retrieval failures treated as high-confidence answers
- Drift in model behavior without updated quality thresholds

See [Business Value](../../docs/business-value.md) and [ARCHITECTURE.md](../../ARCHITECTURE.md) for why verified knowledge is essential to trustworthy AI decisions.
