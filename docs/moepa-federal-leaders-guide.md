# MOEPA: A Federal Leader's Guide to Owning AI Strategy

## The Philosophical AI Architecture — A Cognitive Control Plane for Federal AI

*A strategic handout for senior federal executives, agency CIOs, and mission leaders*

---

## Executive Summary

Federal agencies face a defining inflection point. The market is flooded with AI offerings—each promising transformation through powerful, easy-to-integrate platforms. The hidden price of those platforms is control: data locked in vendor clouds, reasoning logic hidden in black-box models, and audit trails that satisfy a marketing brief but not an Inspector General.

The Taxpayer Bill of Rights demands accuracy and fairness. Congressional oversight demands transparency and accountability. Mission integrity demands that the agency—not a vendor—owns the rules, the data, and the decision logic.

The **Philosophical AI Architecture** provides a cognitive control plane — a unified, agency-owned **Data Substrate** plus the **MOEPA Catalog** — to make ownership practical and defensible. The **MOEPA 5-Layer Framework** is the go/no-go intake rubric inside that architecture. Applied systematically, they give federal leadership the tools to:

- Evaluate any AI use case against clear, auditable criteria before approving investment
- Distinguish between capability the agency must own and commodity compute it can safely rent
- Protect data sovereignty and provide complete audit lineage to oversight bodies (IG, GAO, Congress)
- Ensure mission values, taxpayer rights, and compliance mandates are built into the architecture—not bolted on as an afterthought

**The goal is not to slow AI adoption.** It is to adopt AI on the agency's terms: with clear ownership, explainable decisions, and alignment to the people and mission the agency serves.

---

## Section 1 — The Five-Layer Evaluation Lens

### What MOEPA Is

The MOEPA 5-Layer Framework is built on five classical disciplines of human reasoning, translated into five leadership responsibilities for AI governance. The acronym stands for **Metrology, Ontology, Epistemology, Praxeology, and Axiology**—in that order, from the data foundation up through value governance. Area leaders must prove how their project enriches the MOEPA Catalog across all five layers. Black-box vendor solutions that cannot map to the framework fail intake by design.

Each layer answers a distinct question federal leadership must be able to answer about any AI system the agency operates or procures.

### The Five Layers at a Glance

| Layer | What It Governs | Core Federal Leadership Question | Risk If Unowned |
| --- | --- | --- | --- |
| **Metrology** | Trust of measurement — data quality, calibration, audit lineage, observational provenance | Do we measure, trust, and can we audit the data this system uses? | Data errors propagate undetected; audit findings become indefensible; vendor owns the quality gate |
| **Ontology** | Structure of reality — entity models, relationships, domain definitions | Do we own our entity models, taxonomies, and the meaning of our data? | Agency loses control of how taxpayers, cases, and assets are defined; vendor terminology governs decisions |
| **Epistemology** | Trust of knowledge — confidence levels, provenance, verification, evidence chains | Can we trace how every answer was reached and who or what verified it? | Black-box outputs fail IG review; no audit trail for contested decisions or appeals |
| **Praxeology** | Purposeful action — workflows, decision procedures, human oversight points | Does the system support actual agency workflows and preserve required human oversight? | Autonomous actions without oversight; explainability gaps in high-stakes benefit or enforcement decisions |
| **Axiology** | Values and mission alignment — compliance mandates, fairness rules, taxpayer rights | Are the Taxpayer Bill of Rights, fairness guardrails, and compliance mandates architecturally enforced? | Values embedded only in prompts are easily bypassed; compliance failures during audit, enforcement, or appeal |

### A Plain-Language Walkthrough

To make these layers concrete, consider a federal benefits or tax-processing scenario—for example, verifying a taxpayer's reported income for a credit determination.

- **Metrology** asks: Is the income figure we are using trustworthy? Has it been measured, calibrated, and quality-checked against a known standard, or did it arrive unchecked from an unaudited vendor pipeline?
- **Ontology** asks: Do we have a shared, agency-owned understanding of what "income," "taxpayer," "household," and "eligibility period" mean—or does each system define them differently?
- **Epistemology** asks: With what confidence has this income figure been verified, and can we show the evidence chain to an IG examiner or a taxpayer challenging the determination?
- **Praxeology** asks: Does the workflow map to actual adjudication rules—auto-approve routine cases, escalate edge cases, require human sign-off at defined thresholds—or does it produce a generic output disconnected from policy?
- **Axiology** asks: Are the rights (right to appeal, right to explanation, non-discrimination requirements) hardcoded into the architecture, or are they only in a prompt that a developer can quietly modify?

