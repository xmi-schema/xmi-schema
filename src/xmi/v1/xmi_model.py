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
    def __init__(self,
                 name: str = None,
                 xmi_version: str = None,
                 application_name: str = None,
                 application_version: str = None
                 ):

        self.entities: list[XmiBaseEntity] = []
        self.relationships: list[XmiBaseRelationship] = []
        self.histories = []
        self.errors: list[ErrorLog] = []
        self.name = name
        self.xmi_version = xmi_version
        self.application_name = application_name
        self.application_version = application_version

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("'name' should be an str or None")
        self._name = value

    @property
    def xmi_version(self):
        return self._xmi_version

    @xmi_version.setter
    def xmi_version(self, value):
        if value is not None and not isinstance(value, (str)):
            raise TypeError("'xmi_version' should be a string")
        self._xmi_version = value

    @property
    def application_name(self):
        return self._application_name

    @application_name.setter
    def application_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("'application_name' should be a string")
        self._application_name = value

    @property
    def application_version(self):
        return self._application_version

    @application_version.setter
    def application_version(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("'application_version' should be a string")
        self._application_version = value

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

    def find_relationships_by_target(self, target: XmiBaseEntity) -> list[XmiBaseRelationship]:
        return [rel for rel in self.relationships if rel.target == target]

    def find_relationships_by_source(self, source: XmiBaseEntity) -> list[XmiBaseRelationship]:
        return [rel for rel in self.relationships if rel.source == source]
