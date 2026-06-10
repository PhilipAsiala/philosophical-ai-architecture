# Layer 4 — Praxeology: Decision Workflows and Human Oversight

> **Core principle:** AI systems that can take actions must operate within defined, auditable workflows with guaranteed human oversight checkpoints. Praxeology capabilities govern how the system acts — what it can do, in what sequence, who approves each step, and how every action is recorded.

---

## What Praxeology Covers

| Capability Domain | Description |
|---|---|
| **Workflow definition and enforcement** | Defining and enforcing the sequence of steps for any consequential action |
| **State machine governance** | Tracking workflow state so nothing can skip steps or run out of sequence |
| **Human-in-the-loop controls** | Ensuring human review at defined decision points before consequential actions |
| **Audit trail generation** | Creating an immutable record of every workflow execution |
| **Tool scope enforcement** | Limiting what actions an AI agent can take to its defined scope |
| **Escalation and exception handling** | Governing what happens when automated processing cannot complete |

---

## Core Capabilities

### P1 — Deterministic Workflow State Machine
**What it does:** Represents each workflow as an explicit state machine — a defined set of states, transitions, and conditions. The system can only move between defined states in defined ways; no transitions are possible outside the state machine.

**Why it matters for government:** "Agentic" AI that follows instructions step-by-step with no formal state model can get into undefined states — doing things it wasn't intended to do, or skipping steps that were required. A state machine makes workflows provably correct and auditable.

**Minimum acceptable standard (Score 3):** Workflows documented with required steps; execution follows defined sequence.

**Good practice (Score 4–5):** Formal state machine implementation; transitions logged at each state change; state model version-controlled; impossible to skip required states.

---

### P2 — Human-in-the-Loop Checkpoints
**What it does:** Defines mandatory pause points in workflows where a human must review the situation and explicitly approve before the system can proceed. These checkpoints cannot be bypassed by the system or by prompt engineering.

**Why it matters for government:** Automated AI systems making consequential decisions about citizens — issuing notices, updating records, triggering audits — must have defined points where a responsible official reviews and approves. This is not just a governance preference; it is a legal and due process requirement in many government contexts.

**Minimum acceptable standard (Score 3):** Human review required before any externally visible action; approval logged.

**Good practice (Score 4–5):** Checkpoint enforcement at the infrastructure level (not just application logic); bypassing a checkpoint produces a system error; approver identity and timestamp recorded in immutable log.

---

### P3 — Agent Scope Enforcement (Tool Boundaries)
**What it does:** Explicitly defines what actions an AI agent is authorized to take — what tools it can call, what systems it can write to, what data it can access — and prevents any action outside that scope.

**Why it matters for government:** Agentic AI systems are given access to tools (database updates, API calls, document generation, communication systems). Without explicit scope enforcement, a model could take unintended actions based on ambiguous instructions. Scope enforcement is the "blast radius" limiter.

**Minimum acceptable standard (Score 3):** Documented list of authorized agent actions; unauthorized actions blocked.

**Good practice (Score 4–5):** Tool scope enforced at the infrastructure level; unauthorized action attempts logged and alerted; scope changes require formal review and approval.

---

### P4 — Immutable Workflow Audit Log
**What it does:** Records every workflow event — state transitions, tool calls, human approvals, exceptions — in a tamper-evident log with timestamp and actor identity.

**Why it matters for government:** The workflow audit log is the evidentiary record for investigations, appeals, oversight inquiries, and compliance audits. It must be complete, accurate, and impossible to alter after the fact.

**Minimum acceptable standard (Score 3):** Workflow events logged; log retained per policy; accessible for audit review.

**Good practice (Score 4–5):** Cryptographically signed log entries; append-only storage; every event includes actor identity, timestamp, state before/after, and context reference; log immutable after write.

---

### P5 — Feedback and Adaptation Controls
**What it does:** Defines how workflow logic is updated based on outcomes — and controls that process so changes go through review rather than happening automatically.

**Why it matters for government:** Systems that learn and adapt need governance over how they adapt. An AI that autonomously changes its decision logic based on feedback could silently drift from its approved behavior. Adaptation must be a controlled, reviewed process.

**Minimum acceptable standard (Score 3):** Workflow logic changes go through documented review; changes are version-controlled.

**Good practice (Score 4–5):** Formal change control process for all workflow modifications; approved changes tested before deployment; previous versions archived and retrievable.

