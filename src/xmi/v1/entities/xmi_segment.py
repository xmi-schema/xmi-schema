# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..entities.xmi_structural_point_connection import XmiStructuralPointConnection

from ..geometries.xmi_geometry import XmiBaseGeometry

from ..xmi_base import XmiBaseEntity


class XmiSegment(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_geometry',
                                           '_position'
                                           )

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 geometry: XmiBaseGeometry,
                 position: int,
                 start_node: XmiStructuralPointConnection,
                 end_node: XmiStructuralPointConnection,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs):

        # Ensure material_type is provided
        if geometry is None:
            raise ValueError(
                "The 'geometry' parameter is compulsory and must be provided.")

        # Ensure material_type is provided
        if position is None:
            raise ValueError(
                "The 'position' parameter is compulsory and must be provided.")

        # Ensure material_type is provided
        if start_node is None:
            raise ValueError(
                "The 'start_node' parameter is compulsory and must be provided.")

        # Ensure material_type is provided
        if end_node is None:
            raise ValueError(
                "The 'end_node' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description)

    def set_attributes(self,
                       geometry: XmiBaseGeometry,
                       position: int,
                       start_node: XmiStructuralPointConnection,
                       end_node: XmiStructuralPointConnection,
                       **kwargs):
        attributes = [
            ('geometry', geometry),
            ('position', position),
            ('start_node', start_node),
            ('end_node', end_node)
        ]

        for attr_name, attr_value in attributes:
            value = kwargs.get(attr_name, attr_value)
            try:
                setattr(self, attr_name, value)
            except AttributeError as e:
                print(
                    f"Caught an AttributeError while setting {attr_name}: {e}")
                setattr(self, attr_name, None)

    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, value):
        if not isinstance(value, XmiBaseGeometry):
            raise TypeError(
                "geometry should be an XmiBaseGeometry")
        self._geometry = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "position should be of type int")
        self._position = value

    @property
    def start_node(self):
        return self._start_node

    @start_node.setter
    def start_node(self, value):
        if not isinstance(value, XmiStructuralPointConnection):
            raise TypeError(
                "start_node should be of type XmiStructuralPointConnection")
        self._start_node = value

    @property
    def end_node(self):
        return self._end_node

    @end_node.setter
    def end_node(self, value):
        if not isinstance(value, XmiStructuralPointConnection):
            raise TypeError(
                "end_node should be of type XmiStructuralPointConnection")
        self._end_node = value
