# Philosophical AI Architecture — Technical Specification
## The MOEPA Cognitive Architecture
Version: 2.4 — Dual-Domain Control (Probabilistic Proposal, Deterministic Arbiter)

Author: Philip Asiala

Last Updated: October 2, 2026

Status: Draft for Review — Feedback Welcome

Repository: [philosophical-ai-architecture](https://github.com/PhilipAsiala/philosophical-ai-architecture) (GitHub) — canonical home of the Philosophical AI Architecture

> **Naming.** This document specifies the **MOEPA Cognitive Architecture** — the technical stack design within the **Philosophical AI Architecture**. For the engineering blueprint and intake scoring, see the **MOEPA 5-Layer Framework** in [docs/](docs/). For pitching and narrative alignment, see [pitch strategy](docs/pitch-strategy.md). Term definitions: [glossary](docs/glossary.md).

## Executive Summary: The Owned-Brain Strategy
The industry obsesses over the Artificial — compute, LLMs, infrastructure — and treats Intelligence as a black box. The Philosophical AI Architecture opens that box by mapping human cognitive functions (Cognition, Affect, Conation) into strict, governable software.

The MOEPA Cognitive Architecture (Metrology, Ontology, Epistemology, Praxeology, and Axiology) implements this with rigorous engineering and philosophical symmetry. Organizations achieve an Asset-Light, Owned-Brain Strategy:

- Rent the Muscles (Compute): Raw hardware execution (VPC, compute clusters, GPUs) is treated as a highly interchangeable, variable-cost commodity.
- Own the Brain (Intellectual Property): The organizational intelligence—semantic knowledge graphs, cryptographic validation models, ethical guardrails, and mission alignment—is 100% proprietary, portable, and locked down as core intellectual property.

Key Principle: The MOEPA Cognitive Architecture is the technical implementation layer of the Philosophical AI Architecture — built for enterprise environments that demand sovereignty, explainability, and measurable governance over AI systems.

## 1. The Owned-Brain Strategy — Core Principles
### 1.1 Why This Matters Now
The rapid proliferation of agentic AI, multimodal models, and open-weight ecosystems creates both unprecedented opportunity and systemic risk. Organizations that fail to establish architectural sovereignty risk:

- Permanent vendor lock-in and escalating OPEX.
- Uncontrolled data exfiltration and compliance violations.
- Inability to audit or explain high-stakes decisions.
- Erosion of institutional knowledge as models drift.

### 1.2 The Decoupling Imperative
MOEPA enforces a clean separation between the computational substrate (rented, interchangeable) and the cognitive substrate (owned, versioned, auditable). This mirrors successful patterns in cloud-native architecture while extending them to the domain of reasoning itself.

Core Principle (v2.4): We rent commodity compute. We own the brain. Ownership means internal control of measurement (Metrology), semantics (Ontology), inference (Epistemology), action (Praxeology), and values (Axiology), supported by a unified catalog for discoverability. Runtime control splits those layers into a probabilistic domain that may propose and a deterministic domain that alone may commit.

### 1.3 The Dual-Domain Partition
Every component, data model, and agent workflow belongs to one operational domain. The domains do not share a permission type.

| Domain | Layers | What it may do | What it may not do |
| --- | --- | --- | --- |
| **Probabilistic** ("Quantum" / statistical inference) | Metrology, Epistemology | Measure, score, calibrate, integrate noisy evidence, generate hypotheses, interpret meaning | Commit an entity, authorize an action, or emit a permission |
| **Deterministic** ("Newtonian" / discrete governance) | Ontology, Praxeology, Axiology | Commit categorical state, admit or reject a transition, issue a final verdict | Store uncertainty on an entity, or turn a probability into a permission |

**Probabilistic domain**

- **Metrology** carries continuous telemetry: confidence scoring, calibration, error bounds, and empirical disagreement. A measurement can be uncertain. That uncertainty is a property of the observation, not of an entity's existence.
- **Epistemology** is the inference engine (LLMs and other statistical models). It integrates noisy evidence, updates partial beliefs, generates hypotheses, and interprets semantics. It must emit three distinct states:
  - **Belief** — a partial claim with a confidence, a justification, and any attached error bounds.
  - **Defeater** — a specific reason the belief cannot stand. A defeater is not a lower probability of the same claim.
  - **Ignorance** ("I don't know") — the engine has no warranted claim. Ignorance is not a flat or uniform distribution over the answer set.

**Deterministic domain**

- **Ontology** commits discrete entities and categorical state (RDF subject-predicate-object triples, Apache Iceberg rows, and equivalent schemas). A triple is written or it is not. Epistemic confidence attaches only to the epistemic envelope. It is never a column, predicate, or existence condition on the entity schema. This is the **epistemic firewall**: uncertainty stays on claims.
- **Praxeology** validates the action space. It decides whether a proposed transition is procedurally and physically viable under the current state machine. Viability is a discrete precondition, not a confidence band.
- **Axiology is the final arbiter of systemic commitment.** It returns exactly one of three permissions: **Commit**, **Forbid**, or **Refuse to Act**. It does not return a probability, a score, or a confidence that something is allowed. **Refuse to Act** is the correct verdict when the proposal is Ignorance or carries an unresolved defeater. **Forbid** is the correct verdict when the act is in the action space but violates a value, safety, or compliance rule. **Commit** is the only verdict that authorizes a write or an external effect.

### 1.4 Control Flow: Probabilistic Proposal → Deterministic Arbiter
No layer in the probabilistic domain may write a committed fact or execute an action. The handoff is one-way until Axiology returns a verdict.

1. **Measure (Metrology).** Qualify the observation: value, unit, calibration, error bounds, and any empirical disagreement. Persist the observation as measurement, not as an ontological commitment.
2. **Propose (Epistemology).** Integrate the qualified evidence into one proposal whose epistemic state is Belief, Defeater, or Ignorance. Attach citations and confidence only inside the epistemic envelope. If the warranted output is Ignorance or a defeater, say so. Do not coerce that state into a low probability and continue.
3. **Shape (Ontology).** Accept a candidate categorical state only when it matches a discrete schema. Reject any write that would place confidence, probability, or "maybe" onto the entity. The candidate remains uncommitted until step 5.
4. **Admit (Praxeology).** Test the candidate transition against the action space: current state, allowed verbs, procedural preconditions, and required human checkpoints. A failed admission stops the flow. It does not lower a confidence score.
5. **Arbitrate (Axiology).** Issue **Commit**, **Forbid**, or **Refuse to Act**.
   - **Commit** writes the ontological triple (or equivalent row) and authorizes the admitted action. The epistemic envelope is stored beside the triple, never inside it.
   - **Forbid** blocks the action and records the violated rule. No entity is committed for that act.
   - **Refuse to Act** commits nothing and executes nothing. The ignorance or defeater is preserved so a later proposal can revise the belief without pretending a decision was made.

Orchestrators may call Metrology and Epistemology to form a proposal. They may not treat the model's token probabilities, a RAG score, or a calibrated confidence as authorization. Tool execution that changes state is reachable only after an axiological **Commit**.

## 2. MOEPA Layer Definitions — Philosophical Grounding & Practical Translation
Each layer is named after a classical philosophical discipline and grounded in a specific mathematical formalization. This ensures the framework is both intellectually coherent and technically implementable.

### Layer 1 — Metrology (Science of Measurement) — The Data Foundation Layer
**Domain:** Probabilistic.

Philosophical Definition: The study of measurement, standards, and the conditions under which reliable observation is possible.

Mathematical Grounding: Measure theory, statistics, calibration theory, and boundary conditions.

Enterprise Translation: Continuous telemetry over observations — quality, calibration, error bounds, and disagreement — before any deterministic layer is asked to commit. Metrology never promotes a measurement into an entity.

Key Artifacts:

- Self-hosted open-format data substrate containers (Iceberg, Parquet) that Metrology qualifies through ingress quality controls (see §5.1).
- Internal data quality frameworks (Great Expectations, Monte Carlo, or custom).
- Comprehensive quality gates plus observational lineage/provenance over what enters the substrate.
- Observability for drift, anomaly detection, and statistical profiling.
- Encrypted, air-gappable datasets with strict egress controls.

Explicitly avoid: Architectures where third-party platforms own the data foundation, quality rules, and lineage through proprietary catalogs.

### Layer 2 — Ontology (Study of Being / Reality)
**Domain:** Deterministic.

Philosophical Definition: The study of what exists, the categories of being, and the relationships between entities.

Mathematical Grounding: Graph theory, formal ontologies, description logics. Existence in the schema is categorical.

Enterprise Translation: Discrete entity commitment. Reality is stored as subject-predicate-object triples, Iceberg rows, or an equivalent closed schema. Uncertainty is forbidden on the entity. A record that is "probably an applicant" is an epistemic proposal, not an ontological individual.

Key Artifacts:

- Internally managed knowledge graphs (Neo4j, Amazon Neptune).
- Custom entity resolution, embedding pipelines, and schema management.
- Version-controlled semantic models.

Explicitly avoid: External platforms that own the core semantic model and entity truth layer.

### Layer 3 — Epistemology (Study of Knowledge & Truth)
**Domain:** Probabilistic.

Philosophical Definition: The study of how we know what we know, justification, and the distinction between belief, defeated belief, and ignorance.

Mathematical Grounding: Probability theory, Bayesian updating, and argumentation. Ignorance and defeaters are first-class states, not residual probability mass.

Enterprise Translation: The inference engine. LLMs and other statistical models integrate noisy evidence, update partial beliefs, generate hypotheses, and interpret semantics. They propose. They do not commit. A proposal that cannot be warranted is returned as Ignorance or as a named defeater, with citations, rather than as a confident guess.

Key Artifacts:

- Foundation-model or other statistical inference, bounded by owned evidence.
- RAG with source citation, used as input to a proposal, not as authorization.
- Explicit epistemic states: Belief, Defeater, Ignorance.
- Calibration of reported confidence against Metrology error bounds.
- Chains of justificatory custody stored in the epistemic envelope.

### Layer 4 — Praxeology (Study of Purposeful Action)
**Domain:** Deterministic.

Philosophical Definition: The study of human action, intentionality, and the logical structure of goal-directed behavior.

Mathematical Grounding: State machines, precondition/effect rules, and workflow formalisms. Admission is boolean.

Enterprise Translation: Action-space validation. A transition is viable or it is not, given the current categorical state, the allowed verbs, and the procedural rules (including mandatory human checkpoints). Confidence bands are not routing rules. A human checkpoint is a discrete precondition, not a response to a probability falling below a cutoff.

Key Artifacts:

- Deterministic workflow lifecycles (intake → plan → execute).
- LangGraph state machines.
- Mandatory human-in-the-loop checkpoints.
- Immutable audit trails at every milestone.

### Layer 5 — Axiology (Study of Value & Ethics)
**Domain:** Deterministic. Final arbiter of systemic commitment.

Philosophical Definition: The study of value, worth, and ethical principles—what ought to be preserved or refused.

Mathematical Grounding: Deontic policy. The permission set is finite and discrete: Commit, Forbid, Refuse to Act. Utility models may inform how a rule was written; they are not the runtime verdict.

Enterprise Translation: Hard-coded organizational values, safety bounds, and compliance rules. Axiology is the only layer that may authorize a committed write or an external effect. Prompt-level guidance is not a verdict.

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
| 5. Axiology | Minimizes compliance cost by making Commit, Forbid, and Refuse to Act explicit and auditable. | Final arbiter. Policy-as-code returns a binary permission, never a probability of being allowed. |
| 4. Praxeology | Lowers operational risk by admitting only transitions that the action space already allows. | Discrete state machines and procedural preconditions. Confidence is not an admission rule. |
| 3. Epistemology | Keeps statistical inference honest by separating Belief, Defeater, and Ignorance. | Proposes claims with citations and calibrated confidence. Does not authorize execution. |
| 2. Ontology | Models mission-domain networks as categorical entities and relations. | RDF triples, Iceberg tables, and equivalent schemas. Epistemic confidence cannot appear on the entity. |
| 1. Metrology | Establishes whether an observation is calibrated, bounded, and in disagreement with other measurements. | Continuous telemetry, error bounds, and drift. Measurements are not commitments. |

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
Risk: Context collapse, poor reasoning quality, and leakage of epistemic uncertainty into entity existence.

Audit Question: How does the system represent and maintain structured knowledge of your domain? Is existence categorical, with confidence confined to the epistemic envelope? Is the semantic model internally owned?

Scoring Guidance:

- Score 1: Raw pre-trained weights only; entity "existence" is a model score, or confidence is stored on the entity schema.
- Score 3: Standardized external schemas or flat vector indexes with isolated metadata. Commitment and confidence are separable in documentation but not enforced by schema.
- Score 5: Live, internally managed semantic knowledge graph. Writes are categorical. A schema check rejects any attempt to store probability, confidence, or "maybe" as a property of existence.

#### Layer 3 — Epistemology Evaluation (Inference & Warrant)
Risk: Hallucination presented as knowledge, ignorance flattened into a probability, and model output treated as authorization.

Audit Question: Does the inference layer emit Belief, Defeater, and Ignorance as distinct states, with citations and calibrated confidence inside the epistemic envelope? Is that proposal forbidden from authorizing action on its own?

Scoring Guidance:

- Score 1: The model answers every prompt. "I don't know" is a low score or a hedged sentence. Outputs are served directly to users or APIs.
- Score 3: Retrieval cites sources and a confidence is reported, but Ignorance and defeaters are still coerced into a probability, and a high score can unlock an automated path.
- Score 5: Belief, Defeater, and Ignorance are distinct, logged states. Confidence is calibrated against Metrology bounds and stored only in the epistemic envelope. No confidence value, RAG score, or token probability can commit an entity or execute a tool. The proposal is handed to Ontology, Praxeology, and Axiology.

#### Layer 4 — Praxeology Evaluation (Agentic Workflow Boundaries)
Risk: Uncontrolled agentic loops, destructive autonomous API actions, and untraceable multi-step execution paths.

Audit Question: Which discrete preconditions define the action space? Can a confidence threshold admit or reject a transition, or is admission a boolean function of state, verb, and procedure?

Scoring Guidance:

- Score 1: Free-form, autonomous execution loops; tools are exposed to the LLM, and a probability is treated as permission to act.
- Score 3: Sequential workflow exists, but human checkpoints are bypassable, or routing is still "act if confidence ≥ N."
- Score 5: Immutable state machines. A transition is admitted only when every procedural precondition holds, including required human checkpoints. Confidence may be recorded on the proposal; it is not an edge in the state machine. State parameters are versioned in the MOEPA Catalog. Execution still waits for an axiological Commit.

#### Layer 5 — Axiology Evaluation (Governance & Value Alignment)
Risk: Prompt injection vulnerabilities, alignment drift, and client-side manipulation of organizational guardrails by developers or end-users.

Audit Question: Does Axiology return only Commit, Forbid, or Refuse to Act, and is that verdict the sole authorization for systemic commitment? Can a probability, prompt, or client setting override it?

**Enterprise-Scale Weighting (for 1,000+ use-case intake environments):** In high-volume federal and enterprise intake processes, Axiology scores are weighted heavily by two factors: (1) documented **Business ROI** (quantified mission impact, risk reduction, cost avoidance, equity improvements, or throughput gains with traceable assumptions and sensitivity analysis) and (2) the presence of a formal, auditable **Chargeback/Showback model** that attributes platform, compute, data, and governance costs back to business owners. Proposals lacking credible ROI quantification or a viable cost attribution model cannot achieve a score of 4 or higher regardless of other governance controls.

Scoring Guidance:

- Score 1: Soft constraints only. Guidelines live in the system prompt, or "allowed" is a probability the model emits.
- Score 3: Compliance rules are centralized, but they can be modified at the edge, or a high epistemic confidence can still count as permission.
- Score 5: Values, safety bounds, and preferred/forbidden verbs are hardcoded in a Golden Master locked by OS-level or immutable-infrastructure controls. The runtime verdict is exactly one of Commit, Forbid, or Refuse to Act. Refuse to Act is mandatory for Ignorance and unresolved defeaters. Policy code is cryptographically protected and cataloged. A quantified Business ROI model and an approved chargeback/showback mechanism are reviewed at the executive level. Neither ROI nor confidence can replace the verdict.

### 4.4 Executive Governance & Architecture Review Chain

To support enterprise-scale intake (1,000+ requests) while maintaining sovereignty and preventing uncontrolled proliferation, MOEPA mandates a formal executive governance gate and a strict Architecture Review Chain for all proposals.

**Executive Approval Gate:** Any use case that receives an overall MOEPA score of 4 or higher (or any proposal requesting production funding or enterprise platform resources) must pass an explicit executive-level approval gate before scaling. This gate is separate from technical scoring and is triggered by the weighted Axiology score (incorporating Business ROI and chargeback justification). The executive gate reviews mission alignment, quantified ROI, cost attribution model, demand management clearance (no duplication), and residual risk.

**Mandatory Architecture Review Chain:** Before executive sign-off, every proposal must traverse the following strict, sequential review chain. Each step must provide documented sign-off; no step may be bypassed. Role titles are illustrative — agencies map each step to their own governance bodies (architecture review board, data platform office, mission program office, etc.):

1. **Enterprise Architecture Review** — Initial technical architecture review for alignment with agency standards, security patterns, and MOEPA layer controls.
2. **Agency Data Platform — ingestion and lineage review** — Data platform engineering validates ingestion approach, lineage, and quality controls (see Metrology data availability requirements).
3. **Agency Data Platform — capacity and cost review** — Platform owners confirm capacity, cost model integration, and platform-level governance.
4. **Mission program office** — Owning program confirms operational readiness, ROI assumptions, and acceptance of chargeback/showback obligations.
5. **Executive Sign-off** — Formal approval by designated executive authority (or governance board) confirming the weighted ROI case, approved cost model, demand management clearance via the MOEPA Catalog, and completion of the preceding chain.

This chain ensures that technical feasibility, data reality, platform economics, business ownership, and executive accountability are all explicitly addressed. The MOEPA Catalog serves as the authoritative record of prior decisions to support deduplication at step 1 and throughout the chain.

## 5. MOEPA Catalog Architecture (Cross-Cutting Section)
The MOEPA Catalog is the practical mechanism for owning the brain. It provides discoverability, versioning, governance, and access control across all five layers.

Catalog Implementation Reference: See the layer-by-layer catalog in [catalog/README.md](catalog/README.md) for concrete capabilities, tools, patterns, scoring, and example assets across Metrology, Ontology, Epistemology, Praxeology, and Axiology.

Core Capabilities:

- Semantic and keyword search across data, models, graphs, prompts, workflows, and policies.
- Full versioning, lineage, and deprecation tracking.
- Approval workflow integration tied to the Intake Scoring process.
- Usage analytics and ownership metadata.
- Role-based access aligned with Layer 5 (Axiology).

Implementation Guidance: Utilize DataHub or a custom-engineered enterprise portal backed by an internally managed Neo4j instance. The catalog must interface directly with internal GitOps and CI/CD pipelines to ensure that whenever an asset's hash or schema changes, the catalog's state updates automatically. This provides an inspection-ready, auditable inventory of the entire agency cognitive footprint.

### 5.1 The MOEPA Data Substrate (Set-Theoretic Backbone)
Set Theory in MOEPA is the representation medium, not a sixth scored layer. The five classical disciplines remain the five scored layers (Metrology, Ontology, Epistemology, Praxeology, Axiology), and the 1–5 per-layer scoring model remains unchanged.

The substrate provides a single SPO/quad backbone (Subject-Predicate-Object, quads with context) plus lakehouse storage where the base triple lives once. Each MOEPA layer attaches layer-specific metadata envelopes (epistemic, praxeological, axiological, etc.) without duplicating the base fact. The triple is written only after an axiological **Commit**. Confidence never appears inside the triple.

```json
{
  "triple": {"s": "IncomeVerification:TX12345", "p": "hasAmount", "o": 85000},
  "epistemic_metadata": {
    "state": "belief",
    "confidence": 0.98,
    "justification": "ThirdPartyStudy_2025_n=125000",
    "defeaters": []
  },
  "praxeological_metadata": {"transition": "record_verified_amount", "admitted": true},
  "axiological_metadata": {"verdict": "commit", "rule": "routine_income_record_v3"}
}
```

A proposal that cannot be warranted does not produce a triple:

```json
{
  "proposal_id": "IncomeVerification:TX12345:unearned",
  "epistemic_metadata": {"state": "ignorance", "confidence": null, "note": "I don't know — not a low probability"},
  "axiological_metadata": {"verdict": "refuse_to_act", "rule": "no_commit_on_ignorance"}
}
```

A federation layer (for example, Trino) may *query* committed triples together with their envelopes — for example, "which committed income facts carry a high-confidence belief and a Commit verdict." Querying confidence does not authorize a new commitment. Auto-approval is an axiological rule that returns Commit, not a confidence cutoff.

**End state vs. evolution.** The SPO/quad hypergraph + lakehouse described here is the **imperative end state** — every agency substrate must converge on owned triples with layer metadata envelopes and federated cross-layer query. Agencies **evolve** toward that target incrementally (e.g. Iceberg/Parquet with SPO-compatible schemas first, pilot triple store, then enterprise graph + federation). Interim storage is valid when ownership, open formats, provenance, and a documented migration path to SPO/quad end state are in place. See [Data Substrate Concept — End State vs. Evolution Path](docs/Data-Substrate-Concept.md#end-state-vs-evolution-path).

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

#### 5.1.1 Per-Layer Storage Mapping

Each MOEPA layer has a natural philosophical and computational representation for its knowledge artifacts. The shared substrate stores the **base triple once**; each layer attaches a **metadata envelope** (or a linked sub-graph) without duplicating the base fact.

| Layer | Natural Representation | Storage on Shared Substrate |
| :--- | :--- | :--- |
| **Data / Set Theory** *(substrate native)* | Raw mathematical objects: sets, multisets, relations, functions, probability distributions, tuples, arrays, tensors | Tabular datasets (Apache Iceberg / Polaris), Parquet files, matrix/vector stores. This is the substrate's own native representation — not a scored MOEPA layer. |
| **Ontology / Graph** | Entities, categories, hierarchies, typed relations; graphs, taxonomies, semantic networks. Existence is categorical. | Native graph DBs (Neo4j, property graphs) or RDF-style triples; nodes = entities, edges = relations. Schema rejects confidence, probability, and "maybe" as properties of an entity. |
| **Epistemology** | Beliefs, defeaters, ignorance, evidence trails, calibrated confidence, justificatory provenance (Bayesian networks, argumentation frameworks) | Epistemic envelope beside the triple: `state` ∈ {belief, defeater, ignorance}, confidence (null when ignorant), justification, defeater list, PROV-O links. The envelope is not part of the entity schema. |
| **Praxeology** | Action space, state-transition rules, procedural preconditions, human checkpoints, action logs | Discrete transition records: current state, verb, admitted true/false, failed precondition if any. No confidence edge. |
| **Axiology** | Deontic rules and the permission set {Commit, Forbid, Refuse to Act}. Preference models may explain why a rule was adopted; they are not the verdict. | Verdict record attached as metadata: `verdict`, rule id, policy version. Weighted value graphs may exist as design-time models. Runtime authorization reads only the verdict. |

**Unification principle.** All five layers write to and read from the same SPO-centric hypergraph + lakehouse, under the control flow in §1.4. Probabilistic layers append observations and proposals. Deterministic layers append categorical state, admissions, and verdicts. A federation layer (Trino or equivalent) can ask: *"which committed income triples have a Belief envelope, an admitted transition, and verdict Commit."* That query reads history. It does not create a new commitment.

**Scale range.** From GTSS edge devices (lightweight JSON triples + SQLite) to enterprise deployments (full graph + Iceberg).

### 5.2 Architectural Evolution Principles

All implementations adopting the MOEPA Cognitive Architecture must follow the
[Architectural Governance and Evolution Guidelines](docs/MOEPA-Architectural-Governance-and-Evolution-Guidelines.md).

**Governance over abstraction.** Avoid vendor-locked orchestration — native
Bedrock-only tooling, LangChain glue-code, or equivalent framework coupling
that cannot be ported. Use the Model Context Protocol (MCP) as the standardized
interface for all data and tool access. New capabilities are defined as MCP
servers so logic remains portable across hosts (Bedrock, self-hosted
orchestrators, or equivalent runtimes).

**From fragments to semantic objects.** No chainsaw chunking. Ingestion uses
document-aware semantic parsing (Docling, Unstructured, or equivalent). Every
data object carries provenance, structure, and semantic metadata. Chunks are
Proto-SPOs (Sovereign Processing Objects) that preserve semantic intent
end-to-end before converging to owned SPO/quad records on the substrate.

**MCP-first pattern.** Orchestrators do not call data or RAG layers directly.
Service logic lives inside MCP-compliant services. Legacy APIs required for
throughput are wrapped in MCP facades so capabilities remain visible and
governable for AI orchestrators.

**Proposal, then arbiter.** State-changing MCP tools are registered on
Praxeology or Axiology. Epistemology tools return a proposal (Belief, Defeater,
or Ignorance). A tool that writes a triple or causes an external effect checks
the axiological verdict and runs only on Commit.

## 6. Implementation Playbook
### 6.1 Recommended Technology Stack by Layer (Ownership-Focused)

**Cross-cutting — MCP integration layer:** Expose every layer capability as an
MCP server or MCP facade. Orchestrators (Bedrock Agents, LangGraph routers,
policy-governed agent runtimes) discover and invoke tools only through MCP — never
through direct RAG or data-layer API calls.

- Metrology (Data Foundation): Self-hosted data lakes (MinIO + Iceberg), Great
  Expectations or Monte Carlo for quality, DataHub for catalog — avoiding
  external repository/catalog ownership. Semantic document parsing via Docling,
  Unstructured, or equivalent; ingestion outputs Proto-SPOs with provenance
  envelopes, exposed through an MCP ingestion server.
- Ontology: Neo4j or Amazon Neptune (self-managed), internal schema governance;
  entity resolution and graph queries exposed as MCP tools.
- Epistemology: Self-hosted retrieval (PGVector/Chroma) plus an inference
  runtime that returns Belief, Defeater, or Ignorance. RAG is an MCP server
  that feeds the proposal. It is not an authorization path.
- Praxeology: Deterministic workflow engines (LangGraph, Temporal, Camunda)
  whose edges are preconditions, not confidence thresholds. Human checkpoints
  are states. Transitions are MCP tools.
- Axiology: OPA/Gatekeeper (or an equivalent policy agent) whose decision
  set is Commit, Forbid, and Refuse to Act. Golden Master configs are
  write-locked. State-changing tools call this gate and proceed only on Commit.

### 6.2 Quick-Start Checklist for New Projects
- Define Metrology boundary: units, calibration, error bounds, and disagreement rules (internal control, not vendor-owned).
- Implement semantic ingestion producing Proto-SPOs with provenance, structure, and semantic metadata (no chainsaw chunking).
- Expose measurement and inference as MCP servers that return proposals, not permissions.
- Create or extend the domain ontology so entity schemas are categorical. Reject confidence on the entity.
- Implement inference that can return Belief, Defeater, or Ignorance, with citations in the epistemic envelope.
- Design the action space as a state machine. Do not route on confidence cutoffs.
- Implement the axiological arbiter (Commit, Forbid, Refuse to Act) and bind every state-changing tool to Commit.
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

## 9. Governance of the Philosophical AI Architecture
The practices below describe how an organization adopting the Philosophical AI Architecture and MOEPA 5-Layer Framework should govern its own instance. Architectural evolution rules (MCP-first integration, semantic ingestion, Proto-SPOs, five-layer PR gate) are defined in [Architectural Governance and Evolution Guidelines](docs/MOEPA-Architectural-Governance-and-Evolution-Guidelines.md). To propose changes to this repository itself, see [CONTRIBUTING.md](CONTRIBUTING.md).

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
