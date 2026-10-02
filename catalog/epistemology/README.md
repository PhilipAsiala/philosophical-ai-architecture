# Epistemology Catalog

Epistemology is the probabilistic inference layer. It proposes Belief, Defeater, or Ignorance. Confidence lives in the epistemic envelope. This layer does not authorize action.

## Executive Summary

Bottom line: this layer separates what the model guessed from what the organization can defend. Organization leaders should care because stakeholder trust, auditability, and appeals depend on it.

See the strategic rationale in [ARCHITECTURE.md](../../ARCHITECTURE.md) and the investment framing in [Business Value](../../docs/business-value.md).

## Layer Scope

- Grounded retrieval and inference (exposed via MCP servers — not direct orchestrator calls)
- Model validation and reliability checks
- Provenance tracking for conclusions with exact citations to owned substrate records
- Uncertainty handling and quality scoring
- Explanation generation and consistency checks

## Integration Points

- Beside: [Metrology](../metrology/README.md) supplies calibration and error bounds for the proposal
- Downstream: [Ontology](../ontology/README.md) may shape a categorical candidate from a Belief. [Praxeology](../praxeology/README.md) admits transitions. [Axiology](../axiology/README.md) is the only layer that returns Commit, Forbid, or Refuse to Act.

## Leadership Lens

- Prevents black-box conclusions from driving public decisions.
- Improves audit and review posture by preserving evidence and explanations.
- Helps leadership distinguish between experimental AI and decision-ready AI.

## File Guide

- [Capabilities](capabilities.md)
- [Tools](tools.md)
- [Patterns and Anti-Patterns](patterns.md)
- [Scoring](scoring.md)
- [Examples](examples/README.md)
