# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from math import sqrt, acos

from .xmi_point_3d import XmiPoint3D
from .xmi_base_geometry import XmiBaseGeometry


class XmiArc3D(XmiBaseGeometry):
    __slots__ = ('_begin_point', '_end_point')

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot != "_entity_type"]

    def __init__(self,
                 begin_point: XmiPoint3D,
                 end_point: XmiPoint3D,
                 center_point: XmiPoint3D,
                 radius: float = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs):

        entity_type = "XmiArc3D"

        # Ensure material_type is provided
        if begin_point is None:
            raise ValueError(
                "The 'begin_point' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if end_point is None:
            raise ValueError(
                "The 'end_point' parameter is compulsory and must be provided.")

        # Ensure material_type is provided
        if center_point is None:
            raise ValueError(
                "The 'center_point' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id,
                         name=name,
                         ifcguid=ifcguid,
                         description=description,
                         entity_type=entity_type
                         )

        # Initialize attributes
        self.set_attributes(begin_point, end_point, center_point, **kwargs)

    def set_attributes(self, begin_point, end_point, center_point, **kwargs):
        attributes = [
            ('begin_point', begin_point),
            ('end_point', end_point),
            ('center_point', center_point)
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
    def begin_point(self):
        return self._begin_point

    @begin_point.setter
    def begin_point(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("begin_point should be an XmiPoint3D")
        self._begin_point = value

    @property
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("end_point should be an XmiPoint3D")
        self._end_point = value

    @property
    def center_point(self):
        return self._center_point

    @center_point.setter
    def center_point(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("center_point should be an XmiPoint3D")
        self._center_point = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiPoint3D:
        error_logs = []
        processed_data = obj.copy()

        for attr in cls._attributes_needed:
            if attr not in obj:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        begin_point_found = processed_data['begin_point']
        end_point_found = processed_data['end_point']
        center_point_found = processed_data['center_point']

        # remove compulsory keys for proper class instantiation
        del processed_data['begin_point']
        del processed_data['end_point']
        del processed_data['center_point']
        try:
            instance = cls(
                begin_point=begin_point_found,
                end_point=end_point_found,
                **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating XmiLine3D: {obj}"))

        return instance, error_logs

    def get_length(self) -> float:
        # Calculate radius
        radius = sqrt((self.center_point.x - self.begin_point.x) ** 2 +
                      (self.center_point.y - self.begin_point.y) ** 2 +
                      (self.center_point.z - self.begin_point.z) ** 2)

        # Calculate vectors
        vector_a = (self.begin_point.x - self.center_point.x,
                    self.begin_point.y - self.center_point.y,
                    self.begin_point.z - self.center_point.z)
        vector_b = (self.end_point.x - self.center_point.x,
                    self.end_point.y - self.center_point.y,
                    self.end_point.z - self.center_point.z)

        # Dot product and magnitude of vectors
        dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
        magnitude_a = sqrt(sum(a * a for a in vector_a))
        magnitude_b = sqrt(sum(b * b for b in vector_b))

        # Calculate angle in radians
        angle = acos(dot_product / (magnitude_a * magnitude_b))

        # Calculate arc length
        arc_length = radius * angle
        return arc_length
