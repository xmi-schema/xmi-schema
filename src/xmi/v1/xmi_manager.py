# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .entities.xmi_structural_cross_section import XmiStructuralCrossSection

from .entities.xmi_structural_point_connection import XmiStructuralPointConnection
from .entities.xmi_structural_material import XmiStructuralMaterial
from .xmi_errors import *
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

        # Define the desired key order
        desired_order = ['StructuralMaterial',
                         'StructuralPointConnection',
                         'StructuralCrossSection']

        # Create a new dictionary with rearranged keys
        rearranged_dict = {key: xmi_dict[key]
                           for key in desired_order if key in xmi_dict.keys()}

        # Add keys not in the desired order
        rearranged_dict.update(
            {key: value for key, value in xmi_dict.items() if key not in desired_order})

        for xmi_dict_key, xmi_dict_value in xmi_dict.items():
            if xmi_dict_key == "StructuralMaterial":
                for index, xmi_structural_material_obj in enumerate(xmi_dict_value):
                    try:
                        xmi_structural_material, error_logs = XmiStructuralMaterial.from_xmi_dict_obj(
                            xmi_structural_material_obj)
                        if xmi_structural_material:
                            self.entities.append(xmi_structural_material)
                        self.errors.extend(error_logs)
                    except Exception as e:
                        self.errors.append(
                            ErrorLog(xmi_dict_key, index, str(e)))
                # check for duplicates after all xmi_structural_material_objs have been instantiated

            if xmi_dict_key == "StructuralPointConnection":
                for index, xmi_structural_point_connection_obj in enumerate(xmi_dict_value):
                    try:
                        xmi_structural_point_connection, error_logs = XmiStructuralPointConnection.from_xmi_dict_obj(
                            xmi_structural_point_connection_obj)
                        if xmi_structural_point_connection:
                            self.entities.append(
                                xmi_structural_point_connection)
                        self.errors.extend(error_logs)
                    except Exception as e:
                        self.errors.append(
                            ErrorLog(xmi_dict_key, index, str(e)))
                # check for duplicate names and id after all xmi_structural_point_connection_objs have been instantiated

            if xmi_dict_key == "StructuralCrossSection":
                for index, xmi_structural_cross_section_obj in enumerate(xmi_dict_value):
                    try:
                        xmi_structural_material_found_in_xmi_manager = None

                        if 'Material' in xmi_structural_cross_section_obj:
                            xmi_structural_material_name_to_find: str = xmi_structural_cross_section_obj[
                                'Material']
                            xmi_structural_material_found_in_xmi_manager = next(
                                (inst for inst in self.entities
                                 if inst.name == xmi_structural_material_name_to_find
                                 and isinstance(inst, XmiStructuralMaterial)),
                                None
                            )
                        else:
                            raise XmiMissingReferenceInstanceError(
                                "Material Attribute in xmi_dict is missing")

                        xmi_structural_cross_section, error_logs = XmiStructuralCrossSection.from_xmi_dict_obj(
                            xmi_structural_cross_section_obj,
                            material=xmi_structural_material_found_in_xmi_manager
                        )
                        if xmi_structural_cross_section:
                            self.entities.append(xmi_structural_cross_section)
                        self.errors.extend(error_logs)
                    except Exception as e:
                        self.errors.append(
                            ErrorLog(xmi_dict_key, index, str(e)))
