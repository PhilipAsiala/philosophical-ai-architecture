# Owned vs. Rented AI Strategy

> The most consequential AI decision your agency will make is not which model to use — it is which capabilities you own versus which you rent.

---

## The Core Distinction

| | **Rented AI** | **Owned AI** |
|---|---|---|
| **Definition** | Capabilities accessed through a vendor's platform that your organization does not control | Capabilities built on infrastructure, data, and logic that your organization owns and can audit |
| **Cost model** | Subscription or usage fees that grow as adoption grows | Up-front investment with declining marginal cost over time |
| **Switching cost** | High — data, definitions, and workflows may not transfer | Low — open formats and documented logic are portable |
| **Auditability** | Dependent on vendor-provided logs and reports | Full access at any time to any level of detail |
| **Strategic risk** | Vendor controls the roadmap, pricing, and data access | Organization controls direction and intellectual assets |

Neither approach is categorically wrong. The strategic question is: **which layers must be owned, and which can safely be rented?**

---

## The MOEPA Ownership Map

The five MOEPA layers are not equally sensitive to the own/rent decision. This map shows which layers carry the highest risk if left in vendor hands:

```
LAYER 5 — AXIOLOGY        ██████████  MUST OWN
                          Values, policy, and mission compliance cannot be
                          safely outsourced. If a vendor defines your guardrails,
                          your statutory obligations are at risk.

LAYER 4 — PRAXEOLOGY      ████████    STRONGLY PREFER OWNERSHIP
                          Workflow logic and human oversight points should
                          be under organizational control. Renting is
                          acceptable only with strong audit access.

LAYER 3 — EPISTEMOLOGY    ███████     OWN VERIFICATION STANDARDS
                          You may use vendor models for inference, but
                          the verification layer — what counts as truth —
                          must be owned. Never rent your truth standard.

LAYER 2 — ONTOLOGY        ████████    STRONGLY PREFER OWNERSHIP
                          Domain entity definitions and relationships
                          represent core institutional knowledge.
                          Losing this to a vendor is strategic lock-in.

LAYER 1 — METROLOGY       ██████████  MUST OWN
                          Data quality rules and provenance records are
                          the foundation of every other claim.
                          Vendor ownership here creates permanent dependency.

DATA SUBSTRATE            ██████████  MUST OWN
                          The knowledge library is your most durable
                          strategic AI asset. Own it entirely.

COMPUTE & MODELS          ░░░░░░░░░░  SAFE TO RENT
                          GPUs, cloud infrastructure, and pre-trained
                          model weights are commodity inputs. Rent freely
                          as long as your cognitive layer stays owned.
```

---

## Side-by-Side Comparison: Government Use Cases

### Use Case 1: Third-Party Income Verification

| Dimension | Rented Approach | Owned Approach |
|---|---|---|
| **Data source** | Vendor ingests third-party income data into their platform | Agency ingests data into its own open-format lakehouse |
| **Entity definitions** | "Income," "employer," and "filer" defined by vendor schema | Agency maintains canonical entity model with policy-aligned definitions |
| **Verification logic** | Vendor's matching algorithm — no inspection access | Agency-defined verification rules, auditable at record level |
| **Audit trail** | Vendor-generated report provided to agency | Agency-owned log, reproducible point-in-time |
| **Confidence score explanation** | "Our model says 94%" | "94.1% confidence based on match to W-2 (SSA), 1099-MISC (IRS), and bank verification — see records A, B, C" |
| **Vendor contract expiry** | Income data and match history may not transfer | All data, logic, and history remain with agency |
| **Congressional inquiry response** | Must request from vendor | Can produce directly from owned systems |

> **Leader takeaway:** If a taxpayer challenges a decision based on a vendor-supplied income match, can your agency independently verify and explain that match? With a rented approach, the honest answer is often "we cannot — we would need to ask the vendor."

---

### Use Case 2: AI Project Intake Scoring

| Dimension | Rented Approach | Owned Approach |
|---|---|---|
| **Scoring model** | Vendor provides a project scoring tool with pre-set criteria | Agency defines scoring rubric based on MOEPA layers and mission priorities |
| **Criteria transparency** | Black-box weights determine scores | Documented, version-controlled criteria visible to all reviewers |
| **Historical decisions** | Stored in vendor platform — access may change | Stored in agency-owned Data Substrate with full history |
| **Customization** | Limited to vendor-provided configuration options | Fully configurable to agency's evolving priorities |
| **Governance audit** | "The tool gave it an 82" | "Score of 82 = Metrology 4, Ontology 3, Epistemology 4, Praxeology 4, Axiology 4 — conditional approval based on Ontology gap at layer 2" |
| **Exit scenario** | Re-evaluation methodology lost when contract ends | Scoring methodology persists and is reusable |

