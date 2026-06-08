# Metrology Scoring Guide

## Why Leaders Should Care

Metrology determines whether leadership is making AI investment decisions on a trustworthy data foundation. If this layer is weak, the organization is exposed to poor data quality, weak auditability, compliance gaps, and long-term vendor dependency.

High risk if this layer scores below 3.

## Maturity Scale (1-5)

| Level | What It Means for Leaders | Investment Signal | Recommended Action for Governance Board |
| --- | --- | --- | --- |
| 1 | Data is fragmented, poorly governed, and difficult to trust. | Do not scale. Foundational weakness will contaminate higher-layer investment. | NO-GO for production or enterprise funding. Require data governance remediation first. |
| 2 | Some controls exist, but they are inconsistent and not sufficient for regulated use. | Limited pilot value only. Risk remains elevated. | CONDITIONAL only for tightly bounded experiments with remediation plan. |
| 3 | Data governance is defined, repeatable, and suitable for controlled operational use. | Baseline viable investment. | CONDITIONAL GO if higher layers are also acceptable and oversight is in place. |
| 4 | Data operations are well governed, measurable, and audit-ready. | Strong investment candidate. | GO with normal governance oversight and periodic review. |
| 5 | Data is sovereign, portable, and fully defensible for high-trust mission use. | Strategic asset. | GO and prioritize as a model for reuse across programs. |

## GO / CONDITIONAL / NO-GO Guidance

- Score 1-2: NO-GO for enterprise deployment. Consider only narrow pilots with explicit remediation and leadership approval.
- Score 3: CONDITIONAL GO if data quality, lineage, and access controls are stable enough for the mission context.
- Score 4-5: GO for broader operational use, subject to normal compliance and oversight processes.

## Key Risks If This Layer Is Weak

- Decisions are made on incomplete, inaccurate, or poorly governed data.
- Audit, transparency, and records-management requirements become difficult to satisfy.
- Downstream ontology, retrieval, and automation investments inherit avoidable risk.
- The organization becomes dependent on vendor-controlled storage, metadata, or lineage systems.

## What Good Looks Like From a Governance Perspective

- Leadership can identify where critical data came from, who can access it, and how it changed over time.
- Sensitive data is governed through clear access boundaries and policy controls.
- Data quality is measured and acted on before high-impact use.
- The organization retains control of core data assets, metadata, and historical traceability.

## Integration Dependencies Leaders Should Verify

- Ontology depends on clean, versioned, and governed source data.
- Epistemology depends on trustworthy provenance and retrievable evidence.
- Axiology depends on access control, privacy boundaries, and retention discipline.

## Recommended Questions Leaders Should Ask Proposers

- What evidence shows the source data is accurate, governed, and suitable for this use case?
- If auditors ask where a result came from, can the team show the full lineage?
- What happens if the current data provider or platform is removed or changed?
- How are data quality failures surfaced, escalated, and blocked from downstream use?
