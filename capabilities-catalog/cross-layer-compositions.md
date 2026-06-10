# Cross-Layer Capability Compositions

> Multi-layer capability patterns — showing how MOEPA layers work together for complex, real-world government AI use cases.

---

## Overview

No single MOEPA layer operates in isolation. The most important AI governance capabilities emerge from the **interaction between layers**. This document describes the critical cross-layer compositions that every well-governed AI system should implement.

---

## Composition 1: End-to-End Decision Auditability

**Layers involved:** Metrology + Epistemology + Praxeology + Axiology

**What it achieves:** The ability to reconstruct any decision the system made — who asked for it, what data was used, how confidence was determined, who approved it, and what rules governed it — at any point in the future.

**How the layers interact:**

```
AXIOLOGY    Records which policy version governed this decision
    ↑
PRAXEOLOGY  Records workflow state, human approvals, timestamps
    ↑
EPISTEMOLOGY Records verification results, confidence scores, source citations
    ↑
METROLOGY   Records data provenance, quality status, collection context
    ↑
DATA SUBSTRATE — All records written as immutable entries with cross-references
```

**Government relevance:** When a taxpayer or benefits recipient appeals a decision, or when a Congressional oversight body requests documentation, this composition produces a complete, auditable chain from raw source data through final decision.

**Key capabilities required:**
- M2 (Provenance Recording)
- E1 (Source-Grounded Retrieval)
- E4 (Immutable Decision Audit Log)
- P2 (Human-in-the-Loop Checkpoints)
- P4 (Immutable Workflow Audit Log)
- A1 (Policy-as-Code Enforcement)

---

## Composition 2: High-Confidence Automated Processing with Escalation

**Layers involved:** Metrology + Epistemology + Praxeology

**What it achieves:** Automated processing of high-volume, routine cases with guaranteed escalation for edge cases — achieving operational efficiency without sacrificing accountability.

**How the layers interact:**

```
METROLOGY     → Quality gate: is input data sufficient quality to process?
                  YES → proceed    NO → escalate immediately

EPISTEMOLOGY  → Verification gate: does evidence support a high-confidence answer?
                  HIGH confidence (≥90%) → automated workflow
                  MEDIUM confidence (70–89%) → human review required
                  LOW confidence (<70%) → escalation required

PRAXEOLOGY    → Workflow gate: is the case type within automated processing scope?
                  IN SCOPE → automated workflow with audit logging
                  OUT OF SCOPE → human workflow with audit logging
```

**Government relevance:** Income verification, routine eligibility determinations, and standard compliance checks can be handled at scale. Unusual cases, conflicting evidence, or data quality issues route automatically to human reviewers — no case falls through a gap.

**Key capabilities required:**
- M1 (Data Quality Rules Engine)
- E3 (Confidence Scoring and Uncertainty Communication)
- E2 (Fact Verification Gate)
- P1 (Deterministic Workflow State Machine)
- P2 (Human-in-the-Loop Checkpoints)
- P6 (Escalation and Exception Handling)

---

## Composition 3: Knowledge-Grounded AI Response

**Layers involved:** Ontology + Epistemology + Axiology

**What it achieves:** AI responses that are grounded in owned organizational knowledge, cite specific sources, and are checked against policy constraints before reaching the user.

**How the layers interact:**

```
User Query
    ↓
ONTOLOGY      → Knowledge graph retrieval: find relevant entities and relationships
    ↓
EPISTEMOLOGY  → RAG retrieval: find relevant owned documents and verified facts
                → Confidence scoring: how well-supported is the response?
    ↓
AXIOLOGY      → Policy filter: does the proposed response comply with all constraints?
                  PASS → response delivered with citations and confidence score
                  FAIL → response blocked; violation logged; alternative response generated
    ↓
Response with: citations | confidence score | policy compliance status
```

**Government relevance:** AI-assisted research tools for examiners, analysts, or caseworkers — grounded in agency knowledge, not generic training data, and guaranteed to comply with disclosure and use constraints.

