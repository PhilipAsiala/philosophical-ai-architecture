# Metrology Patterns and Anti-Patterns

## Why These Patterns Matter to Leaders

Weak data patterns do not stay technical for long. They surface as audit failures, unreliable decisions, compliance gaps, and unexpected vendor dependence.

## Durable Governance Patterns

- Data Contract First: publish schema contracts before ingestion changes
- Bronze/Silver/Gold Zones: separate raw, cleaned, and production-grade data
- Quality Gate Pipelines: block promotion when validation thresholds fail
- Immutable Event Logs: retain append-only records for replay and forensics

## Costly Patterns to Avoid

- Hidden ETL logic in unmanaged scripts with no version control
- Exclusive dependence on proprietary catalogs for lineage truth
- Manual schema changes without compatibility checks
- Data quality checks that only alert but never gate usage

## What Leaders Should Watch For

- Catalog drift where metadata does not match actual pipeline behavior
- Time-travel gaps due to retention settings not aligned to compliance needs
- Untracked data access in privileged service accounts

See [Business Value](../../docs/business-value.md) and [ARCHITECTURE.md](../../ARCHITECTURE.md) for why durable data governance is central to the Owned-Brain Strategy.
