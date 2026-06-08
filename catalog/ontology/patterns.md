# Ontology Patterns and Anti-Patterns

## Why These Patterns Matter to Leaders

Weak semantic patterns create a hidden governance problem: systems appear connected, but they do not share the same meaning. That reduces reuse, increases disputes, and weakens institutional control.

## Durable Governance Patterns

- Canonical Entity Registry: maintain authoritative entity classes and IDs
- Relationship Typing Standards: enforce consistent edge semantics
- Semantic Layer Decoupling: separate storage implementation from domain semantics
- Ontology Version Releases: publish reviewed schema versions with compatibility notes

## Costly Patterns to Avoid

- Flat vector-only context with no explicit relationship model
- One-off entity definitions embedded in application code
- Unreviewed taxonomy changes in production
- External vendor ownership of canonical semantic truth

## What Leaders Should Watch For

- Entity identity collisions across systems
- Query instability from unconstrained relationship growth
- Semantic drift between business rules and graph schema

See [Business Value](../../docs/business-value.md) and [ARCHITECTURE.md](../../ARCHITECTURE.md) for why owning the semantic model is a strategic institutional decision.
