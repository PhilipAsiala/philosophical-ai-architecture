---
marp: true
theme: default
paginate: true
size: 16:9
title: "MOEPA: A Federal Leader's Guide to Owning AI Strategy"
---

<!-- _class: lead -->

# MOEPA: A Federal Leader's Guide to Owning AI Strategy

## Evaluating Use Cases Through First-Principles Cognitive Architecture

*A strategic briefing for senior federal executives, agency CIOs, and mission leaders*

---

## The Inflection Point

Federal agencies face a **defining inflection point.**

The market is flooded with AI offerings—each promising transformation through powerful, easy-to-integrate platforms.

**The hidden price of those platforms is control:**
- Data locked in vendor clouds
- Reasoning logic hidden in black-box models
- Audit trails that satisfy a marketing brief—not an Inspector General

> The goal is not to slow AI adoption. It is to adopt AI on the **agency's terms**.

---

## Why Ownership Matters

Federal law and mission integrity demand it:

- **Taxpayer Bill of Rights** — accuracy and fairness are non-negotiable
- **Congressional oversight** — transparency and accountability are required
- **Mission integrity** — the agency—not a vendor—must own the rules, the data, and the decision logic

An agency that cannot explain how its AI reached a determination cannot defend it to an IG, a GAO reviewer, or a taxpayer challenging the result.

---

## What MOEPA Delivers

MOEPA provides a five-layer cognitive architecture model plus a unified, agency-owned knowledge substrate. Applied systematically, it gives federal leadership the tools to:

- **Evaluate** any AI use case against clear, auditable criteria before approving investment
- **Distinguish** capability the agency must own from commodity compute it can safely rent
- **Protect** data sovereignty and provide complete audit lineage to oversight bodies (IG, GAO, Congress)
- **Ensure** mission values, taxpayer rights, and compliance mandates are built into the architecture—not bolted on as an afterthought

---

<!-- _class: lead -->

# Section 1

## The Five-Layer Evaluation Lens

---

## The Five Layers at a Glance

| Layer | What It Governs | Core Federal Leadership Question | Risk If Unowned |
| --- | --- | --- | --- |
| **Metrology** | Trust of measurement — data quality, calibration, audit lineage, observational provenance | Do we measure, trust, and can we audit the data this system uses? | Data errors propagate undetected; audit findings become indefensible; vendor owns the quality gate |
| **Ontology** | Structure of reality — entity models, relationships, domain definitions | Do we own our entity models, taxonomies, and the meaning of our data? | Agency loses control of how taxpayers, cases, and assets are defined; vendor terminology governs decisions |
| **Epistemology** | Trust of knowledge — confidence levels, provenance, verification, evidence chains | Can we trace how every answer was reached and who or what verified it? | Black-box outputs fail IG review; no audit trail for contested decisions or appeals |
| **Praxeology** | Purposeful action — workflows, decision procedures, human oversight points | Does the system support actual agency workflows and preserve required human oversight? | Autonomous actions without oversight; explainability gaps in high-stakes benefit or enforcement decisions |
| **Axiology** | Values and mission alignment — compliance mandates, fairness rules, taxpayer rights | Are the Taxpayer Bill of Rights, fairness guardrails, and compliance mandates architecturally enforced? | Values embedded only in prompts are easily bypassed; compliance failures during audit, enforcement, or appeal |

---

## Plain-Language Walkthrough: Income Verification

Each layer asks a concrete, leadership-level question:

- **Metrology** asks: Is the income figure we are using trustworthy? Has it been measured, calibrated, and quality-checked—or did it arrive unchecked from an unaudited vendor pipeline?
- **Ontology** asks: Do we have a shared, agency-owned understanding of what "income," "taxpayer," "household," and "eligibility period" mean—or does each system define them differently?
- **Epistemology** asks: With what confidence has this income figure been verified, and can we show the evidence chain to an IG examiner or a taxpayer challenging the determination?
- **Praxeology** asks: Does the workflow map to actual adjudication rules—auto-approve routine cases, escalate edge cases, require human sign-off at defined thresholds—or does it produce a generic output disconnected from policy?
- **Axiology** asks: Are the rights (right to appeal, right to explanation, non-discrimination requirements) hardcoded into the architecture, or are they only in a prompt that a developer can quietly modify?

---

<!-- _class: lead -->

# Section 2

## The Owned Data Substrate

---

## What the Substrate Is

Beneath all five scored MOEPA layers sits the **MOEPA Data Substrate** — the agency's owned knowledge library.

- Facts, relationships, and decisions that all five layers write to and read from
- Built on **Subject-Predicate-Object (SPO) triples** + open-format lakehouse storage
- **Not a sixth scored layer** — the representation medium and storage backbone

A concrete example:

```
Subject:              IncomeVerification:TX12345
Predicate:            hasAmount
Object:               85000
Epistemic metadata:   confidence 0.98, source: ThirdPartyStudy_2025 (n=125,000)
```

