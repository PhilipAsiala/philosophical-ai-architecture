# The Data Substrate: Your Organization's Unified Knowledge Library

> The Data Substrate is the agency-owned knowledge library that all five MOEPA layers read from and write to — truth, values, rules, and lineage in open formats. It is not a scored layer. It is the organizational memory that makes the entire Philosophical AI Architecture coherent and auditable.

---

## The Core Idea

Imagine your organization's knowledge as a library. Five departments — measurement science, domain modeling, fact verification, workflow management, and ethics compliance — all need to use and contribute to that library. 

Without a shared library, each department maintains its own filing system, uses different terminology, and has no way to cross-reference. Audits become impossible. Knowledge is siloed. When staff leave or vendors change, institutional memory disappears.

The **Data Substrate** is the design for that shared library. It is a unified, open-format knowledge store that:
- Every MOEPA layer reads from to ground its work in organizational fact
- Every MOEPA layer writes to when it produces verified knowledge
- Carries full provenance, lineage, and version history for everything stored in it
- Is owned entirely by your organization — not by any vendor

---

## What the Data Substrate Contains

The Data Substrate holds four categories of organizational knowledge:

### 1. Facts and Observations (from Metrology)
Raw, quality-validated data records with full provenance:
- Who collected this data, from what source, at what time
- What quality checks it passed
- Whether it has been updated or superseded
- *Example:* A W-2 wage record, stamped with source (SSA), collection date, validation status, and hash fingerprint

### 2. Entities and Relationships (from Ontology)
Structured representations of your domain's reality:
- Core entities (taxpayer, employer, filing unit, dependent) with canonical definitions
- Relationships between entities (employer issued W-2 to taxpayer for tax year)
- Version history of how definitions have evolved
- *Example:* The knowledge graph entry for "third-party income reporter" including all known relationships to filers in the current tax year

### 3. Verified Knowledge and Decisions (from Epistemology)
Claims that have been validated against evidence:
- Verified facts distinguished from model inferences
- Confidence levels and supporting evidence citations
- Audit trails for how a conclusion was reached
- *Example:* "Taxpayer 123's reported income is verified at 98.3% confidence against 4 independent third-party sources — see records A, B, C, D"

### 4. Workflow Events and Audit Records (from Praxeology and Axiology)
An immutable log of what the system did and why:
- Decision workflow executions with timestamps and approvals
- Human oversight checkpoints and outcomes
- Policy enforcement events (what was blocked and why)
- *Example:* "Audit flag triggered at 14:32 EST, reviewed by examiner ID 4471, approved for escalation — workflow state: ESCALATED"

---

## The SPO/Quad Data Model

The Data Substrate uses a **Subject–Predicate–Object (SPO)** model, extended to a **quad** (four-part) model with a named context:

```
Subject       Predicate              Object              Context/Provenance
──────────    ──────────────────     ─────────────────   ──────────────────
Taxpayer:123  hasReportedIncome      $87,400             Source:W2_SSA_2024
Employer:ABC  filedW2For             Taxpayer:123        FilingDate:2025-01-31
Claim:X47     hasConfidenceScore     0.983               VerifiedBy:EpisLayer_v2.1
```

This model allows:
- **Traversal:** "Show me all income sources for Taxpayer 123 and their verification status"
- **Provenance:** "Who recorded this fact, from what source, when?"
- **Versioning:** "What did we know about this entity on January 15th?"
- **Cross-layer queries:** "Show me all workflow decisions involving records with confidence below 0.9"

---

## Open Formats and Vendor Independence

The Data Substrate is designed using **open, non-proprietary formats** so your organization retains full ownership and portability:

| Component | Recommended Open Standard | What It Stores |
|---|---|---|
| **Lakehouse storage** | Apache Iceberg + Apache Parquet | Tabular facts, observations, metrics |
| **Knowledge graph** | RDF/SPARQL or property graph (Neo4j export) | Entities, relationships, ontology |
| **Document/blob storage** | Open object storage (S3-compatible, self-hosted) | Source documents, evidence artifacts |
| **Catalog metadata** | Apache Atlas / open catalog standards | Data lineage, schema, provenance |
| **Version control** | Git-compatible versioning | Schema changes, ontology versions |

> **Why open formats matter:** If your data is stored in a vendor's proprietary format, migrating away requires their cooperation. With open formats, you own an asset that can be moved to any infrastructure provider — or run on-premises — at any time.

---

## Provenance and Lineage: The Accountability Chain

Every record in the Data Substrate carries a **provenance record** answering four questions:

1. **Origin** — Where did this data come from? (source system, external reporter, internal process)
2. **Transformation** — What happened to it on the way in? (cleaning, normalization, validation)
3. **Validation** — What quality checks did it pass, and when?
4. **Custody** — Who has accessed, modified, or acted on it?

This provenance chain is what makes AI-assisted decisions **auditable and defensible**. When an oversight body asks "How did you reach this conclusion?", the answer is not "the model said so" — it is a traceable chain of evidence, transformations, and human approvals.

---

## Versioning: Knowledge That Evolves Correctly

The Data Substrate maintains **version history** for:
- **Ontology definitions** — when entity meanings or relationship structures change
- **Policy and guardrail configurations** — which version of compliance rules was active when a decision was made
- **Fact records** — when a source record is updated or corrected, the history is preserved
- **Model configurations** — which model version was used for which decisions

This enables **point-in-time reconstruction**: the ability to reproduce exactly what the system knew and how it reasoned at any historical moment. For tax administration, benefits programs, and regulatory enforcement, this is a legal and compliance necessity.

---

## The Substrate vs. a Vendor Data Platform

| Capability | Organization-Owned Data Substrate | Vendor Data Platform |
|---|---|---|
| Data portability | Full — open formats, self-hosted | Limited — vendor-dependent export |
| Provenance control | Complete organizational ownership | Vendor defines and controls lineage |
| Schema/ontology ownership | Yours | Typically vendor-defined |
| Audit access | Unrestricted, direct | Subject to vendor API and terms |
| Switching cost | Low — data moves with you | High — schema and history may not transfer |
| Compliance evidence | Produced by your systems | Dependent on vendor-supplied reports |

---

## What the Data Substrate Is Not

- **Not a data warehouse** — it is a knowledge store with semantics, provenance, and versioning, not just rows and columns
- **Not a vendor product** — it is an architectural pattern implemented with open tools
- **Not a scored MOEPA layer** — it is the shared foundation all layers depend on
- **Not optional** — without it, the five layers have no shared organizational memory, and the framework collapses into siloed tools

---

## Getting Started

A Data Substrate can be built incrementally. A practical starting sequence:

1. **Inventory existing data sources** — what does your agency hold, where, in what format?
2. **Define your core entity model** — what are the 10–20 most important entities in your domain?
3. **Establish provenance standards** — what must be recorded for each incoming data record?
4. **Select open-format storage** — start with Iceberg/Parquet for tabular data; add a graph store when ready
5. **Integrate the MOEPA layers** — connect each layer to read from and write to the shared substrate

---

## Related Documents

- [MOEPA 5-Layer Framework](MOEPA-5-Layer-Framework.md) — how each layer uses the substrate
- [Catalog](../catalog/README.md) — capabilities, tools, patterns, and cross-layer guidance (including for the Data Substrate)
- [Full Architecture Specification](../ARCHITECTURE.md) — technical design details
