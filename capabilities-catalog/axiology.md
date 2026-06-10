# Layer 5 — Axiology: Values, Ethics, and Mission Alignment

> **Core principle:** AI systems must embody and enforce the values, legal constraints, and mission priorities of the organization — and those constraints must be hard-coded at the infrastructure level, not soft guidelines that can be worked around.

---

## What Axiology Covers

| Capability Domain | Description |
|---|---|
| **Policy enforcement** | Translating laws, regulations, and agency policy into technical constraints |
| **Guardrail implementation** | Hard limits on what the system can and cannot do |
| **Constitutional AI design** | Principles that the system must never violate regardless of instructions |
| **Compliance monitoring** | Continuously verifying that the system operates within defined boundaries |
| **Value alignment testing** | Regularly testing that guardrails work as intended |
| **Mission priority governance** | Ensuring AI optimization objectives align to agency mission |

---

## Core Capabilities

### A1 — Policy-as-Code Enforcement
**What it does:** Translates agency policy, legal requirements, and compliance mandates into explicit, machine-enforceable rules — not just documentation or prompt instructions.

**Why it matters for government:** A prompt instruction like "do not share PII" can be bypassed by a sophisticated user or an edge-case input. A policy-as-code rule that blocks PII from being included in any outbound response cannot. The difference between soft and hard enforcement is the difference between a policy that applies in all cases and one that applies in most.

**Minimum acceptable standard (Score 3):** Key compliance requirements encoded as enforceable rules; violations blocked.

**Good practice (Score 4–5):** All statutory and regulatory constraints encoded as versioned, auditable policy code; enforcement at infrastructure level (not application logic); policy changes go through formal review.

---

### A2 — Constitutional Guardrails (Inviolable Constraints)
**What it does:** Defines a set of constraints that the system must never violate regardless of instructions, context, or prompt engineering — and enforces those constraints at a layer the system itself cannot override.

**Why it matters for government:** Constitutional guardrails are the equivalent of statutory limits that no employee, manager, or executive can waive. For AI systems, this means constraints like: never disclose PII without authorization, never process data outside the authorized environment, never take an action that waives a citizen's legal rights.

**Minimum acceptable standard (Score 3):** Inviolable constraints documented; enforced at application level.

**Good practice (Score 4–5):** Inviolable constraints enforced at OS/infrastructure level; enforcement tested regularly with adversarial inputs; constraints version-controlled and change-managed; enforcement logs available for audit.

---

### A3 — Prompt Injection Defense
**What it does:** Detects and blocks attempts by users or external data sources to use carefully crafted inputs to override the system's instructions or bypass its constraints.

**Why it matters for government:** Prompt injection is the leading attack vector against AI systems. An attacker who can inject instructions into a document the AI reads, or into data the AI retrieves, may be able to cause the AI to take unauthorized actions or disclose protected information.

**Minimum acceptable standard (Score 3):** Basic input sanitization; known injection patterns blocked; suspicious inputs flagged.

**Good practice (Score 4–5):** Multi-layer injection defense (input sanitization, context separation, output validation); injection attempts logged and alerted; regular red-team testing; context integrity verified before execution.

---

### A4 — Mission Alignment Configuration
**What it does:** Maintains a versioned, approved configuration of the AI system's objectives, priorities, and optimization targets — aligned to agency mission and reviewed regularly.

**Why it matters for government:** AI systems optimize for their defined objectives. If those objectives are set by a vendor ("maximize engagement," "minimize latency"), they may not align to agency mission ("maximize accuracy and equity," "minimize processing errors for vulnerable populations"). Mission alignment configuration makes the optimization target explicit and owned.

**Minimum acceptable standard (Score 3):** System objectives documented and approved; reviewed periodically.

**Good practice (Score 4–5):** Mission alignment formally encoded in system configuration; objectives reviewed against mission and statutory requirements on a defined schedule; changes require leadership approval; alignment testing included in deployment validation.

---

### A5 — Bias and Equity Monitoring
**What it does:** Monitors AI outputs for systematic disparities across demographic, geographic, or population groups — and triggers review when disparities exceed defined thresholds.

**Why it matters for government:** Government agencies are subject to equal protection and anti-discrimination requirements. An AI system that systematically produces different outcomes for different demographic groups — even unintentionally — creates legal and mission risk. Monitoring is the only way to detect this before it causes harm at scale.

**Minimum acceptable standard (Score 3):** Periodic bias audits for high-stakes decision workflows; results reviewed.

**Good practice (Score 4–5):** Continuous equity monitoring across defined demographic dimensions; automated alerting when disparities exceed thresholds; monitoring results publicly reportable; remediation process defined.

