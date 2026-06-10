# Praxeology Capabilities

## What Leaders Need to Know

Bottom line: this layer governs how AI turns into action. It helps leaders decide where automation is appropriate, where human approval is mandatory, and where operational risk is too high.

See [ARCHITECTURE.md](../../ARCHITECTURE.md) for the strategic rationale and [Business Value](../../docs/business-value.md) for the investment lens.

## Mission and Governance Outcomes

- Predictable automation with auditable approvals and actions.
- Lower operational risk from bounded, reviewable workflows.
- Better oversight of where AI is allowed to act versus merely advise.
- Greater ownership of workflow logic instead of hiding it inside vendor tools.

## Capability Matrix

The matrix below binds the minimum set of Praxeology capabilities to **Score 3 — Defined & Contained — Minimum Acceptable Standard** in the existing [Praxeology scoring guide](scoring.md). Capabilities that contribute to Scores 4 and 5 lift the layer beyond that baseline. Live delivery status should be tracked through the [Praxeology workflow](tools.md); the JIRA epic column below is illustrative only.

| Capability | Minimum set? (Score 3) | Maturity contribution (3 / 4 / 5) | Owner | Delivery tracking (illustrative: JIRA epic) |
| --- | --- | --- | --- | --- |
| Agent frameworks for goal-oriented execution | No | 4 — provides a reusable control plane for multi-step automation | Automation platform owner | Illustrative: JIRA epic for agent orchestration platform |
| Workflow automation for repeatable business operations | Yes | 3 — establishes defined and reviewable operational flows | Workflow owner | Illustrative: JIRA epic for repeatable workflow automation |
| Decision engines combining rule-based and AI recommendations | Yes | 3 — keeps actions bounded by explicit decision logic | Decision workflow owner | Illustrative: JIRA epic for hybrid decision services |
| Action orchestration and goal decomposition across multi-step plans | Yes | 3 / 4 — supports governable multi-step execution and lifts maturity when standardized | Workflow owner | Illustrative: JIRA epic for orchestration and goal decomposition |
| Real-time execution controls with human-in-the-loop checkpoints | Yes | 3 / 4 / 5 — mandatory checkpoints satisfy the minimum, while stronger runtime controls and approvals lift higher | Operations control owner | Illustrative: JIRA epic for approvals, checkpoints, and stop conditions |
| Process optimization using telemetry and feedback loops | No | 4 / 5 — improves resilience and scaled operational performance | Process improvement owner | Illustrative: JIRA epic for workflow telemetry and optimization |

## Questions Leaders Should Ask Before Funding

- What actions can this system take without human approval?
- Where are the mandatory checkpoints, escalation paths, and stop conditions?
- Can leadership reconstruct who approved what, when, and on what basis?
- If the workflow fails, can it be paused, rolled back, and reviewed safely?
