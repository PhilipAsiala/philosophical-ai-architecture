# Praxeology Scoring Guide

## Why Leaders Should Care

Praxeology determines how AI moves from analysis to action. If this layer is weak, leaders may authorize systems that take actions without adequate boundaries, approvals, rollback options, or accountability.

High risk if this layer scores below 3.

## Maturity Scale (1-5)

| Level | What It Means for Leaders | Investment Signal | Recommended Action for Governance Board |
| --- | --- | --- | --- |
| 1 | Automation is unbounded, opaque, or poorly supervised. | Unacceptable operational risk. | NO-GO for production use or delegated action authority. |
| 2 | Some workflow controls exist, but governance is inconsistent. | Limited pilot value only. | CONDITIONAL only for tightly bounded tasks with manual oversight. |
| 3 | Workflows are defined, reviewable, and governable. | Baseline viable investment. | GO for bounded operational use with clear approvals and monitoring. |
| 4 | Action pathways are strongly governed, monitored, and resilient. | Strong candidate for scaled mission operations. | GO with standard executive oversight and periodic control review. |
| 5 | Automation is mission-grade, fully auditable, and tightly aligned to policy and approvals. | Strategic operational capability. | GO and prioritize where reliable scaled execution is needed. |

## GO / CONDITIONAL / NO-GO Guidance

- Score 1-2: NO-GO for automation that changes records, triggers enforcement, or commits the organization to action.
- Score 3: CONDITIONAL GO when actions remain bounded and humans retain effective oversight.
- Score 4-5: GO for broader operational use, assuming policy and compliance controls remain active.

## Key Risks If This Layer Is Weak

- AI systems act without sufficient human review or governance.
- Errors propagate into operational systems before they are detected.
- Responsibility becomes unclear when actions are distributed across tools and workflows.
- Recovery becomes expensive or impossible because rollback and traceability are weak.

## What Good Looks Like From a Governance Perspective

- Leadership can identify what the system is allowed to do, when human approval is required, and how actions are logged.
- High-risk actions are gated by explicit policy and approval checkpoints.
- The organization can pause, review, and recover from workflow failures.
- Delegated action authority is narrow, documented, and auditable.

## Integration Dependencies Leaders Should Verify

- Epistemology must provide trustworthy inputs before action is taken.
- Axiology must define the policy and ethical boundaries for action.
- Metrology and Ontology must provide the data and context needed for safe execution.

## Recommended Questions Leaders Should Ask Proposers

- What actions can this system take without human approval?
- Where are the mandatory checkpoints, escalations, and stop conditions?
- If the workflow fails or behaves unexpectedly, how is it stopped and recovered?
- Can leadership reconstruct who approved what, when, and on what basis?