---

### P6 — Escalation and Exception Handling
**What it does:** Defines what happens when a workflow cannot be completed automatically — insufficient evidence, conflicting signals, boundary conditions. Escalation paths are explicit, logged, and governed.

**Why it matters for government:** The edge cases are where errors concentrate. A workflow that handles 95% of cases automatically but has no defined process for the remaining 5% will produce unpredictable outcomes for the citizens in that 5%.

**Minimum acceptable standard (Score 3):** Exception conditions documented; escalation path defined; exceptions logged.

**Good practice (Score 4–5):** Automated escalation routing based on exception type; escalation outcomes tracked; exception patterns reviewed regularly to improve workflow coverage.

---

## Recommended Tools

### Self-Hosted / Open Source (Preferred)

| Tool | Category | Description |
|---|---|---|
| **LangGraph** | Agentic state machine | Open-source library for building stateful, graph-based agentic workflows; supports cycles and human-in-the-loop |
| **Apache Airflow** | Workflow orchestration | Open-source platform for authoring, scheduling, and monitoring data workflows |
| **Prefect** | Workflow orchestration | Modern open-source workflow orchestration with observability and state tracking |
| **Temporal** | Durable workflow engine | Open-source platform for long-running, reliable workflow execution with replay capability |
| **n8n** | Visual workflow builder | Open-source, self-hostable workflow automation with approval gates |
| **Camunda** | BPMN process engine | Open-source BPMN-based process management; strong governance and audit features |
| **OpenFGA / Zanzibar** | Fine-grained authorization | Open-source relationship-based access control; enforces tool scope at authorization layer |
| **Open Policy Agent (OPA)** | Policy enforcement | Open-source policy engine; enforces workflow and access policies as code |

### Deployment Notes

- **For agentic AI workflows:** LangGraph is the leading open-source tool specifically designed for stateful, human-in-the-loop agentic workflows
- **For enterprise process governance:** Camunda is mature and widely used in government contexts; strong BPMN support
- **For policy enforcement:** OPA (Open Policy Agent) can enforce tool scope and action permissions as versioned, auditable policy code
- **For long-running workflows:** Temporal is best for workflows that span hours, days, or longer and must survive system restarts

---

## Patterns

### Pattern P-A: Human Gate State
Every consequential workflow includes at least one `PENDING_HUMAN_REVIEW` state. The workflow cannot transition from this state to `APPROVED` or `ESCALATED` except through an explicit human action. Timeout in the `PENDING_HUMAN_REVIEW` state escalates automatically — it never auto-approves.

```
INITIATED → EVIDENCE_GATHERING → PENDING_HUMAN_REVIEW → [APPROVED | ESCALATED | REJECTED]
                                        ↑
                               Human action required
                               Timeout → ESCALATED (never auto-approved)
```

### Pattern P-B: Tool Call Authorization
Before any tool call, the agent checks an authorization policy: is this agent permitted to call this tool in this workflow state, for this entity type, with these parameters? Unauthorized calls are blocked and logged, not silently skipped.

### Pattern P-C: Immutable Workflow Snapshot
At each state transition, the full workflow context — current state, input data references, evidence references, confidence scores, approver identity, timestamp — is written as an immutable snapshot to the Data Substrate. This snapshot is the basis for any future audit or reproduction of the decision.

---

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| No formal state machine | Workflow can get into undefined states | "It's just a sequence of API calls" |
| Human checkpoints bypassable | High-stakes decisions happen without review | "We have a review step but it can be skipped in urgent cases" |
| Agent has broad tool access | Unintended actions take place | "The agent has access to whatever it needs" |
| Audit log is editable | Compliance and evidentiary integrity at risk | Logs stored in standard database without append-only enforcement |
| No escalation path | Edge cases produce unpredictable outcomes | "If the system can't decide, it just returns an error" |

---

## Related Capabilities

- **Epistemology (Layer 3):** Praxeology receives verified evidence and confidence scores from Epistemology before initiating action. Confidence band determines whether workflow proceeds automatically or requires human review.
- **Axiology (Layer 5):** Axiology's policy constraints are enforced at the Praxeology layer — certain actions are prohibited regardless of workflow state or human approval.
- **Data Substrate:** All workflow state, audit records, and escalation events are written to the Data Substrate as immutable records.
