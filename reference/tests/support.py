"""Shared world and candidate builders for the guardrail tests."""

from __future__ import annotations

from moepa_guard.agents.policy.world import OperationSpec, WorldSnapshot
from moepa_guard.schemas.epistemic import EpistemicClaim, EpistemicState, MetrologyTelemetry
from moepa_guard.schemas.ontology import OntologicalEntity, RdfTriple, RelationRule
from moepa_guard.schemas.proposal import UncommittedCandidate


def benefits_world() -> WorldSnapshot:
    """One known applicant and two operations, one of which axiology forbids."""

    applicant = OntologicalEntity(
        entity_id="Applicant:TX12345",
        entity_type="Applicant",
        attributes={"program": "benefits"},
    )
    return WorldSnapshot(
        entities={applicant.entity_id: applicant},
        triples=(
            RdfTriple(
                subject="Applicant:TX12345",
                predicate="enrolledIn",
                object="benefits",
            ),
        ),
        relation_rules=(
            RelationRule(subject_type="Applicant", predicate="enrolledIn", object_type=None),
        ),
        operations={
            "record_income": OperationSpec(
                action="record_income",
                preconditions={"evidence_present": True},
                required_resources={"review_slots": 1},
                postconditions=("ledger_appended",),
            ),
            "export_pii": OperationSpec(
                action="export_pii",
                preconditions={"vendor_request": True},
                required_resources={"review_slots": 1},
                postconditions=("ledger_appended",),
            ),
        },
        resources={"review_slots": 2},
        satisfiable_postconditions=frozenset({"ledger_appended"}),
        forbidden_actions=frozenset({"export_pii"}),
        schema_id=3,
        table="ontological_entity",
    )


def candidate(
    *,
    proposal_id: str = "prop-1",
    action: str = "record_income",
    confidence: float | None = 0.99,
    state: EpistemicState = EpistemicState.BELIEF,
    entity_ids: list[str] | None = None,
    distribution: dict[str, float] | None = None,
    defeaters: list[str] | None = None,
    flags: dict[str, bool] | None = None,
) -> UncommittedCandidate:
    claim_confidence = None if state is EpistemicState.IGNORANCE else confidence
    return UncommittedCandidate(
        proposal_id=proposal_id,
        query="Should the system act on this applicant?",
        proposed_action=action,
        proposed_response="Proposed by the inference adapter.",
        claim=EpistemicClaim(
            claim_id=f"claim-{proposal_id}",
            proposition=f"Action {action} is warranted.",
            state=state,
            confidence=claim_confidence,
            distribution=distribution,
            evidence_links=["evidence:wage-2025"],
            source_provenance=["source:state-wage"],
            defeaters=defeaters or [],
        ),
        metrology=MetrologyTelemetry(
            confidence=0.0 if confidence is None else confidence,
            uncertainty=0.01,
            error_bound=0.02,
            calibration_id="cal-2026",
        ),
        entity_ids=["Applicant:TX12345"] if entity_ids is None else entity_ids,
        triples=[RdfTriple(subject="Applicant:TX12345", predicate="enrolledIn", object="benefits")],
        flags=flags or {"evidence_present": True, "vendor_request": True},
    )
