# Epistemology Examples

## Why These Examples Matter

These are examples of evidence and validation artifacts leaders should expect when AI conclusions are used for consequential decisions.

## SPO Triple + Epistemic Metadata Envelope

This example demonstrates the substrate pattern for the Epistemology layer: the base triple lives once on the shared SPO backbone, and the epistemic metadata envelope attaches justification, confidence, and provenance information without duplicating the underlying fact.

**Income verification — high-confidence fact**

```json
{
  "triple": {"s": "IncomeVerification:TX12345", "p": "hasAmount", "o": 85000},
  "epistemic_metadata": {
    "confidence": 0.98,
    "justification": "ThirdPartyStudy_2025_n=125000",
    "evidence_links": ["graph-node-study-result"],
    "status": "HighReliability",
    "last_revised": "2026-06-09"
  }
}
```

The base triple `(IncomeVerification:TX12345, hasAmount, 85000)` is stored once in the shared SPO/quad backbone. The `epistemic_metadata` envelope is the Epistemology layer's contribution: it records *how we know* — confidence score, supporting study, evidence graph links, reliability status, and revision timestamp — without altering the base fact. Belief networks, W3C PROV-O provenance lineage, and revision history can be attached as linked sub-graphs in the same substrate.

## Example Governance Artifacts

- rag/index-manifest.yaml
- validation/rules/critical-claims.yaml
- evaluation/benchmark-suite.json
- audit/evidence-bundles/example-case-001.json

## Example Configuration Ideas

- Minimum citation quality thresholds
- Confidence calibration policy by use-case risk
- Escalation logic for low-confidence outcomes
