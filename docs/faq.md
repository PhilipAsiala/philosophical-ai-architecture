# FAQ

## Is the Data Substrate a sixth layer?

No. The Data Substrate (Set-Theoretic Backbone) is the shared representation and storage backbone beneath all five layers — an SPO/quad triple store plus lakehouse — that every layer stores into. It is **not** a scored layer. The five scored disciplines (Metrology, Ontology, Epistemology, Praxeology, Axiology) and the 1–5 per-layer scoring model remain unchanged. See §5.1 of [ARCHITECTURE.md](../ARCHITECTURE.md) for the full substrate specification.

## Is this a finished architecture?

No. This repository describes a draft **MOEPA Architecture** for discussion, refinement, and review. The **MOEPA Framework** (scoring and governance) and **MOEPA Cognitive Architecture** (technical specification in [ARCHITECTURE.md](../ARCHITECTURE.md)) are views within that model — all are proposals, not deployed systems. See the [Glossary](glossary.md) for term definitions.

## What is the difference between MOEPA Architecture, MOEPA Framework, and MOEPA Cognitive Architecture?

- **MOEPA Architecture** — the full model: five layers, Data Substrate, Catalog, and information flow.
- **MOEPA Framework** — the governance layer: scoring rubric, intake checklists, GO / CONDITIONAL GO / NO-GO decisions.
- **MOEPA Cognitive Architecture** — the technical stack design in [ARCHITECTURE.md](../ARCHITECTURE.md): storage mapping, catalog integration, recommended tools.

See the [Naming section in the README](../README.md#naming) and the [Glossary](glossary.md) for details.

## What is the main idea?

The main idea is to separate rented compute from owned cognitive assets so the organization controls its data, semantics, verification, workflow, and policy layers.

## Why five layers?

The five layers provide a clean way to separate concerns:

- Metrology for measurement and data quality
- Ontology for domain structure
- Epistemology for verification and truth
- Praxeology for agentic action
- Axiology for governance and values

## Where should I start?

If you are a leader, start with the [Leader Guide](moepa-business-leaders-guide.md), then read [Business Value](business-value.md), then use the [Catalog](../catalog/README.md).

If you need the full reference model, continue with [Quick Start](quick-start.md), [Glossary](glossary.md), and [ARCHITECTURE.md](../ARCHITECTURE.md).

## Does this include an implementation?

Not yet. The repository currently focuses on the proposal, the governance model, and the intended operating principles.