Leaders do not need to understand every technical implementation detail. They do need to understand what the agency must own at each layer to protect accuracy, fairness, and accountability.

---

## Section 2 — The Owned Data Substrate (Your Agency's Knowledge Library)

### What the Substrate Is

Beneath all five scored MOEPA layers sits a single, cross-cutting foundation: the **MOEPA Data Substrate**. It is the agency's owned knowledge library—the persistent catalog of facts, relationships, and decisions that all five layers write to and read from.

The substrate is **not a sixth scored layer**. It is the representation medium and storage backbone that makes five-layer ownership coherent. Think of it as the agency's own library stacks: the five layers are the reading rooms that specialize in different kinds of reasoning, but every volume lives in the same owned, catalogued archive.

Technically, the substrate is built on **Subject-Predicate-Object (SPO) triples**—the same logical structure underlying all major knowledge graphs and semantic databases—plus open-format lakehouse storage. A concrete example from ARCHITECTURE.md §5.1:

```
Subject:              IncomeVerification:TX12345
Predicate:            hasAmount
Object:               85000
Epistemic metadata:   confidence 0.98, source: ThirdPartyStudy_2025 (n=125,000)
```

Each MOEPA layer can attach its own metadata envelope to that base fact without duplicating it. The Metrology layer owns the trust properties (quality checks passed, source calibration, measurement standard). The Epistemology layer owns the confidence and provenance. The Praxeology layer links the decision procedure. The Axiology layer attaches the rights and fairness constraints. One fact; one owned record; complete cross-layer traceability.

### Why This Matters for Federal Ownership

Most vendor AI platforms store knowledge—including the agency's own data about taxpayers, cases, and assets—inside proprietary vector databases, cloud-specific embedding stores, or black-box knowledge graphs the agency does not control. When the contract ends, the data is difficult to export; the relationships and meanings are even harder.

The MOEPA substrate inverts this dynamic:

| Concern | Vendor-Managed Approach | Agency-Owned Substrate |
| --- | --- | --- |
| Data sovereignty | Facts stored in vendor cloud or proprietary format | Facts stored in open formats (SPO triples + Apache Iceberg/Parquet) on agency-controlled infrastructure |
| Audit and provenance | Opaque; vendor provides what audit trail it chooses | Full PROV-O-compatible lineage; every fact traceable to its source, measurement standard, and evidence chain |
| Portability | Migration requires vendor cooperation; meaning is often non-portable | Open graph + lakehouse formats; agency can migrate, federate, or replicate independently |
| Cross-system reuse | Each system builds its own siloed knowledge store | One base triple reused across all use cases; no duplication of authoritative facts |
| Scale | Vendor-managed scaling at vendor pricing | From lightweight edge deployment (JSON triples + SQLite for field or constrained environments) to full enterprise graph + Iceberg |

The substrate is also the mechanism that makes audit lineage real rather than aspirational. When an IG, GAO reviewer, or taxpayer representative asks "How did the system reach this determination?", the answer should trace back through all five layers—from the trusted data (Metrology) through the verified knowledge (Epistemology) to the decision procedure (Praxeology) to the rights check (Axiology)—as a single owned, queryable record. That is only possible when the agency owns the substrate.

---

## Section 3 — How to Evaluate Any AI Use Case (Scoring Rubric)

### The Evaluation Model

Every AI procurement request, internal use case, or vendor proposal can be scored against the five MOEPA layers using the repo's existing **1–5 scale with GO / CONDITIONAL GO / NO-GO decision bands** (see [ARCHITECTURE.md §4.2](../ARCHITECTURE.md) and the [catalog scoring guides](../catalog/README.md) for full rubric detail).

**Decision bands:**
- **NO-GO:** Any layer scores 1 or 2 — automatic NO-GO; remediation required before re-submission
- **CONDITIONAL GO:** Every layer scores ≥ 3 and at least one layer scores exactly 3 — approved only with named controls and active oversight demonstrably in place for the lowest-scoring layer
- **GO:** Every layer scores ≥ 4

The lowest layer score sets the recommendation band. A system with four perfect scores and one weak layer is still a NO-GO or CONDITIONAL GO until that layer is remediated.

**Substrate sovereignty check:** The Data Substrate is assessed separately as an ownership and sovereignty audit—not as a scored layer. The question is: does the agency control its own knowledge library, or is it dependent on a vendor to access, export, or reason over its own data?

### Vendor-Rented vs. Owned-MOEPA Comparison

