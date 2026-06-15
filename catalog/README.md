# MOEPA Catalog

The MOEPA Catalog is the routing and governance catalog inside the Philosophical AI Architecture. It helps leaders set priorities, evaluate AI proposals, manage risk, ensure sovereignty, and make GO, CONDITIONAL, or NO-GO investment decisions using the MOEPA 5-Layer Framework scoring model. Federal intake requires leaders to prove catalog enrichment — black-box vendor solutions that cannot map to the catalog fail by design.

It also serves technical architects, program managers, and designers by providing detailed capability descriptions, recommended self-hosted and open tools, proven patterns, and cross-layer compositions — all organized by the five MOEPA layers plus the Data Substrate foundation.

Rather than treating AI as a collection of disconnected tools, the catalog provides a structured way to decide which capabilities should be funded, governed, scaled, deferred, or rejected. Its purpose is to support mission alignment, risk reduction, compliance, auditability, business value, and long-term ownership of cognitive assets.

## Strategic Context

This catalog should be read alongside the core [architecture rationale](../ARCHITECTURE.md) and the [business value case](../docs/business-value.md). Together, those documents explain why the MOEPA model exists, while this catalog helps leadership decide where to invest, what to govern tightly, and what to stop early.

## How Leaders and Teams Should Use This Catalog

**Executives, governance boards, and priority setters** use this catalog to:
- Evaluate whether an AI proposal advances mission outcomes and business value
- Determine whether the proposal strengthens or weakens institutional sovereignty
- Identify compliance, audit, privacy, and operational risks before funding decisions are made
- Compare competing initiatives using a common maturity and governance lens
- Build long-term institutional capability instead of approving isolated, vendor-dependent pilots

**Technical architects, program managers, and designers** use this catalog to:
- Understand the concrete capabilities expected at each layer for a well-governed system
- Evaluate sovereignty, portability, and vendor-dependency trade-offs when selecting tools
- Adopt proven patterns and avoid common failure modes
- Design and compose capabilities across layers (see cross-layer compositions)

## Why This Exists

The catalog helps leadership teams move from abstract AI ambition to disciplined governance and priority-setting:
- Evaluate new AI proposals using a common governance framework
- Score maturity by layer before funding, procurement, or deployment
- Test whether a proposal preserves sovereignty and reduces vendor dependency
- Surface patterns that improve auditability, safety, and oversight
- Build durable institutional capability instead of fragmented tool sprawl

## How To Use This Catalog

1. Start with the layer README to understand what decision domain is being evaluated.
2. Use **capabilities** to determine whether a proposal addresses a real institutional need and what "good" looks like.
3. Use **tools** to assess sovereignty, portability, and vendor dependency trade-offs (prefer self-hosted/open).
4. Use **patterns** to recognize durable approaches and avoid repeat governance failures.
5. Use **scoring** to assign maturity, identify gaps, and determine remediation requirements.
6. Use **examples** (per layer and the scenario walkthroughs in ../examples/) to understand what concrete governed assets or controls may be required.
7. Use **cross-layer compositions** for multi-layer patterns that emerge in real government use cases.

## Navigation

- [Capability Matrix](capability-matrix.md) — minimum baseline for Score 3 across all layers
- [Cross-Layer Compositions](cross-layer-compositions.md) — how layers work together
- [Metrology](metrology/README.md) — data quality, measurement, provenance
- [Ontology](ontology/README.md) — structured knowledge and meaning
- [Epistemology](epistemology/README.md) — truth, verification, and accountability
- [Praxeology](praxeology/README.md) — decision workflows and human oversight
- [Axiology](axiology/README.md) — values, ethics, and mission alignment

## Intake and Scoring Workflow

This workflow should be used as a governance and priority-setting process for executive review boards. It is designed to scale to high volumes (1,000+ requests) while enforcing demand management, cost discipline, and formal architecture governance.

1. Map the proposal to one or more core capabilities in each layer.
2. Use the [Capability Matrix](capability-matrix.md) to identify the Score 3 minimum-set baseline and the capabilities that raise maturity toward 4 and 5.
3. **Demand Management Check (Deduplication):** Search the MOEPA Catalog and the enterprise Ontology/knowledge graph to confirm that the proposed solution, data model, or infrastructure does not duplicate an existing approved capability elsewhere in the enterprise. Record the search results and any related assets.
4. Assess current maturity using each layer scoring rubric, with particular attention to Axiology weighting for Business ROI and approved chargeback/showback models.
5. Flag gaps scoring below level 3 and define remediation.
6. Link delivery work to the [Praxeology workflow](praxeology/tools.md) so live status is tracked in execution systems rather than in the catalog.
7. Execute the formal Architecture Review Chain (AAP → EDP Pipelines → EDP Platform → Customer / Business Teams) and obtain documented sign-off at each step.
8. Confirm integration dependencies between adjacent layers.
9. Record ownership metadata, controls, ROI quantification, and cost model in the catalog.
10. For any proposal achieving an overall score of 4 or higher (or requesting production resources), secure formal Executive Approval through the executive gate, confirming weighted ROI, chargeback model, deduplication clearance, and completion of the Architecture Review Chain.
11. Schedule the mandatory post-launch KPI measurement and baselining review (tied to Metrology controls).
12. Present a GO, CONDITIONAL, or NO-GO recommendation to governance reviewers.

## Governance Notes

Leadership should treat this catalog as an oversight instrument, not just a reference library. It is intended to inform funding decisions, architecture review, procurement scrutiny, and ongoing governance.

- Prefer sovereign, self-hosted, and open-standard approaches where practical, especially for high-impact or regulated workloads.
- Treat vendor-hosted capabilities as transitional unless ownership, exportability, and control boundaries are explicit.
- Require lineage, provenance, and audit evidence for high-risk workflows and decisions.
- Align final decisions with mission outcomes, compliance obligations, NIST-aligned governance practices, and business value.
- Use low scores as indicators of governance debt, not merely technical incompleteness.
- Favor investments that compound institutional capability over one-off tools that create dependency without durable ownership.

## Leadership Outcome

Used correctly, the catalog helps leaders fund the right AI initiatives, stop the wrong ones early, reduce operational and compliance risk, and steadily build an owned cognitive layer that remains governable, portable, and aligned to organizational mission.
