# MOEPA Architectural Governance and Evolution Guidelines

> **Audience:** Architects, engineers, and contributors — not executive briefings.
> Leaders evaluate proposals using business outcomes per MOEPA layer ([pitch strategy §0](pitch-strategy.md)).
> This document defines how implementations evolve; it does not replace the business-first narrative.

This repository follows the **MOEPA 5-Layer Framework** (Metrology, Ontology,
Epistemology, Praxeology, Axiology). These guidelines define non-negotiable
architectural evolution rules for all new features, integrations, and pull
requests.

## 1. Governance Over Abstraction

- Avoid vendor-locked orchestration (for example: native Bedrock-only tooling or
  LangChain glue-code that cannot be ported).
- Prioritize the Model Context Protocol (MCP) as the standardized interface for
  all data and tool access.
- Any new capability must be defined as an MCP server, ensuring logic remains
  portable and independent of the host (Bedrock, self-hosted orchestrator, or
  equivalent runtime).

## 2. From Fragments to Semantic Objects

- **No "chainsaw chunking"**: all data ingestion must use document-aware semantic
  parsing (for example: Docling, Unstructured, or equivalent approaches).
- Every data object must include provenance, structure, and semantic metadata.
- All chunks are considered **Proto-SPOs** (Sovereign Processing Objects); they
  must carry their own context to ensure semantic intent is preserved.

## 3. The MOEPA Standard for New Features

Every maintainer pull request must score its impact across the five layers:

- **Metrology**: how is this feature measured?
- **Ontology**: does this align with our canonical entity definitions?
- **Epistemology**: what proposal does this feature emit (Belief, Defeater, or
  Ignorance), and where is the citation chain?
- **Praxeology**: which action-space precondition does this feature serve?
  Confidence must not be the admission rule.
- **Axiology**: which verdict applies (Commit, Forbid, or Refuse to Act), and
  which state-changing tool is bound to Commit?

## 4. Probabilistic Proposal, Deterministic Arbiter

- Metrology and Epistemology may measure and propose. Their tools return observations or an epistemic state (Belief, Defeater, Ignorance).
- Ontology schemas stay categorical. A change that stores confidence on an entity is a NO-GO.
- Praxeology transitions are preconditions. A confidence cutoff is not an edge.
- Axiology returns only Commit, Forbid, or Refuse to Act. State-changing tools run only on Commit.
- Ignorance and unresolved defeaters produce Refuse to Act, not a low probability that is then acted on.

## 5. MCP-First Pattern

- Do not call data or RAG layers directly.
- Implement all service logic within an MCP-compliant service.
- If a legacy API is required for throughput, it must be wrapped in an MCP facade
  to ensure visibility to AI orchestrators.

## Pull Request Gate (Required)

All substantive maintainer pull requests should include a short section in the PR
description documenting:

1. The MCP server or MCP facade introduced or reused.
2. The ingestion/parsing approach and Proto-SPO metadata fields.
3. Five-layer MOEPA impact notes, including which domain proposes and which verdict authorizes any state change.
4. Citation and provenance behavior in generated outputs, with Belief, Defeater, and Ignorance kept distinct.
5. Any exceptions and approved compensating controls.

If a proposal cannot map to these requirements, it should be scored as
CONDITIONAL GO or NO-GO under the MOEPA intake rubric.

## Related Documents

- [Glossary](glossary.md) — MCP, Proto-SPO, semantic ingestion definitions
- [Data Substrate Concept](Data-Substrate-Concept.md) — semantic ingestion and Proto-SPO lifecycle
- [5-Layer Evaluation Checklist](5-Layer-Evaluation-Checklist.md) — architectural evolution gate
- [MOEPA Cognitive Architecture Spec](../ARCHITECTURE.md) — §5.2 architectural evolution principles
- [Catalog](../catalog/README.md) — capabilities, tools, and patterns aligned to these rules
- [CONTRIBUTING.md](../CONTRIBUTING.md) — PR gate requirements for contributors
