# Metrology Patterns and Anti-Patterns

## Why These Patterns Matter to Leaders

Weak data patterns do not stay technical for long. They surface as audit failures, unreliable decisions, compliance gaps, and unexpected vendor dependence.

## Durable Governance Patterns

- **Data Contract First**: publish schema contracts before ingestion changes
- **Bronze/Silver/Gold Zones**: separate raw, cleaned, and production-grade data
- **Quality Gate Pipelines**: block promotion when validation thresholds fail
- **Immutable Event Logs**: retain append-only records for replay and forensics

## Named Implementation Patterns

### Pattern M-A: Ingestion Quality Gate
All incoming data passes through a defined quality rules engine before being written to the Data Substrate. Records failing quality checks are quarantined, logged, and escalated — never silently passed through or discarded.

```
Source Data → Quality Rules Engine → PASS → Data Substrate
                                  → FAIL → Quarantine + Alert + Escalation Log
```

### Pattern M-B: Immutable Provenance Record
Every record written to the Data Substrate includes a provenance header containing: source identifier, collection timestamp, ingestion pipeline version, quality check results, and a content hash. This header is immutable after write.

### Pattern M-C: Statistical Baseline and Drift Alert
On first ingestion, a statistical baseline is computed for each data asset (field distributions, null rates, range bounds). On each subsequent ingestion, current statistics are compared to the baseline; deviations exceeding defined thresholds trigger alerts before downstream processing.

## Costly Patterns to Avoid

- Hidden ETL logic in unmanaged scripts with no version control
- Exclusive dependence on proprietary catalogs for lineage truth
- Manual schema changes without compatibility checks
- Data quality checks that only alert but never gate usage

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| Vendor owns data lineage records | Cannot produce independent audit trail | "We would need to request that from our data provider" |
| No quality rules on third-party data | Garbage enters the system undetected | No documented data quality framework |
| Data stored in proprietary format | Lock-in; migration becomes expensive | Data only accessible through vendor API |
| No egress logging | Privacy Act and security compliance gaps | "We log access at the application level but not the data level" |
| Quality checks happen downstream | Errors propagate before detection | Quality issues discovered when model outputs are wrong |

## What Leaders Should Watch For

- Catalog drift where metadata does not match actual pipeline behavior
- Time-travel gaps due to retention settings not aligned to compliance needs
- Untracked data access in privileged service accounts

See [Business Value](../../docs/business-value.md) and [ARCHITECTURE.md](../../ARCHITECTURE.md) for why durable data governance is central to the Owned-Brain Strategy.
