"""Shared world and candidate builders for the guardrail tests."""

from __future__ import annotations

import tempfile
from pathlib import Path

from moepa_guard.agents.policy.world import WorldSnapshot
from moepa_guard.mounts.bundle import BundleSync, seed_rules
from moepa_guard.mounts.graph import GraphProjection
from moepa_guard.mounts.ledger import IcebergLedger
from moepa_guard.schemas.epistemic import EpistemicClaim, EpistemicState, MetrologyTelemetry
from moepa_guard.schemas.ontology import OntologicalEntity, RdfTriple, RelationRule
from moepa_guard.schemas.proposal import UncommittedCandidate


def benefits_world() -> WorldSnapshot:
    """Iceberg holds the applicant and the Rego. Graph and OPA are mounts."""

    applicant = OntologicalEntity(
        entity_id="Applicant:TX12345",
        entity_type="Applicant",
        attributes={"program": "benefits"},
    )
    ledger = IcebergLedger(
        entities=[applicant],
        triples=[
            RdfTriple(
                subject="Applicant:TX12345",
                predicate="enrolledIn",
                object="benefits",
            )
        ],
        relation_rules=[
            RelationRule(subject_type="Applicant", predicate="enrolledIn", object_type=None),
        ],
        policy_rules=seed_rules(),
    )
    bundle_dir = Path(tempfile.mkdtemp(prefix="moepa-bundle-"))
    bundle = BundleSync().publish(ledger, bundle_dir)
    return WorldSnapshot(
        ledger=ledger,
        graph=GraphProjection(ledger),
        bundle=bundle,
        resources={"review_slots": 2},
        satisfiable_postconditions=frozenset({"ledger_appended"}),
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
