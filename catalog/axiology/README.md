# Axiology Catalog

Axiology is the deterministic final arbiter. It returns exactly one verdict: Commit, Forbid, or Refuse to Act. It does not return a probability of permission. Refuse to Act is required for Ignorance and unresolved defeaters.

## Executive Summary

Bottom line: this layer determines whether AI remains aligned to law, policy, mission, and stakeholder trust. Organization leaders should treat it as the final authority on what the institution is willing to permit, defend, and fund.

See the strategic rationale in [ARCHITECTURE.md](../../ARCHITECTURE.md) and the investment framing in [Business Value](../../docs/business-value.md).

## Layer Scope

- Bias and fairness monitoring
- Policy and regulatory rule enforcement
- Ethical alignment scoring and strategic goal checks
- Privacy controls and rights protection
- Transparency, explainability, and compliance accountability

## Integration Points

- Upstream: [Praxeology](../praxeology/README.md) presents an admitted or rejected transition. Execution of a state change happens only after Commit.
- Cross-cutting: policy requirements constrain which proposals the lower layers are allowed to attempt. They do not turn Epistemology into an authorizer.

## Leadership Lens

- Protects legitimacy, compliance posture, and stakeholder trust.
- Ensures investment decisions stay aligned to mission and statutory obligations.
- Converts governance from advisory intent into enforceable institutional control.

## File Guide

- [Capabilities](capabilities.md)
- [Tools](tools.md)
- [Patterns and Anti-Patterns](patterns.md)
- [Scoring](scoring.md)
- [Examples](examples/README.md)
