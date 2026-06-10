# Metrology Capabilities

## What Leaders Need to Know

Bottom line: an organization that controls its data foundation can make more defensible decisions, withstand audit scrutiny, and avoid long-term dependency on external platforms.

See [ARCHITECTURE.md](../../ARCHITECTURE.md) for the strategic rationale and [Business Value](../../docs/business-value.md) for the investment lens.

## Mission and Governance Outcomes

- Trustworthy decision-making based on governed source data.
- Better audit readiness through lineage, provenance, and replay.
- Reduced vendor lock-in by owning storage, metadata, and control boundaries.
- Stronger privacy and records-management posture for regulated workloads.

## Capability Matrix

The matrix below binds the minimum set of Metrology capabilities to **Score 3 — Defined & Contained — Minimum Acceptable Standard** in the existing [Metrology scoring guide](scoring.md). Capabilities that contribute to Scores 4 and 5 lift the layer beyond that baseline. Live delivery status should be tracked through the [Praxeology workflow](../praxeology/tools.md); the JIRA epic column below is illustrative only.

| Capability | Minimum set? (Score 3) | Maturity contribution (3 / 4 / 5) | Owner | Delivery tracking (illustrative: JIRA epic) |
| --- | --- | --- | --- | --- |
| Raw data ingestion and scalable compute for batch and streaming workloads | Yes | 3 — establishes a controlled internal data foundation for operational use | Data platform owner | Illustrative: JIRA epic for governed ingestion and compute onboarding |
| Structured storage with versioning and replay support (for example, Delta Lake patterns) | Yes | 3 — enables repeatable storage, replay, and controlled operational use | Data platform owner | Illustrative: JIRA epic for versioned storage and replay |
| Data catalog operations for centralized metadata and discovery | No | 4 — strengthens discoverability, reuse, and governance at scale | Data governance owner | Illustrative: JIRA epic for catalog and metadata operations |
| Schema enforcement, data quality checks, and validation gates | Yes | 3 — provides the defined quality controls expected at the minimum acceptable standard | Data quality owner | Illustrative: JIRA epic for schema and quality controls |
| Access control, lineage, provenance, and time-travel inspection | Yes | 3 / 4 / 5 — baseline lineage and access control support Score 3, while deeper provenance and inspection lift audit readiness | Data governance owner | Illustrative: JIRA epic for access, lineage, and provenance controls |

## Questions Leaders Should Ask Before Funding

- Is the authoritative data source internal, governed, and contractually controllable?
- Can the team show where every critical dataset came from and how it changed over time?
- Are data quality failures blocked before they affect downstream decisions?
- If the current platform or vendor changes, does the organization retain its data and metadata?