| Evaluation Criterion | Vendor-Rented Approach | Agency-Owned MOEPA Approach | Indicative Score |
| --- | --- | --- | --- |
| **Data Sovereignty** (Metrology) | Data stored in vendor cloud; quality gates defined and operated by vendor | Agency controls data lake (Iceberg/Parquet); internal quality rules; provenance tracked by agency | Vendor: 1–2 / Owned: 4–5 |
| **Epistemic Transparency** (Epistemology) | Confidence is opaque; no traceable evidence chain; outputs served without deterministic cross-check | Every claim carries confidence score (e.g., 0.98) with provenance; IG-reviewable evidence chain | Vendor: 1–2 / Owned: 4–5 |
| **Action Alignment** (Praxeology) | Generic outputs; workflow mapping is the agency's burden post-procurement | Policy-linked workflow; deterministic state machine; human oversight at defined thresholds | Vendor: 2–3 / Owned: 4–5 |
| **Value/Compliance Guardrails** (Axiology) | Rights protections embedded in prompt; bypassable; compliance is asserted not enforced | Taxpayer Bill of Rights, fairness rules, and compliance mandates hardcoded in architecture | Vendor: 1–2 / Owned: 4–5 |
| **Ontology Ownership** (Ontology) | Vendor defines what "taxpayer," "income," "household" mean in their platform | Agency owns semantic model; entity definitions version-controlled and auditable | Vendor: 1–2 / Owned: 4–5 |
| **Long-term Ownership Cost** | Perpetual licensing; data portability requires vendor cooperation; exit costs high | One-time build + open-source maintenance; agency-controlled migration path | Vendor: 1–2 / Owned: 4–5 |

**+ Substrate sovereignty check (separate from scoring):**

| Substrate Question | Vendor-Rented | Agency-Owned |
| --- | --- | --- |
| Where do agency knowledge facts live? | Vendor proprietary store | Agency-controlled graph + lakehouse |
| Can the agency query its own data independently? | Only through vendor API | Direct; open-format; portable |
| What happens at contract end? | Data export uncertain; meaning non-portable | Agency retains full knowledge library |
| Is provenance auditable to IG standards? | Vendor-defined; often opaque | Full PROV-O lineage; cross-layer traceability |

### Sample Scoring: Income-Verification Use Case

*Illustrative only — actual scores depend on specific implementation details.*

| Layer | Owned MOEPA Score | Rationale |
| --- | --- | --- |
| Metrology | 5 | Internal data lake; calibrated against IRS third-party sources (n = 125,000); observational lineage tracked |
| Ontology | 5 | Agency-owned semantic model; taxpayer and income entities version-controlled |
| Epistemology | 5 | 0.98 confidence with PROV-O evidence chain; fully traceable to source |
| Praxeology | 4 | Deterministic workflow; auto-approve routine; human escalation at edge cases |
| Axiology | 4 | Taxpayer Bill of Rights enforced; fairness rules in architecture; appeals workflow linked |
| **Overall** | **GO** | All layers ≥ 4 |

**Substrate sovereignty: Agency-Owned** — facts stored in owned SPO graph + Iceberg; auditable and portable.

---

## Section 4 — Owned vs. Rented Decision Patterns

### The End-to-End Worked Example: Income Verification

The following illustrates all five layers and the substrate working together on a real federal use case. This example is consistent with [ARCHITECTURE.md §5.1](../ARCHITECTURE.md).

**Scenario:** The agency needs to verify a taxpayer's reported income of $85,000 for a credit determination.

**Step 1 — Metrology (Trust the measurement)**
The $85,000 figure enters the system through a Metrology-governed quality gate. It is checked against calibration standards, compared to third-party corroboration (cross-referenced study, n = 125,000), and assigned an observational lineage record: source, measurement date, quality check result, and drift status. The agency owns this gate.

**Step 2 — Ontology (Structure the reality)**
The agency's owned semantic model defines what "IncomeVerification," "TX12345" (taxpayer identifier), and "hasAmount" mean in this context. These definitions are version-controlled, agency-owned, and consistent across every system that touches taxpayer data.

```
Triple: IncomeVerification:TX12345 — hasAmount → 85000
```

**Step 3 — Epistemology (Verify the knowledge)**
The base fact is enriched with an epistemic metadata envelope: confidence 0.98, justification from ThirdPartyStudy_2025, status HighReliability. The evidence chain is stored in the substrate using PROV-O-compatible provenance. An IG examiner or taxpayer representative can retrieve it on demand.

```json
{
  "triple": {"s": "IncomeVerification:TX12345", "p": "hasAmount", "o": 85000},
  "epistemic_metadata": {
    "confidence": 0.98,
    "justification": "ThirdPartyStudy_2025_n=125000",
    "status": "HighReliability"
  }
}
```

