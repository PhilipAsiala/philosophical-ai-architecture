# Glossary

## MOEPA Architecture

The complete draft model for organizing and governing AI capability: the five scored layers (Metrology, Ontology, Epistemology, Praxeology, Axiology), the Data Substrate, the MOEPA Catalog, and the information flows that connect them. In this repository, the MOEPA Architecture is conceptual and under review — not a deployed implementation. **MOEPA Architecture** is the canonical name for the whole proposal.

## MOEPA Framework

The governance layer within the MOEPA Architecture: per-layer scoring (1–5), GO / CONDITIONAL GO / NO-GO decision bands, intake checklists, own-vs-rent guidance, and executive review processes. Use this term when the subject is evaluation, approval, or investment decisions — not the structural layer model itself.

## MOEPA Cognitive Architecture

The technical stack design within the MOEPA Architecture, as specified in [ARCHITECTURE.md](../ARCHITECTURE.md): layer implementations, Data Substrate storage mapping, catalog integration, recommended technology stack, and implementation playbook. Use this term when the subject is how the model is built and operated, not how proposals are scored.

## Data Substrate (Set-Theoretic Backbone)

The cross-cutting representation medium — an SPO/quad backbone (Subject-Predicate-Object, quads with context) plus lakehouse storage — that all five MOEPA layers store into. The substrate holds each base fact once; every layer attaches its own metadata envelope (epistemic, praxeological, axiological, etc.) without duplicating the base triple. It is the shared storage and representation infrastructure beneath the five scored disciplines and is explicitly **not** a sixth scored layer.

## SPO Triple / Quad

A Subject-Predicate-Object triple (or quad, when a context/graph identifier is added as a fourth element) used as the universal structural unit of the MOEPA Data Substrate. Example: `(IncomeVerification:TX12345, hasAmount, 85000)`. All layer-specific metadata envelopes attach to this base triple rather than replacing it.

## MOEPA

The acronym for the five-layer model at the heart of the MOEPA Architecture:

- Metrology: measurement and data foundation
- Ontology: structured reality and knowledge representation
- Epistemology: truth, verification, and justification
- Praxeology: purposeful action and workflow governance
- Axiology: value, ethics, and policy alignment

## Owned Brain

The idea that the organization should own its semantic models, validation rules, policy controls, and knowledge assets rather than outsourcing them to a vendor.

## Rented Compute

Commodity infrastructure such as GPUs, clusters, or cloud capacity that can be swapped or scaled independently from the MOEPA Cognitive Architecture.

## MOEPA Catalog

A proposed internal catalog for discovering, versioning, governing, and auditing the assets used across the MOEPA Architecture.

## Golden Master

A locked configuration baseline used in the axiological layer to preserve policy and prevent easy modification.