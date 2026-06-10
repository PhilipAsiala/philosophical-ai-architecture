# Strategic Architecture & Governance
## The MOEPA Cognitive Architecture Framework
Version: 2.3 — Full Ownership & Catalog Focus

Author: Philip Asiala

Last Updated: June 4, 2026

Status: Draft for Review — Feedback Welcome

Related Repositories: philosophical-ai-architecture (GitHub)

## Executive Summary: The Owned-Brain Strategy
Modern enterprise AI strategies frequently fail by treating artificial intelligence as a black-box commodity dropped into existing infrastructure. This approach yields brittle systems, probabilistic hallucination, security vulnerabilities, and vendor lock-in.

The MOEPA Cognitive Architecture (Metrology, Ontology, Epistemology, Praxeology, and Axiology) treats machine cognition with rigorous engineering and philosophical symmetry. By decoupling the architecture, organizations can achieve an Asset-Light, Owned-Brain Strategy:

- Rent the Muscles (Compute): Raw hardware execution (VPC, compute clusters, GPUs) is treated as a highly interchangeable, variable-cost commodity.
- Own the Brain (Intellectual Property): The organizational intelligence—semantic knowledge graphs, cryptographic validation models, ethical guardrails, and mission alignment—is 100% proprietary, portable, and locked down as core intellectual property.

Key Principle: MOEPA is a new cognitive architecture designed for enterprise environments that demand sovereignty, explainability, and measurable governance over AI systems.

## 1. The Owned-Brain Strategy — Core Principles
### 1.1 Why This Matters Now
The rapid proliferation of agentic AI, multimodal models, and open-weight ecosystems creates both unprecedented opportunity and systemic risk. Organizations that fail to establish architectural sovereignty risk:

- Permanent vendor lock-in and escalating OPEX.
- Uncontrolled data exfiltration and compliance violations.
- Inability to audit or explain high-stakes decisions.
- Erosion of institutional knowledge as models drift.

### 1.2 The Decoupling Imperative
MOEPA enforces a clean separation between the computational substrate (rented, interchangeable) and the cognitive substrate (owned, versioned, auditable). This mirrors successful patterns in cloud-native architecture while extending them to the domain of reasoning itself.

Core Principle (v2.3): We rent commodity compute. We own the brain. Ownership means internal control of data (Metrology), semantics (Ontology), validation (Epistemology), workflows (Praxeology), and values (Axiology), supported by a unified catalog for discoverability.

## 2. MOEPA Layer Definitions — Philosophical Grounding & Practical Translation
Each layer is named after a classical philosophical discipline and grounded in a specific mathematical formalization. This ensures the framework is both intellectually coherent and technically implementable.

### Layer 1 — Metrology (Science of Measurement) — The Data Foundation Layer
Philosophical Definition: The study of measurement, standards, and the conditions under which reliable observation is possible.

Mathematical Grounding: Measure theory, statistics, calibration theory, and boundary conditions.

Enterprise Translation: Establishing the foundational data layer—ensuring all data is measured, quality-assured, observable, and traceable before it enters higher cognitive layers. This is the bedrock that prevents "garbage in, garbage out" across the entire architecture.

Key Artifacts:

- Self-hosted open-format data substrate containers (Iceberg, Parquet) that Metrology qualifies through ingress quality controls (see §5.1).
- Internal data quality frameworks (Great Expectations, Monte Carlo, or custom).
- Comprehensive quality gates plus observational lineage/provenance over what enters the substrate.
- Observability for drift, anomaly detection, and statistical profiling.
- Encrypted, air-gappable datasets with strict egress controls.

Explicitly avoid: Architectures where third-party platforms own the data foundation, quality rules, and lineage through proprietary catalogs.

### Layer 2 — Ontology (Study of Being / Reality)
Philosophical Definition: The study of what exists, the categories of being, and the relationships between entities.

Mathematical Grounding: Graph theory, formal ontologies, description logics.

Enterprise Translation: Modeling domain reality as structured, queryable knowledge rather than flat text.

Key Artifacts:

- Internally managed knowledge graphs (Neo4j, Amazon Neptune).
- Custom entity resolution, embedding pipelines, and schema management.
- Version-controlled semantic models.

