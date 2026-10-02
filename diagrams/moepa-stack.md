# MOEPA Stack Diagram

The MOEPA 5-Layer Framework inside the Philosophical AI Architecture, with the agency-owned Data Substrate foundation.

---

## Full Stack with Data Substrate

```mermaid
graph TB
    subgraph STACK["MOEPA Cognitive Architecture"]
        direction TB

        A5["━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  LAYER 5 — AXIOLOGY · deterministic arbiter\n  Commit · Forbid · Refuse to Act\n  Values · Safety · Compliance\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]

        A4["━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  LAYER 4 — PRAXEOLOGY · deterministic\n  Action space · State transitions\n  Procedural checkpoints\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]

        A3["━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  LAYER 3 — EPISTEMOLOGY · probabilistic\n  Proposes only\n  Belief · Defeater · Ignorance\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]

        A2["━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  LAYER 2 — ONTOLOGY · deterministic\n  Categorical entities and relations\n  Confidence forbidden on the schema\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]

        A1["━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  LAYER 1 — METROLOGY · probabilistic\n  Calibration · Error bounds\n  Disagreement · Provenance\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]

        SUB[["══════════════════════════════════════\n  DATA SUBSTRATE\n  Unified Knowledge Library\n  SPO/Quad + Open Lakehouse (Iceberg/Parquet)\n  Provenance · Versioning · Lineage\n  (shared foundation — all layers read/write here)\n══════════════════════════════════════"]]
    end

    A1 --> A3
    A3 -->|"proposal"| A2
    A2 --> A4
    A4 --> A5
    A5 -->|"Commit"| SUB
    A1 -. observation .-> SUB
    A3 -. envelope .-> SUB

    style SUB fill:#1a3a5c,color:#ffffff,stroke:#4a90d9
    style A1 fill:#2d4a2d,color:#ffffff,stroke:#5a9a5a
    style A2 fill:#3a4a2d,color:#ffffff,stroke:#7a9a5a
    style A3 fill:#4a3a2d,color:#ffffff,stroke:#9a7a5a
    style A4 fill:#4a2d3a,color:#ffffff,stroke:#9a5a7a
    style A5 fill:#3a2d4a,color:#ffffff,stroke:#7a5a9a
```

---

## Layer Definitions at a Glance

| Layer | Domain | AI Governance Role | Core Tool Examples |
|---|---|---|---|
| **5 — Axiology** | Deterministic arbiter | Commit, Forbid, or Refuse to Act | Open Policy Agent, Gatekeeper |
| **4 — Praxeology** | Deterministic | Which transitions are in the action space | LangGraph, Temporal, Camunda |
| **3 — Epistemology** | Probabilistic | Belief, Defeater, or Ignorance — proposal only | Owned RAG, calibrated inference |
| **2 — Ontology** | Deterministic | Categorical entities; no confidence on the schema | Neo4j, Apache Jena, Iceberg |
| **1 — Metrology** | Probabilistic | Calibration, error bounds, disagreement | Great Expectations, OpenLineage |
| **Data Substrate** | *(architectural pattern)* | Shared knowledge library; owned by the organization | Iceberg + Parquet + Neo4j + Atlas |

---

## The Governance Property of the Stack

Control runs from probabilistic proposal to deterministic arbiter. A weak layer fails in a specific way:

- If **Metrology** is weak, proposals rest on uncalibrated observations
- If **Epistemology** is weak, ignorance is flattened into a probability and handed downstream as if it were a belief
- If **Ontology** is weak, confidence leaks onto entities and existence becomes a score
- If **Praxeology** is weak, the action space is "whatever the model called"
- If **Axiology** is weak, a confidence score or a prompt is treated as permission

This is why the [5-Layer Evaluation Checklist](../docs/5-Layer-Evaluation-Checklist.md) uses the **lowest layer score** as the overall recommendation — not an average.

**Cross-cutting integration:** AI orchestrators access layer capabilities only through the **Model Context Protocol (MCP)** — not vendor glue code or direct data/RAG API calls. Semantic ingestion produces **Proto-SPOs** before records enter the substrate. See [Architectural Governance Guidelines](../docs/MOEPA-Architectural-Governance-and-Evolution-Guidelines.md).
