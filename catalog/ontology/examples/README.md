# Ontology Examples

## Why These Examples Matter

These are examples of governed semantic assets that help leadership ensure the organization owns its core definitions and relationships.

## SPO Triple + Ontology Graph Form

This example demonstrates the substrate pattern for the Ontology layer: the base triple lives once on the shared SPO backbone as a typed edge in the entity graph, and the ontological form captures the structural representation — entity nodes, typed edges, category memberships, and hierarchical relationships.

**Income verification — entity graph representation**

```json
{
  "triple": {"s": "IncomeVerification:TX12345", "p": "hasAmount", "o": 85000},
  "ontology_form": {
    "subject_entity": {
      "id": "IncomeVerification:TX12345",
      "type": "VerificationRecord",
      "category": "FinancialVerification",
      "hierarchy": ["Record", "VerificationRecord", "FinancialVerification"]
    },
    "predicate": {
      "relation": "hasAmount",
      "relation_type": "DataProperty",
      "domain": "VerificationRecord",
      "range": "xsd:decimal"
    },
    "object_entity": {
      "value": 85000,
      "type": "MonetaryAmount",
      "membership": "IncomeObservations"
    },
    "graph_edges": [
      {"from": "IncomeVerification:TX12345", "relation": "hasAmount", "to": 85000},
      {"from": "IncomeVerification:TX12345", "relation": "instanceOf", "to": "FinancialVerification"},
      {"from": "FinancialVerification", "relation": "subClassOf", "to": "VerificationRecord"}
    ]
  }
}
```

The base triple `(IncomeVerification:TX12345, hasAmount, 85000)` is stored once in the shared SPO/quad backbone. The `ontology_form` envelope is the Ontology layer's contribution: it records the *structural and semantic shape* — entity types, category memberships, class hierarchies, and typed relation definitions. Nodes represent entities (from sets), edges represent typed relations, and taxonomic structure is stored natively in a graph database (Neo4j, property graph) or as RDF triples.

## Example Governance Artifacts

- ontology/entities/customer.yaml
- ontology/relationships/account-ownership.yaml
- ontology/taxonomies/business-hierarchy.ttl
- ontology/release-notes/v1.2.0.md

## Example Configuration Ideas

- Change-control checklist for ontology updates
- Entity resolution confidence thresholds
- Graph query performance and freshness SLAs
