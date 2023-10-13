from .entities.xmi_base_entity import XmiBaseEntity
from .relationships.xmi_base_relationship import XmiBaseRelationship


class XmiManager():
    def __init__(self):
        self.entities = []
        self.relationships = []

    def create_entity(self, entity_class: XmiBaseEntity, name) -> XmiBaseEntity:
        entity = entity_class(name)
        self.entities.append(entity)
        return entity

    def create_relationship(self,
                            relationship_class: XmiBaseRelationship,
                            source: XmiBaseEntity,
                            target: XmiBaseEntity) -> XmiBaseRelationship:

        relationship = relationship_class(source, target)
        source.relationships.append(relationship)
        self.relationships.append(relationship)
        return relationship

    def get_related_entities(self, entity):
        related_entities = []
        for relation in entity.relations:
            related_entities.append(relation.target)
        return related_entities

    def find_relationship_by_target(self, target_name):
        return [rel for rel in self.relationships if rel.target.name == target_name]
