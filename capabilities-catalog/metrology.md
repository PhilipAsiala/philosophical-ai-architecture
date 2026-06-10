# Layer 1 — Metrology: Data Quality, Measurement, and Provenance

> **Core principle:** AI systems are only as trustworthy as the data they are built on. Metrology capabilities ensure that data is measured, quality-assured, observable, and traceable before it reaches higher cognitive layers.

---

## What Metrology Covers

| Capability Domain | Description |
|---|---|
| **Data ingestion and validation** | Controls for what data enters the system and how it is checked |
| **Data quality measurement** | Ongoing measurement of completeness, accuracy, consistency, and freshness |
| **Provenance and lineage** | Tracking where data came from, how it was transformed, and who validated it |
| **Observability and monitoring** | Real-time visibility into data health, drift, and anomalies |
| **Storage and portability** | How data is stored to ensure ownership and long-term access |

---

## Core Capabilities

### M1 — Data Quality Rules Engine
**What it does:** Enforces defined quality rules at ingestion — completeness thresholds, format validation, range checks, referential integrity.

**Why it matters for government:** A tax system relying on W-2 data with 15% null fields in the employer EIN column will produce systematically incorrect income matches. Quality rules catch this before it propagates.

**Minimum acceptable standard (Score 3):** Basic rules exist for core fields; failures are logged and escalated.

**Good practice (Score 4–5):** Automated quality profiling on every ingestion batch; failures block downstream processing; quality metrics are published and tracked over time.

---

### M2 — Data Provenance Recording
**What it does:** Creates and maintains a record of each data item's origin, collection context, and transformation history.

**Why it matters for government:** When a constituent challenges a decision, the agency must demonstrate that the underlying data was collected lawfully, from an authorized source, and processed correctly. Provenance is the evidence chain.

**Minimum acceptable standard (Score 3):** Source system, collection date, and basic transformation steps recorded per record.

**Good practice (Score 4–5):** Cryptographic fingerprinting of source records; immutable audit log of all transformations; chain-of-custody from source to model input.

---

### M3 — Statistical Profiling and Drift Detection
**What it does:** Continuously measures the statistical properties of data (distributions, null rates, value ranges) and alerts when those properties change unexpectedly.

**Why it matters for government:** Model behavior can degrade silently when input data distributions shift — for example, when a third-party income reporter changes their reporting format. Drift detection catches this before it causes systematic errors.

**Minimum acceptable standard (Score 3):** Periodic profiling with manual review of major anomalies.

**Good practice (Score 4–5):** Automated continuous profiling; alerting on statistical drift with defined thresholds; trend tracking over time.

---

### M4 — Open-Format Data Storage
**What it does:** Stores all data in open, non-proprietary formats that can be read and migrated without vendor cooperation.

**Why it matters for government:** Proprietary data formats create hard lock-in. When a contract ends, you need your data — not a vendor's promise to provide an export.

**Minimum acceptable standard (Score 3):** Core data exportable in a standard format (CSV, JSON, Parquet).

**Good practice (Score 4–5):** All data stored natively in open-format lakehouse (Iceberg + Parquet); no proprietary format dependencies; self-hosted storage with full agency control.

---

### M5 — Data Access Controls and Egress Logging
**What it does:** Enforces who can access what data, and logs all access events for audit purposes.

**Why it matters for government:** Privacy Act, FOIA, and cybersecurity requirements all depend on knowing who accessed what data and when. Egress logging is the evidentiary foundation.

**Minimum acceptable standard (Score 3):** Role-based access control enforced; access logs available for audit.

**Good practice (Score 4–5):** Zero-trust access model; real-time egress monitoring; automated alerts on unusual access patterns; logs tamper-evident and retained per retention schedule.

---

## Recommended Tools

### Self-Hosted / Open Source (Preferred)

| Tool | Category | Description |
|---|---|---|
| **Apache Iceberg** | Storage format | Open table format for large-scale analytics; supports time travel and schema evolution |
| **Apache Parquet** | Column storage | Open-standard columnar format; high compression and performance; vendor-agnostic |
| **Apache Hudi** | Data lakehouse | Open-source storage layer with ACID transactions and incremental processing |
| **Great Expectations** | Data quality | Open-source data quality framework; define, test, and document data quality expectations |
| **Apache Atlas** | Data catalog / lineage | Open-source data governance and metadata management; tracks lineage and provenance |
| **OpenLineage** | Lineage standard | Open standard for data lineage collection; integrates with Spark, dbt, Airflow |
| **dbt (data build tool)** | Transformation + lineage | Open-source SQL transformation tool with built-in lineage tracking |
| **Monte Carlo** | Data observability | Data observability platform with anomaly detection and data reliability monitoring |
| **Amundsen** | Data catalog | Open-source data discovery and metadata platform |

### Deployment Notes

- **For government air-gapped environments:** Apache Iceberg + Parquet + Great Expectations can be run entirely on-premises with no cloud dependency
- **For lineage tracking:** OpenLineage is the open standard; integrates with most pipeline tools
- **For catalog/discovery:** Apache Atlas is the enterprise-grade open-source choice; Amundsen for lighter-weight needs

---

## Patterns

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

---

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| Vendor owns data lineage records | Cannot produce independent audit trail | "We would need to request that from our data provider" |
| No quality rules on third-party data | Garbage enters the system undetected | No documented data quality framework |
| Data stored in proprietary format | Lock-in; migration becomes expensive | Data only accessible through vendor API |
| No egress logging | Privacy Act and security compliance gaps | "We log access at the application level but not the data level" |
| Quality checks happen downstream | Errors propagate before detection | Quality issues discovered when model outputs are wrong |

---

## Related Capabilities

- **Ontology (Layer 2):** Metrology validates data quality; Ontology gives it meaning. Both layers must share consistent entity identifiers.
- **Epistemology (Layer 3):** Epistemology's fact-verification gates depend on Metrology's provenance records as the ground truth anchor.
- **Data Substrate:** All Metrology outputs are stored in the Data Substrate with provenance records attached.
