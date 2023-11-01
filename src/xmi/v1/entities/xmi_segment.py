# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

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

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description)

    def set_attributes(self,
                       geometry: XmiBaseGeometry,
                       position: int,
                       **kwargs):
        attributes = [
            ('geometry', geometry),
            ('position', position),
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
