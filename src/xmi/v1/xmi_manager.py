# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .entities.xmi_structural_material import XmiStructuralMaterial

from .xmi_base import *


class ErrorLog():
    def __init__(self, entity_type, index, message, obj=None):
        self.entity_type = entity_type
        self.index = index
        self.message = message
        self.obj = str(obj)


class XmiManager():
    def __init__(self):
        self.entities = []
        self.relationships = []
        self.histories = []
        self.errors = []

    def create_relationship(self,
                            relationship_class: XmiBaseRelationship,
                            source: XmiBaseEntity,
                            target: XmiBaseEntity) -> XmiBaseRelationship:

        relationship = relationship_class(source, target)
        self.relationships.append(relationship)
        return relationship

    def create_entity(self, entity_class: XmiBaseEntity, **kwargs) -> XmiBaseEntity:
        entity = entity_class(**kwargs)
        self.entities.append(entity)
        return entity

    def get_related_entities(self, entity) -> list[XmiBaseEntity]:
        related_entities = []
        for relation in entity.relations:
            related_entities.append(relation.target)
        return related_entities

    def find_relationship_by_target(self, target_name) -> list[XmiBaseRelationship]:
        return [rel for rel in self.relationships if rel.target.name == target_name]

    def read_xmi_dict(self, xmi_dict: dict):
        for xmi_key, xmi_value in xmi_dict.items():
            if xmi_key == "StructuralMaterial":
                for index, xmi_structural_material_obj in enumerate(xmi_dict['StructuralMaterial']):
                    try:
                        xmi_structural_material = XmiStructuralMaterial.from_xmi_dict_obj(
                            xmi_structural_material_obj)
                        self.entities.append(xmi_structural_material)
                    except Exception as e:
                        self.errors.append(
                            ErrorLog(xmi_key, index, str(e)))
