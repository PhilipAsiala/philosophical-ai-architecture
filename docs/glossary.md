# Glossary

## Philosophical AI Architecture

The overarching enterprise ecosystem for governing machine intelligence: the **Data Substrate**, **MOEPA Catalog**, security guardrails, own-vs-rent strategy, and cognitive control plane. It decodes Intelligence — not just Artificial infrastructure — by mapping human cognitive functions (Cognition, Affect, Conation) into strict, governable software. **Philosophical AI Architecture** is the canonical name for the whole system. This repository is its reference specification.

## MOEPA 5-Layer Framework

The operational engineering blueprint and governance engine *inside* the Philosophical AI Architecture. It classifies institutional knowledge across five layers and provides the intake scoring rubric (1–5 per layer, GO / CONDITIONAL GO / NO-GO). Use this term for project evaluation, engineering translation, and layer-by-layer accountability — never as a synonym for the full ecosystem.

## MOEPA Cognitive Architecture

The technical stack design within the Philosophical AI Architecture, as specified in [ARCHITECTURE.md](../ARCHITECTURE.md): layer implementations, Data Substrate storage mapping, catalog integration, recommended technology stack, and implementation playbook.

## Cognition, Affect, Conation

The three human cognitive functions the Philosophical AI Architecture maps into software:

- **Cognition** (knowing) — how the system defines and verifies reality → Metrology, Ontology, Epistemology
- **Affect** (valuing) — how the system encodes what matters and what is forbidden → Axiology
- **Conation** (acting) — how the system executes decisions under oversight → Praxeology

## Philosophy vs. Psychology (in the stack)

- **Philosophy** — the operating system of cognition: strict logical rules for defining reality and truth (Metrology, Ontology, Epistemology).
- **Psychology** — the mechanics of behavior: how values and execution drives steer the engine (Axiology, Praxeology).

## Data Substrate (Set-Theoretic Backbone)

The agency-owned knowledge library — the cross-cutting representation medium where truth, values, rules, and lineage live in open, portable formats. At end state: an SPO/quad backbone plus federated lakehouse storage that all five MOEPA layers read from and write to. The substrate holds each base fact once; every layer attaches its own metadata envelope without duplicating the base triple. Explicitly **not** a sixth scored layer. Agencies evolve toward end state incrementally; see [Substrate Evolution Path](#substrate-evolution-path).

## Substrate End State

The imperative logical target for a mature Data Substrate: owned SPO/quad representation, one base fact per triple, layer metadata envelopes, SPO-centric hypergraph + lakehouse federation, and cross-layer queryability. Not optional once the substrate is considered enterprise-ready.

## Substrate Evolution Path

The allowed incremental journey from current agency storage to Substrate End State — typically lakehouse (SPO-compatible schemas) → pilot triple store → enterprise graph → federation layer. Interim implementations are valid when agency-owned, open-format, provenance-complete, and backed by a documented migration roadmap.

## SPO Triple / Quad

At end state, the universal structural unit of the Data Substrate: a Subject-Predicate-Object triple (or quad, when a context/graph identifier is added as a fourth element). Example: `(IncomeVerification:TX12345, hasAmount, 85000)`. Earlier evolution stages must maintain SPO-compatible mapping so records can converge to this form without semantic loss.

## MOEPA

The acronym for the five layers at the heart of the MOEPA 5-Layer Framework:

- Metrology: measurement, telemetry, and data foundation
- Ontology: structured reality and knowledge representation
- Epistemology: truth, verification, and justification
- Praxeology: purposeful action and workflow governance
- Axiology: value, ethics, and policy alignment

## MOEPA Catalog

The routing and governance catalog inside the Philosophical AI Architecture — for discovering, versioning, deduplicating, and auditing assets across all five layers. Federal intake requires leaders to prove how a project enriches this catalog.

## Owned Brain

The organization owns its Data Substrate, semantic models, validation rules, policy controls, and catalog — rather than outsourcing them to a vendor.

## Rented Compute

Commodity infrastructure (GPUs, clusters, cloud capacity, commercial LLM APIs) that the organization rents while retaining sovereignty over the cognitive layers and Data Substrate.

## Golden Master

A locked configuration baseline used in the axiological layer to preserve policy and prevent easy modification.

## Cognitive Control Plane

The combined governance surface — MOEPA 5-Layer Framework intake scoring, MOEPA Catalog deduplication, and Data Substrate ownership — that lets leadership govern an AI mind without relying on standard IT infrastructure metrics alone.