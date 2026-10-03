# MOEPA guardrail reference

A small, tested illustration of the end-state substrate. It is not a production cluster and it does not call a language model.

Apache Iceberg is the ledger. The deterministic engines are mounts over that ledger.

| Layer | Mount in this package |
|---|---|
| Ontology | `GraphProjection` built only from entity and triple rows. A missing node does not exist. |
| Praxeology | Rego package `moepa.praxeology`, decision `allow_action` |
| Axiology | Rego package `moepa.axiology`, decision `deny_action` |

Both Rego documents are versioned as ledger rows and published by `BundleSync` into one bundle (`moepa/praxeology/policy.rego` and `moepa/axiology/policy.rego`). A deployment evaluates that bundle with Open Policy Agent. This package evaluates the same boolean fragment so the tests do not need a live OPA server. The decision document has no confidence field.

Metrology and epistemology stay on the proposal. Their end-state mounts are Trino and Qdrant. They are not asked for permission.

## Flow

1. A proposer builds an `UncommittedCandidate`.
2. `StateCollapseEngine` reduces it to one discrete action. It does not sample.
3. Ontology queries the graph projection.
4. Praxeology asks `allow_action`.
5. Axiology asks `deny_action`. A possible act can still be denied.
6. The external result is **committed** or **blocked**. A commit appends an Iceberg snapshot row. It does not add a score to the graph.

## Run

```bash
python -m pytest reference/tests
```
