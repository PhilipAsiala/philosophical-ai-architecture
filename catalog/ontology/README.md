# Ontology Catalog

Ontology is the deterministic structure layer. Entities and relations are categorical. Confidence, probability, and "maybe" are not properties of existence; they stay on the epistemic envelope.

## Executive Summary

Bottom line: this layer determines whether the organization has a shared understanding of customers, businesses, programs, and relationships. If it is weak, leaders will fund systems that cannot reason consistently across the enterprise.

See the strategic rationale in [ARCHITECTURE.md](../../ARCHITECTURE.md) and the investment framing in [Business Value](../../docs/business-value.md).

## Layer Scope

- Entity and relationship modeling
- Knowledge graph construction and hierarchy management
- Semantic linking across datasets
- Graph querying and dynamic relationship updates
- Controlled ingestion from Metrology assets

## Integration Points

- Schema is available to [Epistemology](../epistemology/README.md) as the categorical model a proposal must match
- Instance triples are written only after [Axiology](../axiology/README.md) returns Commit
- [Metrology](../metrology/README.md) observations are inputs to proposals, not entity writes

## Leadership Lens

- Turns fragmented program knowledge into a reusable institutional asset.
- Reduces conflicting definitions across systems and vendors.
- Improves the value of future AI investments by preserving shared meaning.

## File Guide

- [Capabilities](capabilities.md)
- [Tools](tools.md)
- [Patterns and Anti-Patterns](patterns.md)
- [Scoring](scoring.md)
- [Examples](examples/README.md)
