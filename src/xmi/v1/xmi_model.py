# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .xmi_base import XmiBaseEntity, XmiBaseRelationship


class ErrorLog():
    def __init__(self, entity_type: str, index: int, message: str, obj: str = None):
        self.entity_type: str = entity_type
        self.index: int = index
        self.message: str = message
        self.obj: str = str(obj)


class XmiModel():
    def __init__(self):
        self.entities: list[XmiBaseEntity] = []
        self.relationships: list[XmiBaseRelationship] = []
        self.histories = []
        self.errors: list[ErrorLog] = []

    def create_relationship(self,
                            relationship_class: XmiBaseRelationship,
                            source: XmiBaseEntity,
                            target: XmiBaseEntity,
                            name: str = None,
                            **kwargs) -> XmiBaseRelationship:

        if relationship_class == XmiBaseRelationship:
            relationship = relationship_class(source, target, name)
        else:
            relationship = relationship_class(
                source, target, **kwargs)
        self.relationships.append(relationship)
        return relationship

    def create_entity(self, entity_class: XmiBaseEntity, **kwargs) -> XmiBaseEntity:
        entity = entity_class(**kwargs)
        self.entities.append(entity)
        return entity

    def find_relationships_by_target(self, target_name) -> list[XmiBaseRelationship]:
        return [rel for rel in self.relationships if rel.target.name == target_name]
