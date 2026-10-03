"""Graph projection over Iceberg entity and triple tables.

If a node is not in this projection, it does not exist in the ontology.
The projection is rebuilt from the ledger. It does not store a private copy
of reality and it has no score-valued edges.
"""

from __future__ import annotations

from moepa_guard.mounts.ledger import IcebergLedger
from moepa_guard.schemas.ontology import OntologicalEntity, RelationRule


class GraphProjection:
    """Read-only graph mount. Callers ask existence and relation questions."""

    def __init__(self, ledger: IcebergLedger) -> None:
        self._nodes = {entity.entity_id: entity for entity in ledger.entities}
        self._rules = tuple(ledger.relation_rules)

    def exists(self, entity_id: str) -> bool:
        return entity_id in self._nodes

    def entity(self, entity_id: str) -> OntologicalEntity | None:
        return self._nodes.get(entity_id)

    def relation_breach(self, subject: str, predicate: str, obj: str) -> str | None:
        """Return a reason the edge is absent from the ontology, or None."""

        subject_entity = self._nodes.get(subject)
        if subject_entity is None:
            return f"Triple subject {subject} is not a node in the graph."
        for rule in self._rules:
            if _rule_matches(rule, subject_entity, predicate, obj, self._nodes):
                return None
        return f"Relation {predicate} is not in the graph schema for {subject_entity.entity_type}."


def _rule_matches(
    rule: RelationRule,
    subject: OntologicalEntity,
    predicate: str,
    obj: str,
    nodes: dict[str, OntologicalEntity],
) -> bool:
    if rule.subject_type != subject.entity_type or rule.predicate != predicate:
        return False
    if rule.object_type is None:
        return True
    object_entity = nodes.get(obj)
    return object_entity is not None and object_entity.entity_type == rule.object_type