One fact. One owned record. Complete cross-layer traceability.

---

## Vendor-Managed vs. Agency-Owned Substrate

| Concern | Vendor-Managed Approach | Agency-Owned Substrate |
| --- | --- | --- |
| Data sovereignty | Facts stored in vendor cloud or proprietary format | Facts stored in open formats (SPO triples + Apache Iceberg/Parquet) on agency-controlled infrastructure |
| Audit and provenance | Opaque; vendor provides what audit trail it chooses | Full PROV-O-compatible lineage; every fact traceable to its source, measurement standard, and evidence chain |
| Portability | Migration requires vendor cooperation; meaning is often non-portable | Open graph + lakehouse formats; agency can migrate, federate, or replicate independently |
| Cross-system reuse | Each system builds its own siloed knowledge store | One base triple reused across all use cases; no duplication of authoritative facts |
| Scale | Vendor-managed scaling at vendor pricing | From lightweight edge deployment (JSON triples + SQLite) to full enterprise graph + Iceberg |

---

<!-- _class: lead -->

# Section 3

## How to Evaluate Any AI Use Case

---

## Scoring Rubric: Decision Bands

Every AI use case is scored 1–5 per layer. The **lowest layer sets the recommendation band.**

- **NO-GO:** Any layer scores 1 or 2 — automatic NO-GO; remediation required before re-submission
- **CONDITIONAL GO:** Every layer scores ≥ 3 and at least one scores exactly 3 — approved only with named controls and active oversight for the lowest-scoring layer
- **GO:** Every layer scores ≥ 4

A system with four perfect scores and one weak layer is still a NO-GO or CONDITIONAL GO until that layer is remediated.

**Substrate sovereignty check** (separate from scoring): Does the agency control its own knowledge library, or is it dependent on a vendor to access, export, or reason over its own data?

---

## Vendor-Rented vs. Owned-MOEPA

| Evaluation Criterion | Vendor-Rented Approach | Agency-Owned MOEPA Approach | Indicative Score |
| --- | --- | --- | --- |
| **Data Sovereignty** (Metrology) | Data stored in vendor cloud; quality gates defined and operated by vendor | Agency controls data lake (Iceberg/Parquet); internal quality rules; provenance tracked by agency | Vendor: 1–2 / Owned: 4–5 |
| **Epistemic Transparency** (Epistemology) | Confidence is opaque; no traceable evidence chain; outputs served without deterministic cross-check | Every claim carries confidence score (e.g., 0.98) with provenance; IG-reviewable evidence chain | Vendor: 1–2 / Owned: 4–5 |
| **Action Alignment** (Praxeology) | Generic outputs; workflow mapping is the agency's burden post-procurement | Policy-linked workflow; deterministic state machine; human oversight at defined thresholds | Vendor: 2–3 / Owned: 4–5 |
| **Value/Compliance Guardrails** (Axiology) | Rights protections embedded in prompt; bypassable; compliance is asserted not enforced | Taxpayer Bill of Rights, fairness rules, and compliance mandates hardcoded in architecture | Vendor: 1–2 / Owned: 4–5 |
| **Ontology Ownership** (Ontology) | Vendor defines what "taxpayer," "income," "household" mean in their platform | Agency owns semantic model; entity definitions version-controlled and auditable | Vendor: 1–2 / Owned: 4–5 |
| **Long-term Ownership Cost** | Perpetual licensing; data portability requires vendor cooperation; exit costs high | One-time build + open-source maintenance; agency-controlled migration path | Vendor: 1–2 / Owned: 4–5 |

---

## Sample Scoring: Income Verification

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

<!-- _class: lead -->

# Section 4

## Owned vs. Rented Decision Patterns

---

## Worked Example: Income Verification (Steps 1–3)

**Scenario:** Verify a taxpayer's reported income of $85,000 for a credit determination.

**Step 1 — Metrology:** The $85,000 figure enters through an agency-owned quality gate — calibrated, corroborated (cross-referenced study, n = 125,000), with observational lineage: source, measurement date, quality check result, and drift status.

**Step 2 — Ontology:** The agency's owned semantic model defines "IncomeVerification," "TX12345," and "hasAmount" — version-controlled and consistent across every system.

```
Triple: IncomeVerification:TX12345 — hasAmount → 85000
```

**Step 3 — Epistemology:** The base fact is enriched with an epistemic metadata envelope:

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

---

## Worked Example: Income Verification (Steps 4–5 + Result)

**Step 4 — Praxeology:** The workflow maps directly to agency policy:
- Income ≤ threshold with confidence ≥ 0.95 → **auto-approve** routine determination
- Edge cases → **human review queue** with documented escalation reason
- A deterministic state machine the agency controls — not a generic AI output

**Step 5 — Axiology:** The Taxpayer Bill of Rights is architecturally enforced before any determination is finalized:
- Right to explanation ✓
- Right to appeal ✓
- Non-discrimination rules ✓
- Hardcoded constraints — not prompt-level guidelines

