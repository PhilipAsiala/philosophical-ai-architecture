# Pitch Strategy: The Philosophical AI Architecture

> **Repository directive.** Every document, diagram, and architectural decision in this repository must serve this narrative. Use this guide when writing, reviewing, or presenting any material derived from the repo.

---

## 0. Business First

**Lead with business outcomes, not technology.** MOEPA is named after philosophical disciplines because leaders must be able to describe what the organization needs — trusted data, shared meaning, verifiable truth, governed action, and enforced values — before anyone names a tool, protocol, or platform.

| Rule | What it means |
|---|---|
| **Disciplines describe outcomes** | Metrology = trusted measurement. Ontology = shared reality. Epistemology = defensible truth. Praxeology = accountable action. Axiology = enforced values. |
| **Leaders ask ownership questions** | Every layer reduces to: *Do we own this outcome, or does a vendor?* |
| **Technology follows** | Stack choices, protocols, and implementation patterns belong in builder documents — not executive briefings, leader guides, or the README's primary narrative. |
| **One vocabulary per audience** | Executives hear mission, risk, auditability, and ROI. Architects hear substrates, interfaces, and catalogs. Never mix the two in the same paragraph. |

### Document tiers

| Tier | Audience | Lead with | Technical depth |
|---|---|---|---|
| **Leader-facing** | Executives, program managers, acquisition | Business outcomes per MOEPA layer; ownership questions; use-case walkthroughs | None in body copy — link to builder tier |
| **Builder-facing** | Architects, engineers, reviewers | Engineering translation of each layer; substrate end state; tool patterns | Full — `ARCHITECTURE.md`, governance guidelines, catalog tools |
| **Contributor** | Doc authors, RFC proposers | Pitch strategy + business-first test before adding technical detail | Scoped to the tier being edited |

If a leader-facing document mentions MCP, RAG, Iceberg, LangGraph, or similar before stating the business outcome that layer protects, rewrite it.

---

## 1. The Core Mindset

**The industry blind spot:** The market obsesses over the *Artificial* — infrastructure, compute, LLMs — and treats *Intelligence* as an uncontrollable black box.

**Our solution:** We open the black box. We decode Intelligence by mapping human cognitive functions into strict, governable software:

| Function | What it is | MOEPA expression |
|---|---|---|
| **Cognition** (knowing) | How the system defines and verifies reality | Metrology, Ontology, Epistemology |
| **Affect** (valuing) | How the system encodes what matters and what is forbidden | Axiology |
| **Conation** (acting) | How the system executes decisions under human oversight | Praxeology |

**Philosophy vs. psychology in the stack:**

- **Philosophy** is the operating system — the strict logical rules for defining reality and truth (Metrology, Ontology, Epistemology).
- **Psychology** is the mechanics of behavior — how values and execution drives steer the cognitive engine (Axiology, Praxeology).

**The mission:** We do not build black boxes. We build auditable, institutional brains.

---

## 2. Strict Terminology

Never conflate the overarching system with the operational tool.

| Term | What it is | When to use it |
|---|---|---|
| **Philosophical AI Architecture** | The overarching enterprise ecosystem: Data Substrate, MOEPA Catalog, security guardrails, own-vs-rent strategy, and cognitive control plane | Pitching the whole system; README; strategic docs |
| **MOEPA 5-Layer Framework** | The operational engineering blueprint and governance engine *inside* the architecture: five layers, intake scoring, GO / CONDITIONAL GO / NO-GO rubric | Engineering translation; project intake; layer-by-layer evaluation |
| **MOEPA Cognitive Architecture** | The technical stack specification: storage mapping, catalog integration, recommended tools, implementation playbook | `ARCHITECTURE.md`; architects and builders |
| **Data Substrate** | The organization-owned knowledge library — truth, values, rules, and lineage in open formats | Always a physical metaphor; never a "vendor database" |
| **MOEPA Catalog** | The routing and governance catalog — discoverability, deduplication, versioning, intake evidence | Enterprise and public sector intake lever; demand management |

---

## 3. Pitching the Technical Team (The Builders)

**The hook:** Validate their mastery of the Artificial. Challenge them to engineer the Intelligence.

**The translation:** Map human sciences directly to system architecture.

| MOEPA layer | Scientific anchor | Engineering translation |
|---|---|---|
| **Metrology** | Measurement | Telemetry, audit trails, performance scoring |
| **Ontology** | Domain / reality | Knowledge graphs, approved vocabularies, data models |
| **Epistemology** | Truth | Evidence mapping, RAG validation, authoritative source indexing |
| **Praxeology** | Action | Digitized SOPs, workflows, agentic execution playbooks |
| **Axiology** | Values / rules | Encoded guardrails, access controls, NIST-aligned compliance |

