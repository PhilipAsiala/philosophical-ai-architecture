"""Epistemic uncertainty cannot be stored as entity existence."""

import pytest
from pydantic import ValidationError

from moepa_guard.agents.policy.base import PolicyView
from moepa_guard.schemas.ontology import ENTITY_TABLE_FIELDS, OntologicalEntity, RdfTriple

_LEAKED = {"confidence", "probability", "uncertainty", "existence_probability", "maybe", "score"}


def test_entity_table_has_no_uncertainty_columns() -> None:
    assert _LEAKED.isdisjoint(ENTITY_TABLE_FIELDS)


def test_entity_rejects_confidence_attribute() -> None:
    with pytest.raises(ValidationError):
        OntologicalEntity(
            entity_id="Applicant:TX1",
            entity_type="Applicant",
            attributes={"confidence": "0.99"},
        )


def test_triple_rejects_confidence_predicate() -> None:
    with pytest.raises(ValidationError):
        RdfTriple(subject="Applicant:TX1", predicate="hasConfidence", object="0.99")


def test_policy_view_has_no_score_field() -> None:
    assert _LEAKED.isdisjoint(PolicyView.model_fields)
