# Epistemology Tools

## Executive Summary

These tool categories matter because they determine whether validation, explanation, and evidence remain under institutional control. Leaders should favor approaches that preserve inspectability and defensible reasoning over black-box convenience.

## Recommended Self-Hosted and Open Options

| Capability | Tools | Leadership Decision Lens |
| --- | --- | --- |
| Retrieval infrastructure | OpenSearch, Elasticsearch, PGVector, Qdrant, Chroma | Keep indexes and source mappings inside controlled infrastructure so evidence remains exportable. |
| RAG orchestration | LangChain, LlamaIndex, Haystack | Retrieval rules and grounding policies should be inspectable and versioned. |
| Validation and guardrails | Guardrails AI, NeMo Guardrails, custom policy engines | Choose options that allow leadership and auditors to inspect how conclusions are checked. |
| Experiment and model evaluation | MLflow, Evidently, WhyLabs (self-managed where possible) | Reliability data should remain under enterprise control, not only in vendor dashboards. |
| Explainability and consistency | Captum, SHAP, custom consistency tests | Rationale artifacts should support audit, appeal, and oversight needs. |

## Leadership Guidance

- Separate model output generation from verification decisions.
- Keep source-of-truth indexes and citation metadata exportable.
- Require signed evidence bundles for high-risk decisions.
- Cross-check validation choices against [Business Value](../../docs/business-value.md) and the [Owned-Brain Strategy](../../ARCHITECTURE.md).
