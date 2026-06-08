# Ontology Tools

## Executive Summary

These tool categories matter because they determine whether the organization owns its semantic model or leaves core institutional meaning embedded inside vendor products or isolated projects.

## Recommended Self-Hosted and Open Options

| Capability | Tools | Leadership Decision Lens |
| --- | --- | --- |
| Graph storage and querying | Neo4j (self-managed), JanusGraph, ArangoDB | Favor options that keep graph structures exportable and under institutional control. |
| RDF and semantic web | Apache Jena, RDF4J, Blazegraph | Standards-based options are useful when long-term interoperability matters. |
| Ontology modeling | Protégé, TopBraid EDG (self-hosted option) | Semantic definitions should be treated as governed institutional assets, not project artifacts. |
| Entity resolution | Splink, Dedupe, custom pipelines | Matching policies should be transparent enough for review in regulated contexts. |
| Graph ETL | Apache Spark GraphFrames, Kafka Connect, Airflow | Build graph pipelines so source lineage and accountability remain visible. |

## Leadership Guidance

- Keep canonical entity definitions inside internal repositories.
- Require change governance for taxonomy and relationship updates.
- Export graph snapshots for continuity and portability.
- Cross-check major semantic decisions against [Business Value](../../docs/business-value.md) and the [Owned-Brain Strategy](../../ARCHITECTURE.md).