Introduce the **MOEPA 5-Layer Framework** as their engineering blueprint — not a presentation-layer abstraction, but the control plane for how institutional knowledge is classified, stored, verified, acted on, and governed.

---

## 4. Pitching Enterprise Leadership (The Buyers)

**The hook:** Vendors sell compelling demos. Your organization needs a framework that separates what you must own from what you can rent.

**The governance lever:** Position the **MOEPA 5-Layer Framework** as the organization's go/no-go project intake rubric. Leaders must prove how each proposal enriches the **MOEPA Catalog**. Black-box vendor solutions that cannot map to all five layers are rejected by design.

**The own-vs-rent strategy:** The organization permanently owns the **Data Substrate** — the truth, the values, the rules. Rent commercial LLMs and compute. Zero vendor lock-in on institutional knowledge.

**Primary guide:** [Business Leader Guide](moepa-business-leaders-guide.md)

---

## 5. Pitching Public Sector Leadership (Federal, State, and Local)

**The hook:** You cannot govern an AI mind with standard IT infrastructure metrics. You need a **cognitive control plane**.

**The governance lever:** Position the **MOEPA 5-Layer Framework** as the organization's go/no-go project intake rubric. Area leaders must prove how their project enriches the **MOEPA Catalog**. Black-box vendor solutions that cannot map to all five layers are rejected by design.

**The own-vs-rent strategy:** The institution permanently owns the **Data Substrate** — the truth, the values, the rules. Rent commercial LLMs and compute. Zero vendor lock-in. Total data sovereignty. Immunity to model churn.

**End state vs. evolution:** The organization must eventually own a single, auditable knowledge library (the Data Substrate) that every layer reads from and writes to. Public institutions get there incrementally — starting with what they have, documenting the path, and refusing new vendor silos. Technical storage targets belong in builder conversations; leaders hear *ownership, portability, and audit lineage*.

**Primary guide:** [Public Sector Leader Guide](moepa-public-sector-leaders-guide.md)

---

## 6. Golden Rules of Tone and Execution

- **Business first:** State the outcome each MOEPA layer protects before any implementation detail. If the reader is a leader, stop when the ownership question is answered.
- **Voice:** Punchy, authoritative, direct. Executive-to-executive for leaders; engineer-to-engineer only in builder-tier documents.
- **Clarity:** Ground abstract philosophy in physical metaphors — Data Substrate, Control Plane, Management Lever, Catalog.
- **Actionable output:** Leader guides and examples must show how philosophical disciplines translate into defensible business decisions — not tool selections.
- **Technical containment:** MCP, semantic ingestion, and substrate storage patterns belong in `ARCHITECTURE.md`, governance guidelines, and catalog **tools** — not in README intros, leader handouts, or executive summaries.
- **Confidence:** Present the Philosophical AI Architecture as the necessary future of secure enterprise AI — not an academic thought experiment.

---

## 7. Architectural Evolution (Builders Only)

When describing implementation paths, align with the
[Architectural Governance and Evolution Guidelines](MOEPA-Architectural-Governance-and-Evolution-Guidelines.md):

| Principle | Pitch to builders |
|---|---|
| Governance over abstraction | MCP is the integration layer — not Bedrock-native tooling or LangChain glue |
| Fragments to semantic objects | Docling/Unstructured-style parsing produces Proto-SPOs with provenance, not naive chunks |
| MOEPA standard | Every feature scores across all five layers with exact citations where evidence is claimed |
| MCP-first pattern | Data and RAG access live in MCP servers; legacy APIs get MCP facades |

---

## Related Documents

- [Business Value](business-value.md) — investment case in business-outcome terms
- [Glossary](glossary.md) — canonical term definitions
- [MOEPA 5-Layer Framework for Leaders](MOEPA-5-Layer-Framework.md) — per-layer leadership questions
- [Architectural Governance and Evolution Guidelines](MOEPA-Architectural-Governance-and-Evolution-Guidelines.md) — MCP-first evolution rules and PR gate
- [Business Leader Guide](moepa-business-leaders-guide.md) — enterprise intake and ownership pitch
- [Public Sector Leader Guide](moepa-public-sector-leaders-guide.md) — government intake and accountability pitch
- [Own vs. Rented AI Strategy](Owned-vs-Rented-AI-Strategy.md) — own substrate, rent compute
- [MOEPA Cognitive Architecture Spec](../ARCHITECTURE.md) — technical implementation