---

### A6 — Value Alignment Testing
**What it does:** Regularly tests the system with boundary cases, adversarial inputs, and edge conditions designed to reveal whether guardrails are working as intended.

**Why it matters for government:** Guardrails that have never been tested are wishful thinking. Regular red-team testing — including tests designed by people trying to break the system — is the only way to validate that constraints hold under real-world pressure.

**Minimum acceptable standard (Score 3):** Periodic testing of key guardrails; results documented and reviewed.

**Good practice (Score 4–5):** Scheduled red-team testing; adversarial test suite version-controlled alongside system; test results reviewed by governance board; failures trigger formal remediation.

---

## Recommended Tools

### Self-Hosted / Open Source (Preferred)

| Tool | Category | Description |
|---|---|---|
| **Open Policy Agent (OPA)** | Policy enforcement | Open-source policy engine; enforces rules as versioned, auditable Rego code |
| **Guardrails AI** | Output constraint enforcement | Open-source framework for defining and enforcing output structure and content constraints |
| **LLM Guard** | Security and safety | Open-source library for scanning LLM inputs and outputs for security risks |
| **Rebuff** | Prompt injection detection | Open-source prompt injection detection and defense library |
| **Giskard** | AI testing and red-teaming | Open-source AI quality testing including bias detection and adversarial testing |
| **Fairlearn** | Fairness / bias measurement | Open-source toolkit for assessing and mitigating AI fairness issues |
| **AI Fairness 360 (AIF360)** | Bias detection | IBM open-source toolkit for measuring and mitigating dataset and model bias |
| **Conftest** | Policy testing | Open-source tool for testing configurations against OPA policies |
| **Trivy** | Security scanning | Open-source vulnerability scanner for containers, code, and configs |

### Deployment Notes

- **For policy enforcement:** OPA is the standard for policy-as-code in government and enterprise contexts; integrates with Kubernetes, API gateways, and CI/CD pipelines
- **For output safety:** Guardrails AI and LLM Guard can be run in-process with the AI system pipeline; no external service required
- **For prompt injection:** Rebuff is lightweight and easily integrated; combine with input sanitization and context separation
- **For bias monitoring:** Fairlearn (Microsoft) and AIF360 (IBM) are both open-source and well-documented; suitable for government use

---

## Patterns

### Pattern A-A: Constitutional Layer Wrapper
Wrap all AI inference calls in a constitutional layer that evaluates both the input and output against inviolable constraints before either enters the system or reaches the user. The constitutional layer is a separate service that cannot be bypassed by the inference pipeline.

```
User Input → Constitutional Input Filter → Inference Engine
                     ↓ (blocked if violates constraints)
                 Violation Log + Alert

Inference Output → Constitutional Output Filter → User
                          ↓ (blocked if violates constraints)
                      Violation Log + Alert + Human Escalation
```

### Pattern A-B: Policy Versioning with Effective Dates
All policy-as-code configurations include an effective date and an expiry date. Before executing any workflow, the system retrieves the policy version that was active at the time of the initiating event — not just the current policy. This enables correct handling of decisions made under superseded policy.

### Pattern A-C: Equity Monitoring Baseline
At deployment, compute a baseline output distribution across demographic and geographic dimensions for the intended population. Set alerting thresholds at ±2 standard deviations from baseline. Review triggered when any dimension crosses the threshold. Baseline reviewed and updated annually.

---

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| Guardrails only in system prompt | Bypassable by sophisticated prompt engineering | "Our guidelines are embedded in the instructions we give the model" |
| No testing of guardrails | Guardrails may not work under real conditions | "We haven't done adversarial testing" |
| Vendor defines compliance controls | Agency cannot verify or modify constraints | "Compliance is handled by the platform's built-in features" |
| No bias monitoring | Systematic inequity undetected | "We haven't measured outcomes across demographic groups" |
| Policy not version-controlled | Cannot reconstruct which rules were active for a historical decision | "We updated the policy guidelines last quarter" |

---

## Related Capabilities

- **Praxeology (Layer 4):** Axiology constraints are enforced within Praxeology workflows — certain actions are blocked regardless of workflow state. Axiology defines the outer boundary; Praxeology operates within it.
- **Epistemology (Layer 3):** Fact verification results feed into Axiology monitoring — if the verification layer detects systematic errors affecting specific populations, Axiology equity monitoring should detect the downstream pattern.
- **Data Substrate:** Policy configurations, guardrail test results, equity monitoring records, and compliance audit logs are all stored in the Data Substrate with version history.
