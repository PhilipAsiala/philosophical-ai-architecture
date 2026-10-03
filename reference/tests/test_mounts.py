"""Iceberg is the ledger. The graph and the OPA bundle are mounts over it."""

from moepa_guard.agents.policy.base import PolicyView
from moepa_guard.mounts.decision_input import policy_document
from moepa_guard.pipeline.orchestrator import GuardrailPipeline
from support import benefits_world, candidate


def test_missing_ledger_row_is_missing_from_the_graph() -> None:
    world = benefits_world()

    assert world.graph.exists("Applicant:TX12345")
    assert not world.graph.exists("Applicant:DOES-NOT-EXIST")


def test_opa_input_has_no_score() -> None:
    world = benefits_world()
    view = PolicyView(
        proposal_id="prop-1",
        commit_eligible=True,
        action="export_pii",
        epistemic_state="belief",
        entity_ids=("Applicant:TX12345",),
        triples=(),
        flags={"vendor_request": True},
    )
    document = policy_document(view, world)

    assert "confidence" not in document
    assert "uncertainty" not in document
    assert "distribution" not in document


def test_praxeology_allows_a_staged_transition_and_axiology_can_still_deny() -> None:
    bundle = benefits_world().bundle
    possible = {
        "requested_state": "transition_to_production",
        "current_state": "staged",
        "user_clearance": 1,
        "required_clearance": 3,
        "commit_eligible": True,
        "action": "transition_to_production",
    }

    assert bundle.boolean("moepa.praxeology", "allow_action", possible)
    assert bundle.boolean("moepa.axiology", "deny_action", possible)

    impossible = {**possible, "current_state": "draft"}
    assert not bundle.boolean("moepa.praxeology", "allow_action", impossible)


def test_bundle_files_come_from_the_ledger() -> None:
    world = benefits_world()

    assert "moepa/praxeology/policy.rego" in world.bundle.files
    assert "moepa/axiology/policy.rego" in world.bundle.files
    assert "package moepa.praxeology" in world.bundle.files["moepa/praxeology/policy.rego"]
    assert "package moepa.axiology" in world.bundle.files["moepa/axiology/policy.rego"]


def test_commit_is_appended_to_the_ledger() -> None:
    world = benefits_world()
    result = GuardrailPipeline(world).run(candidate(proposal_id="ok", action="record_income"))

    assert result.outcome == "committed"
    assert world.ledger.commits == [result.commit]
    assert not world.graph.exists("confidence")
