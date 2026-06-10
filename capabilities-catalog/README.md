# Capabilities Catalog

A reference catalog of AI capabilities, tools, and patterns organized by MOEPA layer. This catalog is designed for technical architects, program managers, and governance reviewers evaluating AI proposals or designing owned AI systems.

---

## Purpose

This catalog answers the question: **"For each MOEPA layer, what capabilities should a well-governed AI system have — and what open-source or self-hosted tools can provide them?"**

It is a reference resource, not a prescriptive implementation guide. Tool recommendations prioritize:
- **Sovereignty:** tools you can run on your own infrastructure
- **Openness:** open-source or open-standard tools you are not locked into
- **Auditability:** tools that produce verifiable, inspectable outputs

---

## How to Use This Catalog

1. **Identify the layer(s)** relevant to your evaluation or design task
2. **Review the capabilities** to understand what a mature implementation includes
3. **Assess tool options** against your agency's hosting and compliance requirements
4. **Use patterns** to understand proven architectural approaches
5. **Review cross-layer compositions** for multi-layer use cases

---

## Catalog Files

| Layer | File | Core Focus |
|---|---|---|
| Layer 1 — Metrology | [metrology.md](metrology.md) | Data quality, measurement, provenance, observability |
| Layer 2 — Ontology | [ontology.md](ontology.md) | Knowledge graphs, entity models, semantic structure |
| Layer 3 — Epistemology | [epistemology.md](epistemology.md) | Verification, RAG, fact-checking, audit trails |
| Layer 4 — Praxeology | [praxeology.md](praxeology.md) | Workflow orchestration, state machines, human oversight |
| Layer 5 — Axiology | [axiology.md](axiology.md) | Policy enforcement, guardrails, compliance, values |
| Cross-Layer | [cross-layer-compositions.md](cross-layer-compositions.md) | Multi-layer patterns and capability combinations |

---

## Governance Notes

- Prefer **self-hosted** options for any capability that touches PII, regulatory data, or high-stakes decisions
- Treat cloud-hosted SaaS tools as **transitional** — acceptable short-term with an explicit migration path
- Require **open data formats** at every layer so capabilities remain portable
- Document **which tools are in use** at each layer as part of your MOEPA governance record

---

## Related Resources

- [MOEPA 5-Layer Framework](../docs/MOEPA-5-Layer-Framework.md) — per-layer leadership questions
- [5-Layer Evaluation Checklist](../docs/5-Layer-Evaluation-Checklist.md) — scoring rubric for proposals
- [Full Governance Catalog](../catalog/README.md) — detailed scoring and governance by layer
- [Architecture Specification](../ARCHITECTURE.md) — complete technical specification