Explicitly avoid: External platforms that own the core semantic model and entity truth layer.

### Layer 3 — Epistemology (Study of Knowledge & Truth)
Philosophical Definition: The study of how we know what we know, justification, and the distinction between belief and justified true belief.

Mathematical Grounding: Formal logic, probability theory, Bayesian inference, cryptographic verification.

Enterprise Translation: Separating probabilistic model output from verified facts; building chains of custody for information.

Key Artifacts:

- SHA-256 validation pipelines in CI/CD.
- RAG with source citation + grounding checks against owned data.
- Automated vulnerability scanning.
- Deterministic fact-verification gates before any execution.

### Layer 4 — Praxeology (Study of Purposeful Action)
Philosophical Definition: The study of human action, intentionality, and the logical structure of goal-directed behavior.

Mathematical Grounding: Game theory, decision theory, planning algorithms, workflow formalisms.

Enterprise Translation: Governing how agents act—what tools they may call, in what sequence, and under what human oversight.

Key Artifacts:

- Deterministic slash-command workflows (/jira-epic → /plan → /execute).
- LangGraph state machines.
- Mandatory human-in-the-loop checkpoints.
- Immutable audit trails at every milestone.

### Layer 5 — Axiology (Study of Value & Ethics)
Philosophical Definition: The study of value, worth, and ethical principles—what ought to be preserved or optimized.

Mathematical Grounding: Optimization theory, multi-objective decision making, constitutional AI approaches.

Enterprise Translation: Hard-coding organizational values, regulatory constraints, and mission alignment so they cannot be easily overridden.

Key Artifacts:

- "Golden Master" config.yaml with OS-level write locks (icacls / Windows ACLs).
- Preferred/forbidden verb enforcement (allowed vs. prohibited agent actions).
- Zero Trust policy blocks.
- Constitutional guardrails that survive prompt injection.

## 3. The MOEPA Stack Specification
The five layers are interdependent. Weakness in any layer undermines the integrity of the whole system. Layers are numbered bottom-up (1 = foundation, 5 = highest governance). All layers must score ≥3 to avoid an automatic NO-GO; an unconditional GO requires every layer to score ≥4, and a layer at exactly 3 yields a CONDITIONAL GO.

### Strategic Evaluation Matrix

| Layer | The Econometric & Risk Lens (Program Evaluation / RAS) | The Systems Engineering & Zero Trust Lens (IT Enterprise Services) |
| --- | --- | --- |
| 5. Axiology | Minimizes compliance costs and legal liabilities by hardcoding mandatory operational boundaries. | Enforces policy-as-code at the OS/Infrastructure level, eliminating client-side manipulation. |
| 4. Praxeology | Lowers operational risk by replacing erratic manual loops with highly predictable, auditable processes. | Implements deterministic state-machines and strict slash-command agentic boundaries. |
| 3. Epistemology | Protects the statistical validity of decision models by preventing data pollution and hallucinations. | Deploys cryptographic SHA-256 validation pipelines and automated CI/CD security gates. |
| 2. Ontology | Models complex corporate relational networks (e.g., entity ownership and dependency tracking) into clean, queryable realities. | Generates abstract syntax trees, semantic knowledge graphs, and local context embedding indices. |
| 1. Metrology | Establishes baseline data integrity, ensuring that econometric profiling relies on uncorrupted metrics. | Restricts compute to quantized open-weight models inside secure, zero-egress VPCs. |

## 4. MOEPA Intake & Scoring Framework
### 4.1 Purpose
Every AI procurement request, vendor pitch, internal use-case, or model deployment must be audited against the five MOEPA layers before funding or infrastructure provisioning is approved.

### 4.2 Scoring Rubric (1–5 Scale)
Decision Bands: Each layer is scored 1–5, and the lowest layer score sets the overall recommendation.

- NO-GO: any layer scores 1 or 2 (automatic NO-GO with required remediation).
- CONDITIONAL GO: every layer scores ≥3 and at least one layer scores exactly 3 — approved only if that layer's named controls and oversight are demonstrably active.
- GO: every layer scores ≥4.