**Result:** A defensible, auditable determination — traceable from measurement standard through verification evidence to decision procedure to rights check — all stored in the agency's owned knowledge library.

---

## Implications for Common Federal Patterns

| Federal Scenario | Without MOEPA Ownership | With MOEPA + Owned Substrate |
| --- | --- | --- |
| Audit by IG or GAO | "The system produced this output" — no further trace | Full five-layer audit trail; every decision reconstructible |
| Taxpayer appeal | Cannot explain confidence or evidence basis | 0.98 confidence with PROV-O chain available to taxpayer representative |
| Policy change (e.g., new eligibility rules) | Vendor update cycle; unclear propagation | Agency updates axiological rule set; propagation is traceable and version-controlled |
| Vendor exit or pricing change | Data migration uncertain; knowledge non-portable | Agency retains full owned substrate; compute is the only vendor-dependent element |
| Congressional inquiry | Vendor-mediated response | Agency provides complete, internally documented decision record |

---

<!-- _class: lead -->

# Section 5

## Quick Wins and Implementation Roadmap

---

## Recommended Pilot

**Cognitive intake assistant built on the agency's owned intake process**

An ideal first deployment — visible, high-interaction, lower individual-transaction stakes.

Pilot objectives:
1. Stand up an owned SPO triple store for intake facts (taxpayer type, issue category, documentation status)
2. Apply Metrology quality gates to intake data before it enters the reasoning layer
3. Build the initial agency ontology for intake entities and relationships
4. Implement a deterministic workflow (Praxeology) that maps to actual intake policy
5. Hardcode the rights constraints (Axiology) for the intake context

---

## Migration Path

**Quick wins (0–3 months)**
- Inventory current AI investments against the five-layer scorecard
- Identify which layers are currently vendor-owned (most common: Metrology and Ontology)
- Establish internal data quality baseline for the highest-value data asset
- Begin versioning core entity definitions (taxpayer, case, transaction) in an agency-controlled schema

**Layer-by-layer ownership (3–12 months)**
- Migrate highest-risk data to agency-controlled open-format storage (Metrology)
- Stand up an internal semantic model for the pilot domain (Ontology)
- Implement provenance and confidence tracking for the pilot use case (Epistemology)
- Design deterministic workflow state machines for the pilot (Praxeology)
- Formalize the axiological rule set and enforce architecturally (Axiology)

**Full owned brain (12–24 months)**
- Enterprise-wide substrate (SPO graph + Iceberg) deployed and governed
- All five layers owned across priority use cases
- MOEPA scoring used as the standard gate for all new AI procurement
- Vendor relationships scoped to rented compute only; no vendor owns a scored layer

---

## What to Require of Vendors Now

Even before full ownership is achieved, agency leaders can immediately require vendors to:

- **Provide complete data export** in open formats (SPO-compatible, Parquet, or equivalent)
- **Document the confidence and provenance model** for all AI-generated outputs
- **Map their solution to the five MOEPA layers** and score each layer honestly
- **Identify which layers they own** versus which the agency controls
- **Demonstrate audit-trail compatibility** with IG and GAO review requirements

> This reframes every vendor conversation from "What features do you offer?" to **"Can we defend this system to oversight?"**

---

## Appendix: Illustrative Scoring Patterns

*Assessments are illustrative only, based on publicly documented default configurations. Not endorsements or disqualifications of any vendor.*

| Pattern | Description | Overall | Basis |
| --- | --- | --- | --- |
| **Pattern A** | Large-vendor agentic SaaS platform (default configuration) | **NO-GO** | Metrology, Ontology, Epistemology, Axiology all score ≤ 2 |
| **Pattern B** | Data lakehouse platform with custom AI build (e.g., Databricks-style stack) | **CONDITIONAL GO** | Achievable GO with deliberate agency ownership of Ontology and Axiology layers |
| **Pattern C** | Fully owned MOEPA stack (agency-implemented, open tools) | **GO** | All layers ≥ 4 |

For full per-layer scoring tables, see the [source guide](../moepa-federal-leaders-guide.md).

---

## References & Further Reading

**Full documentation:**
- 📄 [Federal Leader's Guide](../moepa-federal-leaders-guide.md) — this deck's source of truth
- 📄 [Business Leader's Guide](../moepa-business-leaders-guide.md) — industry-neutral companion
- 📐 [Architecture Specification](../../ARCHITECTURE.md) — full technical spec and scoring rubric
- 📋 [Per-Layer Catalog](../../catalog/README.md) — concrete scoring, tool patterns, and example assets by layer

**Important note:** Vendor pattern assessments in the Appendix are illustrative only, based on publicly documented default configurations. Actual scores depend on specific implementation choices, contract terms, and agency deployment patterns. They are not endorsements or disqualifications of any vendor.