**Step 4 — Praxeology (Align the action)**
The workflow maps directly to agency policy: income ≤ threshold with confidence ≥ 0.95 → auto-approve routine determination; edge cases → human review queue with documented escalation reason. The decision procedure is a deterministic state machine the agency controls, not a generic AI output.

**Step 5 — Axiology (Enforce the values)**
The Taxpayer Bill of Rights is architecturally enforced. The right to explanation, the right to appeal, and non-discrimination rules are checked before any determination is finalized. These are hardcoded constraints, not prompt-level guidelines.

**Result:** A defensible, auditable determination—traceable from the measurement standard through the verification evidence to the decision procedure to the rights check—all stored in the agency's owned knowledge library.

### Implications for Common Federal Patterns

| Federal Scenario | Without MOEPA Ownership | With MOEPA + Owned Substrate |
| --- | --- | --- |
| Audit by IG or GAO | "The system produced this output" — no further trace | Full five-layer audit trail; every decision reconstructible |
| Taxpayer appeal | Cannot explain confidence or evidence basis | 0.98 confidence with PROV-O chain available to taxpayer representative |
| Policy change (e.g., new eligibility rules) | Vendor update cycle; unclear propagation | Agency updates axiological rule set; propagation is traceable and version-controlled |
| Vendor exit or pricing change | Data migration uncertain; knowledge non-portable | Agency retains full owned substrate; compute is the only vendor-dependent element |
| Congressional inquiry | Vendor-mediated response | Agency provides complete, internally documented decision record |

---

## Section 5 — Quick Wins and Implementation Roadmap

### Where to Start

Federal agencies do not need to rebuild their entire AI estate to begin capturing MOEPA benefits. A staged approach—start narrow, prove the model, expand—reduces risk and builds internal capability before enterprise commitment.

**Recommended pilot: Cognitive intake assistant built on agency-owned intake process**

A conversational AI intake assistant that guides taxpayers or staff through a structured intake process is an ideal first deployment. It is visible, high-interaction, and immediately demonstrable—but the stakes of any individual transaction are lower than enforcement or determination. More importantly, the agency's own intake workflow *is* the knowledge model, so owning the ontology and workflow from day one is natural rather than aspirational.

Pilot objectives:
1. Stand up an owned SPO triple store for intake facts (taxpayer type, issue category, documentation status)
2. Apply Metrology quality gates to intake data before it enters the reasoning layer
3. Build the initial agency ontology for intake entities and relationships
4. Implement a deterministic workflow (Praxeology) that maps to actual intake policy
5. Hardcode the rights constraints (Axiology) for the intake context

### Migration Path from Current Stack

**Quick wins (0–3 months)**
- Inventory current AI investments against the five-layer scorecard
- Identify which layers are currently vendor-owned (most common: Metrology and Ontology)
- Establish internal data quality baseline for the highest-value data asset
- Begin versioning the agency's core entity definitions (taxpayer, case, transaction) in an agency-controlled schema

**Layer-by-layer ownership (3–12 months)**
- Migrate highest-risk data (Metrology layer) to agency-controlled open-format storage
- Stand up an internal semantic model (Ontology layer) for the pilot domain
- Implement provenance and confidence tracking (Epistemology layer) for the pilot use case
- Design deterministic workflow state machines (Praxeology layer) for the pilot
- Formalize the axiological rule set and enforce architecturally (Axiology layer)

**Full owned brain (12–24 months)**
- Enterprise-wide substrate (SPO graph + Iceberg) deployed and governed
- All five layers owned across priority use cases
- MOEPA scoring used as the standard gate for all new AI procurement
- Vendor relationships scoped to rented compute only; no vendor owns a scored layer

### What to Require of Vendors Now

Even before full ownership is achieved, agency leaders can immediately require vendors to:

- Provide complete data export in open formats (SPO-compatible, Parquet, or equivalent)
- Document the confidence and provenance model for all AI-generated outputs
- Map their solution to the five MOEPA layers and score each layer honestly
- Identify which layers they own versus which the agency controls
- Demonstrate audit-trail compatibility with IG and GAO review requirements

This reframes every vendor conversation from "What features do you offer?" to "Can we defend this system to oversight?"

---

## Appendix — Illustrative Vendor Stack Assessments and Open-Source Tool Options

*Assessments below are illustrative only, based on publicly documented default configurations. Actual scores depend on specific implementation choices, contract terms, and agency deployment patterns. These are not endorsements or disqualifications of any vendor.*

### Illustrative MOEPA Scoring: Common Federal AI Patterns

**Pattern A: Large-vendor agentic SaaS platform (default configuration)**

