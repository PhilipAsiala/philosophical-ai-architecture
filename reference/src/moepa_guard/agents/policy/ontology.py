"""Schema and grounding checks. Existence is categorical."""

from __future__ import annotations

from moepa_guard.agents.policy.base import DeterministicPolicyAgent, PolicyResult, PolicyView
from moepa_guard.agents.policy.world import WorldSnapshot


class OntologyPolicyAgent(DeterministicPolicyAgent):
    """Reject ungrounded entity ids and triples that break the relation schema."""

    name = "ontology"

    def evaluate(self, proposal: PolicyView, world: WorldSnapshot) -> PolicyResult:
        if not proposal.commit_eligible:
            return PolicyResult(
                agent=self.name,
                passed=True,
                rule_id="ONT-NO-WRITE",
                detail="No categorical write was proposed.",
            )
        for entity_id in proposal.entity_ids:
            if entity_id not in world.entities:
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="ONT-UNGROUNDED",
                    detail=f"Entity {entity_id} has no grounded reference.",
                )
        for triple in proposal.triples:
            breach = _relation_breach(triple.subject, triple.predicate, triple.object, world)
            if breach is not None:
                return PolicyResult(
                    agent=self.name,
                    passed=False,
                    rule_id="ONT-RELATION",
                    detail=breach,
                )
        return PolicyResult(
            agent=self.name,
            passed=True,
            rule_id="ONT-GROUNDED",
            detail="Referenced entities and relations match the schema.",
        )


def _relation_breach(
    subject: str,
    predicate: str,
    obj: str,
    world: WorldSnapshot,
) -> str | None:
    subject_entity = world.entities.get(subject)
    if subject_entity is None:
        return f"Triple subject {subject} is not a known entity."
    matched = False
    for rule in world.relation_rules:
        if rule.subject_type != subject_entity.entity_type or rule.predicate != predicate:
            continue
        if rule.object_type is None:
            matched = True
            break
        object_entity = world.entities.get(obj)
        if object_entity is not None and object_entity.entity_type == rule.object_type:
            matched = True
            break
    if not matched:
        return f"Relation {predicate} is not allowed for {subject_entity.entity_type}."
    return None
