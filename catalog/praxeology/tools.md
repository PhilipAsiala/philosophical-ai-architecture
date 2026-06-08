# Praxeology Tools

## Executive Summary

These tool categories matter because they determine whether workflow logic, approvals, and action histories remain under institutional control. Leaders should treat orchestration choices as accountability choices.

## Recommended Self-Hosted and Open Options

| Capability | Tools | Leadership Decision Lens |
| --- | --- | --- |
| Agent orchestration | LangGraph, CrewAI, AutoGen | Favor options that make workflow state, approvals, and boundaries visible to oversight bodies. |
| Workflow automation | Temporal, Camunda, Apache Airflow | Process definitions and audit trails should remain portable and reviewable. |
| Decision management | Drools, OpenL Tablets, custom rule engines | Decision logic should be inspectable and not buried inside application code or prompts. |
| Human-in-the-loop operations | Internal approval services, Jira workflows, ServiceNow integration | Approval records should be identity-backed and easy to reconstruct in review. |
| Observability | OpenTelemetry, Prometheus, Grafana | Runtime traces should support operational review, policy review, and incident response. |

## Leadership Guidance

- Keep workflow state and action logs in enterprise-controlled systems.
- Enforce tool allowlists and scoped credentials for agent calls.
- Require deterministic rollback strategies for critical flows.
- Cross-check orchestration choices against [Business Value](../../docs/business-value.md) and the [Owned-Brain Strategy](../../ARCHITECTURE.md).
