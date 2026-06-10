# Layer 2 — Ontology: Structured Knowledge and Meaning

> **Core principle:** AI systems must represent domain reality as structured, queryable knowledge — not just flat text. Ontology capabilities ensure your organization owns the definitions, entities, and relationships that the system uses to understand your domain.

---

## What Ontology Covers

| Capability Domain | Description |
|---|---|
| **Entity modeling** | Defining the core "things" in your domain and their properties |
| **Relationship mapping** | Explicitly representing how entities relate to each other |
| **Semantic consistency** | Ensuring the same terms mean the same things across all systems |
| **Knowledge graph management** | Building and maintaining a queryable graph of domain knowledge |
| **Schema versioning** | Tracking how definitions evolve over time |

---

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

## Recommended Tools

### Self-Hosted / Open Source (Preferred)

| Tool | Category | Description |
|---|---|---|
| **Neo4j** | Knowledge graph | Leading open-source graph database; Cypher query language; strong ecosystem |
| **Apache Jena / TDB2** | RDF triple store | Open-source RDF framework with SPARQL query support; W3C standards-compliant |
| **Oxigraph** | Lightweight RDF store | Rust-based, embeddable RDF store; fast and portable |
| **Weaviate** | Vector + graph hybrid | Open-source vector database with graph capabilities; self-hostable |
| **Chroma** | Vector database | Lightweight open-source embedding store; ideal for self-hosted RAG |
| **Qdrant** | Vector database | High-performance open-source vector search; Rust-based, self-hostable |
| **spaCy + Prodigy** | NLP / entity extraction | Industrial-strength NLP; custom entity recognition for domain-specific terms |
| **Protégé** | Ontology editor | Open-source ontology editor (OWL/RDF); widely used in government and academia |
| **SKOS** | Vocabulary standard | W3C standard for controlled vocabularies and thesauri |

### Deployment Notes

- **For knowledge graphs:** Neo4j Community Edition is free and suitable for most government use cases; enterprise features require a license
- **For RDF/SPARQL:** Apache Jena is the mature, battle-tested open-source option
- **For vector search (self-hosted RAG):** Chroma is lightweight; Qdrant is more performant at scale
- **For ontology authoring:** Protégé is the standard tool in government and academic contexts

---

## Patterns

### Pattern O-A: Domain Entity Canonical Register
Maintain a single JSON-LD or OWL file per major entity type, version-controlled in Git. Each entity definition includes: canonical name, aliases, properties, relationships, statutory or regulatory citation, effective date, and approving authority.

### Pattern O-B: Graph-Augmented Retrieval
When answering a query about a specific entity (e.g., a taxpayer), traverse the knowledge graph to gather related entities (employers, income sources, agents) before generating a response. This grounds the AI response in structured, owned knowledge rather than unstructured text search alone.

### Pattern O-C: Ontology-Validated Ingestion
Before a new data record enters the Data Substrate, validate that all entity references (taxpayer ID, employer EIN) resolve correctly in the canonical entity registry. Records referencing unknown entities are flagged for resolution before processing.

---

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| Entity definitions managed by vendor | Domain knowledge is rented; migration loses institutional meaning | "The vendor's data model handles that" |
| No cross-system entity reconciliation | Same entity has different identifiers in different systems | Matching errors; duplicate records |
| Embeddings generated by vendor API | Knowledge is processed outside agency control | "We use [Vendor] Embeddings API" |
| No version history for schema changes | Cannot interpret historical records correctly | "We updated the schema but didn't document what changed" |
| Flat keyword search instead of graph | Complex relationship queries not supported | Investigation requires manual research |

---

## Related Capabilities

- **Metrology (Layer 1):** Ontology entity identifiers must align with Metrology's provenance records; quality validation depends on consistent entity definitions.
- **Epistemology (Layer 3):** Fact verification grounds claims against Ontology's entity model; RAG retrieval uses the owned vector index.
- **Data Substrate:** The knowledge graph and entity registry are core components of the Data Substrate's semantic layer.