**Key capabilities required:**
- O2 (Knowledge Graph)
- O3 (Embedding and Vector Index)
- E1 (Source-Grounded Retrieval)
- E5 (Hallucination Detection)
- A1 (Policy-as-Code Enforcement)
- A2 (Constitutional Guardrails)

---

## Composition 4: Sovereign AI Intake and Scoring

**Layers involved:** All five layers + Data Substrate

**What it achieves:** A fully owned, governed AI project intake and evaluation process — no vendor dependency at any layer.

**How the layers interact:**

| Layer | Role in Intake Process |
|---|---|
| Metrology | Validates the quality and completeness of proposal submission data |
| Ontology | Resolves entities in the proposal (what systems, what data, what processes) to the agency's canonical model |
| Epistemology | Verifies factual claims in the proposal against owned reference data (budget figures, policy citations) |
| Praxeology | Executes the scoring workflow with defined review stages and human approval gates |
| Axiology | Evaluates proposal alignment with mission priorities and compliance requirements |
| Data Substrate | Records all scores, evidence, approvals, and decisions as a durable governance record |

**Government relevance:** Consistent, auditable AI project evaluation across an agency — enabling leadership to compare proposals, track historical decisions, and demonstrate governance rigor to oversight bodies.

**Key capabilities required:**
- Full 5-Layer scoring per the [Evaluation Checklist](../docs/5-Layer-Evaluation-Checklist.md)
- Data Substrate for persistent governance records
- P1 (Deterministic Workflow State Machine)
- A4 (Mission Alignment Configuration)

---

## Composition 5: Continuous Compliance Monitoring

**Layers involved:** Metrology + Praxeology + Axiology

**What it achieves:** Ongoing assurance that the AI system is operating within approved parameters — detecting drift, policy violations, and anomalies before they become incidents.

**How the layers interact:**

```
METROLOGY     → Continuous data quality monitoring: detect input drift
    ↓             Alert if input distribution changes significantly
PRAXEOLOGY    → Workflow monitoring: detect deviation from approved process
    ↓             Alert if unusual state transitions or escalation rate changes
AXIOLOGY      → Policy compliance monitoring: detect guardrail activation patterns
                  Alert if policy violations increase; trigger investigation
```

**Government relevance:** AI systems cannot be approved once and forgotten. Continuous compliance monitoring provides ongoing assurance to leadership and oversight bodies that the system remains within approved boundaries — without requiring manual audits on a fixed schedule.

**Key capabilities required:**
- M3 (Statistical Profiling and Drift Detection)
- P4 (Immutable Workflow Audit Log)
- A5 (Bias and Equity Monitoring)
- A6 (Value Alignment Testing)

---

## Tool Stack Reference: Cross-Layer Integration

A reference stack for a well-integrated, self-hosted MOEPA implementation:

| Layer | Primary Tool | Integration Point |
|---|---|---|
| Data Substrate | Apache Iceberg + Neo4j | All layers read/write via unified API |
| Metrology | Great Expectations + OpenLineage | Validates data quality before layer 2+ |
| Ontology | Neo4j + Chroma | Graph traversal + vector retrieval |
| Epistemology | LlamaIndex + Guardrails AI | RAG grounded in Ontology; output validated by Axiology |
| Praxeology | LangGraph + Open Policy Agent | State machine execution; OPA enforces Axiology constraints |
| Axiology | OPA + LLM Guard | Policy code enforced across Praxeology; output filtering |
| Observability | OpenTelemetry | Spans across all layers; fed to compliance monitoring |

---

## Related Documents

- [Metrology Capabilities](metrology.md)
- [Ontology Capabilities](ontology.md)
- [Epistemology Capabilities](epistemology.md)
- [Praxeology Capabilities](praxeology.md)
- [Axiology Capabilities](axiology.md)
- [Examples](../examples/) — end-to-end scenario walkthroughs using these compositions