> **Leader takeaway:** An AI intake scoring tool that cannot explain *why* a project scored as it did is a governance liability, not an asset. Ownership of the scoring logic is what makes it defensible.

---

### Use Case 3: Benefits Eligibility Determination

| Dimension | Rented Approach | Owned Approach |
|---|---|---|
| **Eligibility rules** | Vendor encodes policy as model training | Agency encodes policy as explicit, auditable rules |
| **Explanation to applicant** | "The system determined you do not qualify" | "You do not qualify under 26 CFR § X because income threshold exceeded — see verification record Y" |
| **Rule update process** | Submit request to vendor; wait for release cycle | Update owned rule configuration; version-controlled, effective immediately |
| **Appeal support** | Dependent on vendor to reproduce decision logic | Agency can reconstruct any decision from owned records |
| **Privacy compliance** | PII processed in vendor environment | PII stays in agency-controlled environment |
| **Error correction** | Vendor must identify and patch | Agency can audit, identify, and correct immediately |

> **Leader takeaway:** When a constituent appeals a benefits denial, the agency — not a vendor — must be able to explain the decision. Renting eligibility determination logic makes that impossible in practice.

---

## The Escalating Cost of Renting

Rented AI capabilities are typically cheap at the start. The cost grows over time in ways that are easy to underestimate:

| Rented Layer | Year 1 Cost | Year 3+ Risk |
|---|---|---|
| Data foundation (Metrology) | Low — vendor manages data | Migration becomes expensive; historical data may not transfer |
| Semantic model (Ontology) | Low — vendor provides schema | Changing definitions requires vendor cooperation |
| Verification layer (Epistemology) | Low — built into vendor tool | Cannot audit or challenge model outputs independently |
| Workflow logic (Praxeology) | Low — vendor-managed workflows | Governance requirements cannot be enforced |
| Values layer (Axiology) | Low — vendor provides guardrails | Compliance risk accumulates silently |

**The critical threshold:** Once you have relied on rented cognitive layers for 2–3 years, switching costs are typically prohibitive without a significant re-engineering effort. The time to make ownership decisions is at the start of procurement — not when a contract renewal gives you leverage.

---

## A Decision Framework for Procurement

Use this framework when evaluating any AI vendor proposal:

### Step 1: Map the proposal to MOEPA layers
Ask: "Which of the five layers does this product touch?"

### Step 2: Assess ownership for each layer
For each layer the product touches, ask:
- Can we export all data, definitions, and history in open formats?
- Can we reproduce any decision or output independently of the vendor?
- If this vendor disappeared, how long would it take to restore capability?

### Step 3: Classify each layer
- **Own:** Agency retains full control, portability, and audit access
- **Transitional Rent:** Acceptable short-term with an explicit migration plan
- **Avoid:** Vendor owns a layer that should belong to the agency

### Step 4: Score against the MOEPA rubric
Use the [5-Layer Evaluation Checklist](5-Layer-Evaluation-Checklist.md) to assign scores before approving funding.

### Step 5: Require contractual protections
For any rented layer that the agency has not yet moved to owned:
- Data portability clause — agency can export all data in open formats at any time
- Audit access clause — agency can inspect logs, decisions, and configurations
- Escrow clause — source code or configuration is escrowed in case of vendor failure

---

## Summary: The Strategic Rule

> **Own the brain. Rent the muscles.**

- **Brain** = Data quality rules, entity definitions, verification standards, decision workflows, and values/compliance — these are your institutional knowledge. They must be owned.
- **Muscles** = Compute, GPU capacity, pre-trained model weights, cloud storage infrastructure — these are commodity inputs. Rent freely with clean exit clauses.

A government agency that follows this rule will have AI systems it can audit, explain, defend, and migrate. An agency that inverts it will have fast, impressive tools today — and an expensive, ungovernable dependency problem in three years.

---

## Related Documents

- [5-Layer Evaluation Checklist](5-Layer-Evaluation-Checklist.md) — score any AI proposal against MOEPA
- [MOEPA 5-Layer Framework](MOEPA-5-Layer-Framework.md) — detailed per-layer leadership guide
- [Business Leader Guide](moepa-business-leaders-guide.md) — full executive handout
- [Federal Leader Guide](moepa-federal-leaders-guide.md) — government-specific guidance
