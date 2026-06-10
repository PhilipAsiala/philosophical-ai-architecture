# Glossary

## Data Substrate (Set-Theoretic Backbone)

The cross-cutting representation medium — an SPO/quad backbone (Subject-Predicate-Object, quads with context) plus lakehouse storage — that all five MOEPA layers store into. The substrate holds each base fact once; every layer attaches its own metadata envelope (epistemic, praxeological, axiological, etc.) without duplicating the base triple. It is the shared storage and representation infrastructure beneath the five scored disciplines and is explicitly **not** a sixth scored layer.

## SPO Triple / Quad

A Subject-Predicate-Object triple (or quad, when a context/graph identifier is added as a fourth element) used as the universal structural unit of the MOEPA Data Substrate. Example: `(IncomeVerification:TX12345, hasAmount, 85000)`. All layer-specific metadata envelopes attach to this base triple rather than replacing it.

## MOEPA

The five-layer framework used in the proposal:

- Metrology: measurement and data foundation
- Ontology: structured reality and knowledge representation
- Epistemology: truth, verification, and justification
- Praxeology: purposeful action and workflow governance
- Axiology: value, ethics, and policy alignment

## Proposed Architecture

A draft design that describes how an AI system could be organized. In this repository, the architecture is conceptual and under review, not a deployed implementation.

## Owned Brain

The idea that the organization should own its semantic models, validation rules, policy controls, and knowledge assets rather than outsourcing them to a vendor.

## Rented Compute

Commodity infrastructure such as GPUs, clusters, or cloud capacity that can be swapped or scaled independently from the cognitive architecture.

## MOEPA Catalog

A proposed internal catalog for discovering, versioning, governing, and auditing the assets used across the architecture.

## Golden Master

A locked configuration baseline used in the axiological layer to preserve policy and prevent easy modification.
