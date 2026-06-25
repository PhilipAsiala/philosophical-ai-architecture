# FAQ

## Is SPO/quad storage required on day one?

No — but it is **imperative at end state**. The repository requires every agency-owned Data Substrate to **evolve toward** owned SPO/quad representation with layer metadata envelopes on a federated hypergraph + lakehouse. Agencies may start with open-format lakehouse storage (Iceberg/Parquet) using SPO-compatible schemas, then add a pilot triple store, then enterprise graph and federation. Interim storage is acceptable when the data is agency-owned, provenance-complete, open-format, and backed by a documented migration path to end state. See [End State vs. Evolution Path](Data-Substrate-Concept.md#end-state-vs-evolution-path).

## Is the Data Substrate a sixth layer?

No. The Data Substrate is the agency-owned knowledge library beneath all five layers — an SPO/quad triple store plus lakehouse — that every layer stores into. It holds truth, values, rules, and lineage in open formats the organization owns permanently. It is **not** a scored layer. See §5.1 of [ARCHITECTURE.md](../ARCHITECTURE.md) for the full substrate specification.

## Is this a finished architecture?

No. This repository describes a draft **Philosophical AI Architecture** for discussion, refinement, and review. The **MOEPA 5-Layer Framework** (engineering blueprint and intake scoring) and **MOEPA Cognitive Architecture** (technical specification in [ARCHITECTURE.md](../ARCHITECTURE.md)) are components within that ecosystem — all are proposals, not deployed systems.

## What is the difference between Philosophical AI Architecture, MOEPA 5-Layer Framework, and MOEPA Cognitive Architecture?

- **Philosophical AI Architecture** — the full ecosystem: Data Substrate, MOEPA Catalog, guardrails, own-vs-rent strategy, cognitive control plane.
- **MOEPA 5-Layer Framework** — the engineering blueprint and governance engine inside the architecture: five layers, intake scoring, GO / CONDITIONAL GO / NO-GO decisions.
- **MOEPA Cognitive Architecture** — the technical stack design in [ARCHITECTURE.md](../ARCHITECTURE.md): storage mapping, catalog integration, recommended tools.

See the [Naming section in the README](../README.md#naming), [Pitch Strategy](pitch-strategy.md), and [Glossary](glossary.md).

## What are Cognition, Affect, and Conation?

The three human cognitive functions the Philosophical AI Architecture maps into software:

- **Cognition** (knowing) → Metrology, Ontology, Epistemology
- **Affect** (valuing) → Axiology
- **Conation** (acting) → Praxeology

Philosophy (Metrology, Ontology, Epistemology) is the operating system for reality and truth. Psychology (Axiology, Praxeology) is the mechanics of values and execution.

## What is the main idea?

Decode Intelligence — not just Artificial infrastructure. Separate rented compute and commercial LLMs from owned cognitive assets: the Data Substrate, semantic models, verification rules, workflows, and policy guardrails.

## Why five layers?

The MOEPA 5-Layer Framework provides a clean engineering blueprint:

- Metrology — telemetry, measurement, data quality
- Ontology — knowledge graphs, approved vocabularies
- Epistemology — RAG validation, evidence mapping
- Praxeology — workflows, SOPs, agentic playbooks
- Axiology — guardrails, compliance, values

## Where should I start?

**Enterprise and commercial leaders:** [Business Leader Guide](moepa-business-leaders-guide.md) → [Evaluation Checklist](5-Layer-Evaluation-Checklist.md) → [Pitch Strategy](pitch-strategy.md)

**Public sector leaders:** [Public Sector Leader Guide](moepa-public-sector-leaders-guide.md) → [Evaluation Checklist](5-Layer-Evaluation-Checklist.md) → [Pitch Strategy](pitch-strategy.md)

**Technical architects:** [MOEPA 5-Layer Framework](MOEPA-5-Layer-Framework.md) → [Data Substrate Concept](Data-Substrate-Concept.md) → [ARCHITECTURE.md](../ARCHITECTURE.md)

**All readers:** [Glossary](glossary.md) → [Catalog](../catalog/README.md)

## Does this include an implementation?

Not yet. The repository focuses on the proposal, the MOEPA 5-Layer Framework governance model, and the intended operating principles for a governed Data Substrate.

## Why MCP-first?

Vendor orchestration glue (native Bedrock tooling, LangChain chains, framework-specific callbacks) creates lock-in and hides capability boundaries from governance review. The Model Context Protocol (MCP) is the standardized interface: every data, retrieval, workflow, and policy capability is exposed as an MCP server or facade. Orchestrators discover tools through MCP — never by calling RAG or data layers directly. See [Architectural Governance Guidelines](MOEPA-Architectural-Governance-and-Evolution-Guidelines.md).

## What is a Proto-SPO and why does chunking matter?

A **Proto-SPO** (Sovereign Processing Object) is a semantically parsed document segment that carries its own provenance, structure, and context. **Chainsaw chunking** — splitting documents by fixed token counts — destroys tables, sections, and citations. Semantic parsers (Docling, Unstructured, or equivalent) produce Proto-SPOs that preserve meaning from ingestion through retrieval and verification. See [Data Substrate Concept — Semantic Ingestion](Data-Substrate-Concept.md#semantic-ingestion-and-proto-spos) and the [Glossary](glossary.md).