| Layer | Illustrative Score | Basis |
| --- | --- | --- |
| Metrology | 2 | Data quality gates and lineage managed by vendor; agency has limited observability |
| Ontology | 2 | Semantic model is vendor-defined; entity definitions not exportable in agency-usable form |
| Epistemology | 2 | Confidence and provenance opaque; outputs served without deterministic cross-check |
| Praxeology | 3 | Workflow configuration available, but state machine is vendor-controlled; human override is prompt-level |
| Axiology | 2 | Compliance rules embedded in system prompt; bypassable; not architecturally enforced |
| **Overall** | **NO-GO** | Metrology, Ontology, Epistemology, Axiology all score ≤ 2 |

**Pattern B: Data lakehouse platform with custom AI build (e.g., Databricks-style stack)**

| Layer | Illustrative Score | Basis |
| --- | --- | --- |
| Metrology | 3–4 | Good data quality tooling; agency can own the lake if contract terms permit; lineage partially available |
| Ontology | 2–3 | Schema tools available; semantic model ownership depends on implementation choices |
| Epistemology | 3 | RAG with citations available; cryptographic validation requires additional build |
| Praxeology | 3–4 | Workflow orchestration available; deterministic state machines require agency implementation |
| Axiology | 2–3 | Policy-as-code possible but requires explicit agency build; not default |
| **Overall** | **CONDITIONAL GO** | Achievable GO with deliberate agency ownership of Ontology and Axiology layers |

**Pattern C: Fully owned MOEPA stack (agency-implemented, open tools)**

| Layer | Illustrative Score | Basis |
| --- | --- | --- |
| Metrology | 5 | Agency-owned open-format data lake; internal quality observability; provenance tracked |
| Ontology | 5 | Internal semantic knowledge graph; agency-version-controlled entity definitions |
| Epistemology | 5 | Full confidence + PROV-O lineage; IG-reviewable audit chain |
| Praxeology | 5 | Deterministic state machine; human oversight at defined thresholds; full audit trail |
| Axiology | 5 | Rights and compliance rules hardcoded; Golden Master config locked at infrastructure level |
| **Overall** | **GO** | All layers ≥ 4 |

### Migration from a Current Vendor Stack

If the agency is currently operating on a large-vendor platform (data lakehouse + agentic layer), a pragmatic migration sequence is:

1. **Export and own the data first.** Negotiate data portability in open formats as a contractual prerequisite before the next renewal. Establish the Iceberg/Parquet foundation on agency-controlled infrastructure in parallel.
2. **Own the ontology next.** Stand up an internal semantic model (graph triple store) alongside the vendor's semantic layer. Begin migrating entity definitions to the owned model, use case by use case.
3. **Layer in epistemology controls.** Add PROV-O-compatible provenance tracking to the owned substrate. This is the layer that makes IG and GAO review tractable.
4. **Replace workflow orchestration.** Move from vendor-managed workflow to a deterministic state machine the agency controls (open orchestration frameworks). Map each workflow to actual policy.
5. **Lock the axiology layer.** Formalize rights and compliance rules in policy-as-code; apply infrastructure-level write locks. This layer should be the last to migrate but the first to plan.

### Illustrative Open-Source Tool Options

*Listed as illustrative; agency technology selection must follow applicable acquisition and security requirements.*

| MOEPA Layer / Use | Example Open Tools |
| --- | --- |
| Graph / Triple Store (Ontology + Substrate) | Apache Jena, TerminusDB, ArcadeDB, Neo4j Community |
| Lakehouse Storage (Substrate) | Apache Iceberg + Polaris Catalog, Apache Parquet |
| Data Quality and Observability (Metrology) | Great Expectations, Monte Carlo (open tier), Apache Griffin |
| Provenance Tracking (Epistemology) | W3C PROV-O libraries, OpenLineage |
| Workflow Orchestration (Praxeology) | Apache Airflow, LangGraph (open), Prefect |
| Policy-as-Code (Axiology) | Open Policy Agent (OPA), Gatekeeper |
| Catalog / Discoverability (Cross-cutting) | Apache Atlas, DataHub (open tier) |

---

*For the general-enterprise version of this guide (industry-neutral voice, no government-specific examples), see [moepa-business-leaders-guide.md](moepa-business-leaders-guide.md).*

*For the full technical specification, including the MOEPA scoring rubric (§4.2), the Data Substrate definition (§5.1), and per-layer evaluation criteria (§4.3), see [ARCHITECTURE.md](../ARCHITECTURE.md).*

*For the layer-by-layer catalog with concrete scoring, tool patterns, and example assets, see [catalog/README.md](../catalog/README.md).*
