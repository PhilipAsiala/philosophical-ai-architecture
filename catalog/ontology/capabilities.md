# Ontology Capabilities

## What Leaders Need to Know

Bottom line: this layer gives the institution a shared model of reality. Without it, different systems, vendors, and programs may disagree about what a customer, business, account, or relationship actually is.

See [ARCHITECTURE.md](../../ARCHITECTURE.md) for the strategic rationale and [Business Value](../../docs/business-value.md) for the investment lens.

## Mission and Governance Outcomes

- More consistent reasoning across programs and systems.
- Better reuse of institutional knowledge across initiatives.
- Reduced semantic lock-in to vendor-specific data models.
- Clearer accountability for how core entities and relationships are defined.

## Capability Matrix

The matrix below binds the minimum set of Ontology capabilities to **Score 3 — Defined & Contained — Minimum Acceptable Standard** in the existing [Ontology scoring guide](scoring.md). Capabilities that contribute to Scores 4 and 5 lift the layer beyond that baseline. Live delivery status should be tracked through the [Praxeology workflow](../praxeology/tools.md); the JIRA epic column below is illustrative only.

| Capability | Minimum set? (Score 3) | Maturity contribution (3 / 4 / 5) | Owner | Delivery tracking (illustrative: JIRA epic) |
| --- | --- | --- | --- | --- |
| Entity modeling for customers, businesses, accounts, and related actors | Yes | 3 — establishes governable core entities for the mission domain | Domain ontology owner | Illustrative: JIRA epic for core entity modeling |
| Relationship mapping across legal, financial, and operational domains | Yes | 3 — defines governable institutional relationships across key domains | Domain ontology owner | Illustrative: JIRA epic for relationship mapping |
| Knowledge graph construction with hierarchy and taxonomy support | No | 4 — expands reuse and institutional consistency through richer semantic governance | Knowledge graph owner | Illustrative: JIRA epic for knowledge graph and taxonomy build-out |
| Semantic linking to connect meaning across heterogeneous datasets | Yes | 3 / 4 — provides shared meaning across governed sources and improves reuse across programs | Domain integration owner | Illustrative: JIRA epic for semantic linking across datasets |
| Advanced graph querying with dynamic relationship updates | No | 5 — supports enterprise-scale reasoning and continuously evolving semantic operations | Knowledge graph owner | Illustrative: JIRA epic for advanced graph query services |
| Controlled integration with Metrology outputs | Yes | 3 — keeps semantic assets grounded in governed source data | Data and ontology steward | Illustrative: JIRA epic for ontology-to-metrology integration |

## Questions Leaders Should Ask Before Funding

- Are the key entities and relationships defined clearly enough for governance review?
- Who owns those definitions, and how are changes approved?
- If programs disagree about the meaning of a customer, business, or relationship, how is that resolved?
- Does the organization own the semantic model, or is that knowledge embedded inside a vendor platform?