Minimum Threshold: A score of 3 is the minimum acceptable standard for a layer and does not trigger a NO-GO, but a project is not an unconditional GO until every layer scores ≥4.

Score Definitions:

- 1: Completely Missing or Free-Form Prompt Dependent — High Risk
- 2: Partial / Ad-Hoc Controls — Elevated Risk
- 3: Defined & Contained — Minimum Acceptable Standard (Conditional)
- 4: Strongly Enforced & Measurable — Good Practice
- 5: Immutable / Cryptographically Proven & Fully Decoupled — Gold Standard

### 4.3 Layer-by-Layer Evaluation Criteria
#### Layer 1 — Metrology Evaluation (Data Foundation)
Risk: Poor data quality, uncontrolled lineage, vendor lock-in on the data layer, loss of sovereignty over organizational truth.

Audit Question: How is data quality measured, assured, and made observable? Is the data foundation internally controlled or owned by an outside vendor?

Scoring Guidance:

- Score 1: No data quality measurement; complete reliance on vendor-managed proprietary data platforms.
- Score 3: Basic internal data quality rules and lineage tracking exist within standard data lakes.
- Score 5: Comprehensive internal data observability, statistical profiling, provenance tracking, and self-hosted open-format data lake with full sovereignty.

#### Layer 2 — Ontology Evaluation (Structured Reality)
Risk: Context collapse, poor reasoning quality, inability to maintain consistent world model.

Audit Question: How does the system represent and maintain structured knowledge of your domain? Is the semantic model internally owned or controlled by an outside vendor?

Scoring Guidance:

- Score 1: Raw pre-trained weights only; no domain structuring or custom schema constraints.
- Score 3: Standardized external schemas or flat vector indexes with isolated metadata.
- Score 5: Live, internally managed semantic knowledge graph + AST-level understanding that evolves with your codebase and business rules.

#### Layer 3 — Epistemology Evaluation (Truth & Verification)
Risk: Hallucination amplification, unverified code execution, lack of operational traceability, and blind reliance on probabilistic outputs.

Audit Question: How does the system differentiate between a statistically generated guess and an immutable, verified enterprise fact? Are validation gates centralized or hidden inside a vendor's black-box pipeline?

Scoring Guidance:

- Score 1: Prompt-dependent validation only; model outputs are served directly to users or APIs with zero deterministic cross-checking.
- Score 3: Basic automated checks exist (e.g., local code linters or flat retrieval checks). Retrieval-Augmented Generation (RAG) surfaces source citations, but lacks cryptographic pipeline validation.
- Score 5: Advanced cryptographic verification is standard. Pipeline integration validates model configurations using SHA-256 hashes before code execution. Every fact is verified against your sovereign, owned Metrology asset, and verification metadata is continuously indexed in the MOEPA Catalog.

#### Layer 4 — Praxeology Evaluation (Agentic Workflow Boundaries)
Risk: Uncontrolled agentic loops, destructive autonomous API actions, and untraceable multi-step execution paths.

Audit Question: What deterministic framework governs the sequence of execution when an AI calls a tool or generates a system artifact? How is human oversight structurally guaranteed?

Scoring Guidance:

- Score 1: Free-form, autonomous execution loops with zero state-machine tracking; tools are exposed to the LLM via open-ended prompts.
- Score 3: Agentic logic is bounded by basic sequential code, but lacks a centralized state machine. Human-in-the-loop checkpoints exist but are bypassable.
- Score 5: The workflow is driven by immutable, deterministic state machines (e.g., LangGraph). Execution follows strict, auditable lifecycles (/jira-epic → /plan → /execute) generating permanent audit trails. State parameters are discoverable and versioned inside the MOEPA Catalog.

#### Layer 5 — Axiology Evaluation (Governance & Value Alignment)
Risk: Prompt injection vulnerabilities, alignment drift, and client-side manipulation of organizational guardrails by developers or end-users.

Audit Question: How are the ethical boundaries, compliance mandates, and organizational value guardrails permanently locked down against intentional or accidental modification?

Scoring Guidance:

