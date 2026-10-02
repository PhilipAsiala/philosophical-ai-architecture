# Information Flow Across MOEPA Layers

How a case moves through the Philosophical AI Architecture: the probabilistic domain proposes, and the deterministic domain arbitrates. Nothing is committed until Axiology returns **Commit**.

---

## End-to-End Information Flow

```mermaid
flowchart TD
    SRC["External Sources\n(Third-party reporters, APIs,\ndocuments, sensor data)"]

    subgraph M["LAYER 1 — METROLOGY (probabilistic)"]
        M0["Semantic Parsing\n(Docling / Unstructured)\n→ Proto-SPOs"]
        M1["Quality Gate\n(completeness, accuracy,\nformat validation)"]
        M2["Provenance Stamp\n(source, timestamp, hash,\nquality results)"]
        M3["Data Observability\n(drift detection, profiling,\nanomalies)"]
    end

    MCP["MCP Integration Layer\n(orchestrators discover\ntools here only)"]

    subgraph SUB["DATA SUBSTRATE (Shared)"]
        DS["Open-Format Lakehouse\n+ Knowledge Graph\n+ Audit Log\n(Iceberg / Parquet / Neo4j)"]
    end

    subgraph O["LAYER 2 — ONTOLOGY (deterministic)"]
        O1["Match proposal to schema\n(categorical candidate)"]
        O2["Firewall\n(reject confidence on the entity)"]
    end

    subgraph E["LAYER 3 — EPISTEMOLOGY (probabilistic)"]
        E1["Retrieve owned evidence"]
        E2["Infer a proposal\nBelief · Defeater · Ignorance"]
        E3["Attach citations and\ncalibrated confidence\n(envelope only)"]
    end

    subgraph P["LAYER 4 — PRAXEOLOGY (deterministic)"]
        P1["Action-space check\n(verb, state, procedure)"]
        P2["Human checkpoint\n(a required state, not a score)"]
        P3["Execute only after Commit"]
    end

    subgraph A["LAYER 5 — AXIOLOGY (final arbiter)"]
        A1{"Verdict"}
        A2["Commit"]
        A3["Forbid"]
        A4["Refuse to Act"]
    end

    OUT["Governed Output\n(decision / recommendation /\naction with full audit trail)"]

    ORCH["AI Orchestrator\n(Bedrock / LangGraph /\nagent runtime)"]

    ORCH --> MCP
    MCP -. "tool calls" .-> E1
    MCP -. "tool calls" .-> P1
    MCP -. "tool calls" .-> A1

    SRC --> M0
    M0 --> M1
    M1 -->|"PASS"| M2
    M1 -->|"FAIL"| QUARANTINE["Quarantine +\nAlert + Escalation"]
    M2 --> M3
    M2 --> DS
    M3 --> DS

    DS --> E1
    E1 --> E2
    E2 --> E3

    E3 -->|"Belief"| O1
    E3 -->|"Ignorance or defeater"| A4
    O1 --> O2
    O2 -->|"candidate triple\n(uncommitted)"| P1
    P1 -->|"not viable"| A4
    P1 -->|"viable, checkpoint required"| P2
    P1 -->|"viable, no checkpoint"| A1
    P2 -->|"checkpoint met"| A1
    P2 -->|"checkpoint absent"| A4
    A1 -->|"Commit"| A2
    A1 -->|"Forbid"| BLOCKED["Forbid\n+ violation log\n(no write)"]
    A2 --> P3
    A4 --> REFUSE["Refuse to Act\n(no write)"]
    P3 --> DS
    P3 --> OUT

    style DS fill:#1a3a5c,color:#ffffff
    style OUT fill:#1a4a1a,color:#ffffff
    style BLOCKED fill:#4a1a1a,color:#ffffff
    style QUARANTINE fill:#4a3a1a,color:#ffffff
    style REFUSE fill:#3a2a4a,color:#ffffff
```

---

## Key Handoffs Between Layers

### Metrology → Data Substrate
Every record that passes Metrology's quality gate is stored as an observation: value, unit, provenance, calibration, and error bounds. That write is not an entity commitment.

**What passes:** A qualified measurement  
**What gets added:** Observational lineage and disagreement flags

---

### Epistemology → Ontology
Epistemology reads owned evidence, including the standing schema, and emits one proposal: Belief, Defeater, or Ignorance. Ontology turns a Belief into an uncommitted candidate triple only when the schema matches. Confidence stays in the epistemic envelope.

**What passes:** A proposal  
**What gets added:** A categorical candidate, or a rejection if the write would put uncertainty on the entity

---

### Epistemology → Ontology → Praxeology
Epistemology emits one proposal. The epistemic state is Belief, Defeater, or Ignorance. Confidence, when present, stays in the envelope.

Ontology accepts a candidate triple only when it matches a discrete schema. It rejects any write that would put confidence on the entity. The candidate is not yet committed.

Praxeology then tests the action space: current state, allowed verb, and procedural preconditions. A human checkpoint is one of those preconditions. A confidence cutoff is not.

---

### Praxeology → Axiology → Output
Axiology is the final arbiter. It returns exactly one verdict:

- **Commit** — write the triple and perform the admitted action
- **Forbid** — the act violates a value or compliance rule; write nothing for that act
- **Refuse to Act** — the proposal is Ignorance, a defeater is unresolved, or a precondition is absent; write nothing and do not pretend a decision was made

**What passes:** An admitted candidate plus its epistemic envelope  
**What gets added:** The verdict, the rule id, and the compliance log entry

---

## What the Data Substrate Stores After Each Layer

| Layer | Records Written to Substrate |
|---|---|
| Metrology | Observations with provenance, calibration, and error bounds. Not entity commitments. |
| Epistemology | Proposals: epistemic state, citations, and confidence only inside the envelope. |
| Ontology | Categorical triples, and only when the verdict on that proposal is Commit. |
| Praxeology | Admission records: state, verb, precondition results. No confidence edge. |
| Axiology | Verdict records: Commit, Forbid, or Refuse to Act, with rule id. |

The Data Substrate accumulates observations and proposals immediately, and categorical facts only after Commit. Forbid and Refuse to Act are themselves durable records. They are not silent drops.

---

## MCP Integration Boundary

AI orchestrators (Bedrock Agents, LangGraph routers, policy-governed agent runtimes)
discover and invoke layer capabilities **only through MCP** — never by calling
data, RAG, or workflow APIs directly. Semantic ingestion, retrieval,
verification, workflow steps, and policy checks are each exposed as MCP servers
or facades. See [Architectural Governance Guidelines](../docs/MOEPA-Architectural-Governance-and-Evolution-Guidelines.md).
