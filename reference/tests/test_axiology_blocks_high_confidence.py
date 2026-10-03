"""A high confidence score does not authorize a forbidden action."""

from moepa_guard.pipeline.orchestrator import GuardrailPipeline
from moepa_guard.schemas.epistemic import EpistemicState
from support import benefits_world, candidate


def test_axiology_blocks_high_confidence_boundary_violation() -> None:
    pipeline = GuardrailPipeline(benefits_world())
    result = pipeline.run(
        candidate(
            proposal_id="hallucinated-permission",
            action="export_pii",
            confidence=0.99,
        )
    )

    assert result.outcome == "blocked"
    assert result.axiological_verdict == "forbid"
    assert result.blocking_rule_id == "AX-FORBID"
    assert result.commit is None
    assert result.epistemic_confidence == 0.99
    assert [stage.rule_id for stage in result.stages] == [
        "ONT-GROUNDED",
        "PRX-ADMITTED",
        "AX-FORBID",
    ]


def test_same_rules_block_a_low_confidence_forbidden_action() -> None:
    pipeline = GuardrailPipeline(benefits_world())
    low = pipeline.run(candidate(proposal_id="low", action="export_pii", confidence=0.01))
    high = pipeline.run(candidate(proposal_id="high", action="export_pii", confidence=0.99))

    assert low.outcome == high.outcome == "blocked"
    assert low.blocking_rule_id == high.blocking_rule_id == "AX-FORBID"


def test_allowed_belief_commits_without_consulting_confidence() -> None:
    pipeline = GuardrailPipeline(benefits_world())
    result = pipeline.run(candidate(proposal_id="ok", action="record_income", confidence=0.02))

    assert result.outcome == "committed"
    assert result.axiological_verdict == "commit"
    assert result.commit is not None
    assert result.commit.schema_id == 3
    assert result.commit.entity_id == "Applicant:TX12345"
    assert "confidence" not in result.commit.model_dump()


def test_ontology_blocks_ungrounded_entity_before_commit() -> None:
    pipeline = GuardrailPipeline(benefits_world())
    result = pipeline.run(
        candidate(
            proposal_id="invented",
            action="record_income",
            confidence=0.96,
            entity_ids=["Applicant:DOES-NOT-EXIST"],
        )
    )

    assert result.outcome == "blocked"
    assert result.blocking_rule_id == "ONT-UNGROUNDED"
    assert result.axiological_verdict is None
    assert result.commit is None


def test_ignorance_is_refused_even_when_metrology_reports_a_number() -> None:
    pipeline = GuardrailPipeline(benefits_world())
    result = pipeline.run(
        candidate(
            proposal_id="unknown",
            action="record_income",
            confidence=None,
            state=EpistemicState.IGNORANCE,
        )
    )

    assert result.outcome == "blocked"
    assert result.axiological_verdict == "refuse_to_act"
    assert result.blocking_rule_id == "AX-REFUSE"
    assert result.epistemic_confidence is None