- Score 1: Soft constraints only; guidelines are embedded within the system prompt and easily bypassed by sophisticated prompt injections.
- Score 3: Compliance rules are centralized, but security configuration settings are modifiable by local client environments or developers at the edge.
- Score 5: Core organizational values, preferred/forbidden verb lists, and security policies are hardcoded into a "Golden Master" configuration file locked via OS-level write constraints (Windows ACLs/icacls or immutable infrastructure policies). Policy code is cryptographically protected and cataloged.

## 5. MOEPA Catalog Architecture (Cross-Cutting Section)
The MOEPA Catalog is the practical mechanism for owning the brain. It provides discoverability, versioning, governance, and access control across all five layers.

Catalog Implementation Reference: See the layer-by-layer catalog in [catalog/README.md](catalog/README.md) for concrete capabilities, tools, patterns, scoring, and example assets across Metrology, Ontology, Epistemology, Praxeology, and Axiology.

Core Capabilities:

- Semantic and keyword search across data, models, graphs, prompts, workflows, and policies.
- Full versioning, lineage, and deprecation tracking.
- Approval workflow integration tied to the Intake Scoring process.
- Usage analytics and ownership metadata.
- Role-based access aligned with Layer 5 (Axiology).

Implementation Guidance: Utilize DataHub or a custom-engineered enterprise portal backed by an internally managed Neo4j instance. The catalog must interface directly with internal GitOps and CI/CD pipelines to ensure that whenever an asset's hash or schema changes, the catalog's state updates automatically. This provides an inspection-ready, auditable inventory of the entire corporate cognitive footprint.

### 5.1 The MOEPA Data Substrate (Set-Theoretic Backbone)
Set Theory in MOEPA is the representation medium, not a sixth scored layer. The five classical disciplines remain the five scored layers (Metrology, Ontology, Epistemology, Praxeology, Axiology), and the 1–5 per-layer scoring model remains unchanged.

The substrate provides a single SPO/quad backbone (Subject-Predicate-Object, quads with context) plus lakehouse storage where the base triple lives once. Each MOEPA layer attaches layer-specific metadata envelopes (epistemic, praxeological, axiological, etc.) without duplicating the base fact.

```json
{
  "triple": {"s": "IncomeVerification:TX12345", "p": "hasAmount", "o": 85000},
  "epistemic_metadata": {"confidence": 0.98, "justification": "ThirdPartyStudy_2025_n=125000", "status": "HighReliability"}
}
```

A federation layer (for example, LangGraph routing or Trino) supports cross-layer queries such as: "find all high-confidence income facts that satisfy axiological fairness and support praxeological auto-approval."

This substrate scales from lightweight edge deployments (JSON triples + SQLite) to enterprise deployments (full graph + Iceberg). It is sovereignty-aligned with the Owned-Brain strategy: self-hosted graph control, open formats, PROV-O lineage compatibility, and one owned base triple that remains queryable as a single auditable whole.

Decisive trust-vs-form test: "Does the property describe how trustworthy/observed a value is (→ Metrology), or what formal shape and storage it has (→ Set Theory)?"

| Dimension | Metrology (Trust of Measurement) | Set Theory / Data Substrate (Form & Storage) |
| :--- | :--- | :--- |
| Core question | Can we trust this observation? | What formal shape does this fact take and where is it stored? |
| Mathematical grounding | Measure theory, statistics, calibration theory, boundary conditions | Set theory, relations/functions/tuples, tensor algebra, graph triple/quad structures |
| Owns | Units, standards, calibration, error bounds, quality gates, observational lineage, observability/drift controls | Sets/multisets, relations, tensors, SPO/quad backbone, Iceberg/Parquet containers, storage layout |
| Does **not** own | Container formats, triple/quad structural model, physical lakehouse encoding | Measurement trust policies, calibration rules, quality thresholds, observational reliability controls |
| Lifecycle stage | Data entering the system (quality and trust qualification) | Data at rest and query form (representation and storage) |
| One-word summary | Adjectives of trust | Nouns |

Worked example (income = 85000):
- Metrology owns the trust envelope: unit = USD, source = `ThirdPartyStudy_2025`, n = 125000, quality checks passed, drift status, observational lineage.
- Set Theory / Data Substrate owns the form envelope: element of set `IncomeObservations`; object of triple `(IncomeVerification:TX12345, hasAmount, 85000)`; `int64` Parquet column; aggregable into a distribution object.

