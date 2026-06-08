# Praxeology Patterns and Anti-Patterns

## Why These Patterns Matter to Leaders

Weak action patterns create operational risk quickly. They lead to automation that is difficult to stop, difficult to explain, and difficult to assign responsibility for when something goes wrong.

## Durable Governance Patterns

- State Machine First: every workflow step has explicit transitions
- Policy Gate Checkpoints: evaluate compliance before sensitive actions
- Human Approval Escalation: mandatory intervention for high-risk outcomes
- Idempotent Tool Wrappers: retry-safe operations with audit identifiers

## Costly Patterns to Avoid

- Open-ended autonomous loops with unrestricted tool access
- Workflow logic split across prompts and undocumented scripts
- Human review configured but bypassable in production
- No rollback path for multi-step side effects

## What Leaders Should Watch For

- State desynchronization between orchestrator and tool systems
- Approval bottlenecks due to poor risk segmentation
- Excessive automation of decisions that require policy interpretation

See [Business Value](../../docs/business-value.md) and [ARCHITECTURE.md](../../ARCHITECTURE.md) for why controlled execution is part of long-term institutional ownership.
