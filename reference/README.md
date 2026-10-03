# MOEPA guardrail reference

A small, tested illustration of the dual-domain control flow. It is not a production runtime and it does not call a language model.

The mind is probabilistic in handling evidence, and non-probabilistic in its commitments.

## Flow

1. A proposer (any provider) builds an `UncommittedCandidate`: a proposed action, an `EpistemicClaim`, and metrology telemetry.
2. `StateCollapseEngine` turns that payload into one discrete action. It does not sample. A tied distribution or a non-belief yields no commit-eligible action. The confidence value is kept on the audit record only.
3. Deterministic agents run in order: `OntologyPolicyAgent`, `PraxeologyPolicyAgent`, `AxiologyPolicyAgent`. Their input type, `PolicyView`, has no confidence field.
4. The external result is **committed** or **blocked**. Only a committed result writes an `IcebergCommitRecord`. Forbid and Refuse to Act are both blocks.

## Layout

| Path | Role |
|---|---|
| `src/moepa_guard/schemas/` | `EpistemicClaim` separated from `OntologicalEntity`, RDF triples, Iceberg commit metadata |
| `src/moepa_guard/agents/policy/` | `DeterministicPolicyAgent` and the three layer agents |
| `src/moepa_guard/pipeline/` | Collapse engine and sequential pipeline |
| `tests/` | High-confidence boundary block, schema firewall, deterministic collapse |

## Run

```bash
python -m pytest reference/tests
```

From this directory, after installing the package, `pytest` is enough. The agents import no LLM client, so they run without a model provider.