Provenance three-way split (to avoid double-claiming):
- Set Theory / Data Substrate: structural lineage (for example, this tensor came from that table via this join).
- Metrology: observational provenance (who measured it, against what standard, with what error bounds).
- Epistemology: justificatory provenance (confidence, warrant, and belief revision over claims).

## 6. Implementation Playbook
### 6.1 Recommended Technology Stack by Layer (Ownership-Focused)
- Metrology (Data Foundation): Self-hosted data lakes (MinIO + Iceberg), Great Expectations or Monte Carlo for quality, DataHub for catalog — avoiding external repository/catalog ownership.
- Ontology: Neo4j or Amazon Neptune (self-managed), internal schema governance.
- Epistemology: Self-hosted RAG (PGVector/Chroma) + Guardrails AI + cryptographic validation in CI/CD.
- Praxeology: Self-hosted LangGraph or CrewAI with human-in-the-loop approval queues.
- Axiology: OPA/Gatekeeper for policy-as-code, OS-level write locks on Golden Master configs.

### 6.2 Quick-Start Checklist for New Projects
- Define Metrology boundary and data quality baseline (internal control, not vendor-owned).
- Create or extend domain ontology / knowledge graph schema (internal ownership).
- Implement RAG with citation + grounding verification pipeline against owned data.
- Design deterministic workflow (LangGraph state machine or slash-command sequence).
- Create Golden Master config.yaml and apply OS-level write locks.
- Register all assets in the MOEPA Catalog.
- Map all five layers to the MOEPA scorecard and obtain review board sign-off.

## 7. Success Metrics & Key Performance Indicators
### Governance Health
- % of AI projects that pass initial MOEPA intake on first submission (target: >70%).
- Average time from intake submission to GO/NO-GO decision (target: <5 business days).

### Risk Reduction
- Reduction in vendor-owned layer dependencies (target: significant reduction in external vendor control of Metrology/Ontology layers).
- Reduction in security findings related to AI systems.
- Mean time to detect policy drift or configuration bypass.

### Operational Excellence
- Infrastructure cost predictability.
- Model performance consistency before vs. after MOEPA controls.
- Developer velocity on approved patterns.

## 8. Alignment with Industry Standards & Frameworks
MOEPA is designed to be complementary to major AI governance frameworks:

- NIST AI RMF 1.0
- ISO/IEC 42001:2023
- MITRE ATLAS
- OWASP LLM Top 10
- Executive Order 14110 (Safe AI)

## 9. Governance of the MOEPA Framework Itself
The practices below describe how an organization adopting MOEPA should govern its own instance of the framework. To propose changes to this repository itself, see [CONTRIBUTING.md](CONTRIBUTING.md).

- Semantic versioning (MAJOR.MINOR.PATCH).
- Quarterly review by Architecture Review Board.
- Time-boxed exception process for high-value innovation pilots.
- Open internal RFC process for proposed changes.

## Appendix A: Sample Scoring for Common AI Tools
Illustrative only — actual scores depend on specific implementation details.

### ChatGPT Enterprise (Default)
Metrology: 2 | Ontology: 1 | Epistemology: 2 | Praxeology: 2 | Axiology: 2

High vendor dependency on data and semantic layers.

### Claude (Default, no custom guardrails)
Metrology: 2 | Ontology: 2 | Epistemology: 3 | Praxeology: 2 | Axiology: 3

### Local Llama 3.1 70B + Guardrails AI + LangGraph + Internal Catalog
Metrology: 5 | Ontology: 5 | Epistemology: 5 | Praxeology: 5 | Axiology: 5

Full internal ownership across layers + Catalog discoverability.

### RAG over internal knowledge graph + deterministic workflow + self-hosted data lake
Metrology: 5 | Ontology: 5 | Epistemology: 5 | Praxeology: 5 | Axiology: 4

### Typical Vendor Agentic SaaS Platform
Metrology: 2 | Ontology: 2 | Epistemology: 2 | Praxeology: 3 | Axiology: 2

Significant lock-in on foundational layers.
