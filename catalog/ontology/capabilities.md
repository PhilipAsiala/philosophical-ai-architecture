# Ontology Capabilities

## What Leaders Need to Know

Bottom line: this layer gives the institution a shared model of reality. Without it, different systems, vendors, and programs may disagree about what a customer, business, account, or relationship actually is.

See [ARCHITECTURE.md](../../ARCHITECTURE.md) for the strategic rationale and [Business Value](../../docs/business-value.md) for the investment lens.

## Mission and Governance Outcomes

- More consistent reasoning across programs and systems.
- Better reuse of institutional knowledge across initiatives.
- Reduced semantic lock-in to vendor-specific data models.
- Clearer accountability for how core entities and relationships are defined.

## What Ontology Covers

| Capability Domain | Description |
|---|---|
| **Entity modeling** | Defining the core "things" in your domain and their properties |
| **Relationship mapping** | Explicitly representing how entities relate to each other |
| **Semantic consistency** | Ensuring the same terms mean the same things across all systems |
| **Knowledge graph management** | Building and maintaining a queryable graph of domain knowledge |
| **Schema versioning** | Tracking how definitions evolve over time |

## Core Capabilities

### O1 — Canonical Entity Registry
**What it does:** Maintains a single authoritative definition for each core entity in your domain — with versioning, ownership, and cross-system identifiers.

**Why it matters for government:** In a tax administration context, "taxpayer," "filer," "legal entity," and "beneficial owner" must have precise, consistent definitions that are the same across every system. When they are not, matching and verification become unreliable.

**Minimum acceptable standard (Score 3):** Core entities documented in a data dictionary with agreed definitions.

**Good practice (Score 4–5):** Formally modeled entity registry with version history; canonical identifiers used across all systems; policy-aligned definitions reviewed and approved by domain owners.

---

### O2 — Knowledge Graph
**What it does:** Represents entities and their relationships in a queryable graph structure — enabling complex queries like "show me all income sources connected to this taxpayer and their verification status."

**Why it matters for government:** Flat databases answer simple questions. Complex compliance and investigation questions require traversing relationships: who owns what entity, which employer issued income to which individuals, which agent acted on behalf of which filer. A knowledge graph makes these queries fast and auditable.

**Minimum acceptable standard (Score 3):** Key entity relationships documented; basic graph or relational model available for core queries.

**Good practice (Score 4–5):** Live, internally managed knowledge graph; relationships evolve with policy changes; graph queries available for investigative and compliance workflows.

---

### O3 — Embedding and Vector Index (Owned)
**What it does:** Converts organizational knowledge (documents, rules, case records) into vector representations for similarity search — owned and self-hosted by the agency.

**Why it matters for government:** RAG (Retrieval-Augmented Generation) systems use vector search to find relevant context for AI responses. If the vector index is hosted by a vendor, the agency's documents and knowledge are processed in an environment it does not control.

**Minimum acceptable standard (Score 3):** Vector index exists for key document collections; hosted within agency-controlled infrastructure.

**Good practice (Score 4–5):** Agency-managed embedding pipeline; vector index updated automatically when source documents change; index versioned and auditable.

---

### O4 — Taxonomy and Controlled Vocabulary
**What it does:** Maintains official taxonomies, code sets, and controlled vocabularies for classification — e.g., income type codes, entity type classifications, NAICS industry codes.

**Why it matters for government:** Inconsistent classification creates comparison and aggregation errors. When "self-employment income" is coded differently by different systems, analysis across systems produces incorrect totals.

**Minimum acceptable standard (Score 3):** Core taxonomies documented; consistent coding enforced for primary workflows.

**Good practice (Score 4–5):** Governed vocabulary service; automated validation against canonical code sets; versioned; aligned to statutory definitions.

---

### O5 — Ontology Versioning and Change Management
**What it does:** Tracks changes to entity definitions, relationships, and schemas over time — with effective dates so historical records can be interpreted correctly.

**Why it matters for government:** If the definition of "qualifying dependent" changes with new legislation, historical records need to be interpretable under the rules in effect at the time they were created. Ontology versioning makes this possible.

**Minimum acceptable standard (Score 3):** Major schema changes documented with effective dates.

**Good practice (Score 4–5):** Formal version control for all ontology changes; point-in-time query capability; change review process aligned to policy update cycle.

---

## Capability Matrix

The matrix below binds the minimum set of Ontology capabilities to **Score 3 — Defined & Contained — Minimum Acceptable Standard** in the existing [Ontology scoring guide](scoring.md). Capabilities that contribute to Scores 4 and 5 lift the layer beyond that baseline. Live delivery status should be tracked through the [Praxeology workflow](../praxeology/tools.md); the JIRA epic column below is illustrative only.

| Capability | Minimum set? (Score 3) | Maturity contribution (3 / 4 / 5) | Owner | Delivery tracking (illustrative: JIRA epic) |
| --- | --- | --- | --- | --- |
| Entity modeling for customers, businesses, accounts, and related actors | Yes | 3 — establishes governable core entities for the mission domain | Domain ontology owner | Illustrative: JIRA epic for core entity modeling |
| Relationship mapping across legal, financial, and operational domains | Yes | 3 — defines governable institutional relationships across key domains | Domain ontology owner | Illustrative: JIRA epic for relationship mapping |
| Knowledge graph construction with hierarchy and taxonomy support | No | 4 — expands reuse and institutional consistency through richer semantic governance | Knowledge graph owner | Illustrative: JIRA epic for knowledge graph and taxonomy build-out |
| Semantic linking to connect meaning across heterogeneous datasets | Yes | 3 / 4 — provides shared meaning across governed sources and improves reuse across programs | Domain integration owner | Illustrative: JIRA epic for semantic linking across datasets |
| Advanced graph querying with dynamic relationship updates | No | 5 — supports enterprise-scale reasoning and continuously evolving semantic operations | Knowledge graph owner | Illustrative: JIRA epic for advanced graph query services |
| Controlled integration with Metrology outputs | Yes | 3 — keeps semantic assets grounded in governed source data | Data and ontology steward | Illustrative: JIRA epic for ontology-to-metrology integration |

## Questions Leaders Should Ask Before Funding

- Are the key entities and relationships defined clearly enough for governance review?
- Who owns those definitions, and how are changes approved?
- If programs disagree about the meaning of a customer, business, or relationship, how is that resolved?
- Does the organization own the semantic model, or is that knowledge embedded inside a vendor platform?

## Related

See also the layer overview in [Ontology README](README.md), [scoring guide](scoring.md), [tools](tools.md), and [patterns](patterns.md). Cross-layer interactions are described in [cross-layer-compositions.md](../cross-layer-compositions.md).
