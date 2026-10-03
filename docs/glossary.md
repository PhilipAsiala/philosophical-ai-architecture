# Glossary

## Business First

The repository's primary communication rule: MOEPA philosophical disciplines describe **business outcomes** leaders must own (trusted data, shared meaning, verifiable truth, governed action, enforced values). Technical implementation detail belongs in builder-tier documents (`ARCHITECTURE.md`, governance guidelines, catalog tools). See [pitch strategy §0](pitch-strategy.md).

## Philosophical AI Architecture

The overarching enterprise ecosystem for governing machine intelligence: the **Data Substrate**, **MOEPA Catalog**, security guardrails, own-vs-rent strategy, and cognitive control plane. It decodes Intelligence — not just Artificial infrastructure — by mapping human cognitive functions (Cognition, Affect, Conation) into strict, governable software. **Philosophical AI Architecture** is the canonical name for the whole system. This repository is its reference specification.

## MOEPA 5-Layer Framework

The operational engineering blueprint and governance engine *inside* the Philosophical AI Architecture. It classifies institutional knowledge across five layers and provides the intake scoring rubric (1–5 per layer, GO / CONDITIONAL GO / NO-GO). Use this term for project evaluation, engineering translation, and layer-by-layer accountability — never as a synonym for the full ecosystem.

## MOEPA Cognitive Architecture

The technical stack design within the Philosophical AI Architecture, as specified in [ARCHITECTURE.md](../ARCHITECTURE.md): layer implementations, Data Substrate storage mapping, catalog integration, recommended technology stack, and implementation playbook.

## Cognition, Affect, Conation

The three human cognitive functions the Philosophical AI Architecture maps into software. This map describes *what kind of question* a layer answers. Runtime authorization uses the [dual-domain partition](#dual-domain-partition) below.

- **Cognition** (knowing) — Metrology and Epistemology propose; Ontology holds the categorical model those proposals are about
- **Affect** (valuing) — Axiology, the final arbiter
- **Conation** (acting) — Praxeology, the action space

## Dual-Domain Partition

The runtime cut inside the MOEPA Cognitive Architecture. Specified in [ARCHITECTURE.md](../ARCHITECTURE.md) §1.3.

- **Probabilistic domain** — Metrology and Epistemology. They measure and propose. They do not commit entities or authorize action.
- **Deterministic domain** — Ontology, Praxeology, and Axiology. They commit categorical state, admit transitions, and issue verdicts.

## Epistemic State

The three outputs Epistemology is required to keep distinct:

- **Belief** — a partial claim with confidence, justification, and any metrological error bounds.
- **Defeater** — a specific reason a belief cannot stand. Not a lower probability of the same claim.
- **Ignorance** — "I don't know." Not a flat distribution over the answers.

## Epistemic Firewall

The rule that uncertainty attaches only to epistemic claims. Ontological schemas (RDF triples, Iceberg entity tables, and equivalents) do not carry confidence, probability, or "maybe" as a property of existence.

## Axiological Verdict

The only permission Axiology may return, and the only authorization for systemic commitment:

- **Commit** — write the categorical state and perform the admitted action.
- **Forbid** — the act is in the action space and violates a value, safety, or compliance rule. Do not commit.
- **Refuse to Act** — the proposal is Ignorance or has an unresolved defeater, or a required precondition is absent. Commit nothing. Do not pretend a decision was made.

## Probabilistic Proposal

The object Epistemology hands to the deterministic domain: an epistemic state, citations, and (when the state is Belief) a calibrated confidence. A proposal is not a permission. In the reference pipeline this object is an `UncommittedCandidate`.

## State Collapse

The deterministic step that turns a continuous proposal into one discrete action before any policy agent runs. A unique mode is kept. A tie, a defeater, or ignorance yields no commit-eligible action. Collapse does not sample, and it does not authorize.

## Deterministic Policy Agent

A rule, schema, or policy-as-code check that returns pass or fail. The reference agents are `OntologyPolicyAgent`, `PraxeologyPolicyAgent`, and `AxiologyPolicyAgent`, in that order. Their input has no confidence field. Axiology is last. The pipeline outcome is committed or blocked.

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
- Epistemology: probabilistic inference; Belief, Defeater, and Ignorance (proposes, does not commit)
- Praxeology: action-space validation and state transitions
- Axiology: final arbiter; Commit, Forbid, or Refuse to Act

## MOEPA Catalog

The routing and governance catalog inside the Philosophical AI Architecture — for discovering, versioning, deduplicating, and auditing assets across all five layers. Enterprise and public sector intake requires leaders to prove how a project enriches this catalog.

## Owned Brain

The organization owns its Data Substrate, semantic models, validation rules, policy controls, and catalog — rather than outsourcing them to a vendor.

## Rented Compute

Commodity infrastructure (GPUs, clusters, cloud capacity, commercial LLM APIs) that the organization rents while retaining sovereignty over the cognitive layers and Data Substrate.

## Golden Master

A locked configuration baseline used in the axiological layer to preserve policy and prevent easy modification.

## Cognitive Control Plane

The combined governance surface — MOEPA 5-Layer Framework intake scoring, MOEPA Catalog deduplication, and Data Substrate ownership — that lets leadership govern an AI mind without relying on standard IT infrastructure metrics alone.

## Model Context Protocol (MCP)

The standardized interface for all data and tool access in the MOEPA Cognitive Architecture. MCP keeps capabilities portable across orchestration hosts (Bedrock, self-hosted runtimes, or equivalent) and prevents vendor-locked glue code from becoming the integration layer.

## MCP Server

An MCP-compliant service that exposes a governed capability — ingestion, retrieval, workflow step, policy check — with a stable tool contract. New capabilities are defined as MCP servers so execution logic remains inspectable and host-independent.

## MCP Facade

A thin MCP wrapper around a legacy or high-throughput API. Used when direct integration is required for performance, but orchestrators must still discover and govern the capability through MCP rather than calling the underlying API directly.

## Proto-SPO (Sovereign Processing Object)

A semantically parsed document segment that carries its own provenance, structure, and context — not a naive text chunk. Proto-SPOs are the ingestion-stage precursors to owned SPO/quad records on the Data Substrate. They preserve semantic intent from source document through retrieval and verification.

## Semantic Ingestion

Document-aware parsing during data ingress (for example: Docling, Unstructured, or equivalent) that produces Proto-SPOs with provenance and structural metadata. Explicitly excludes "chainsaw chunking" — fixed-size splits that discard document structure and semantic boundaries.