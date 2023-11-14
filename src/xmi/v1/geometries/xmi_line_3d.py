# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .xmi_point_3d import XmiPoint3D
from .xmi_base_geometry import XmiBaseGeometry


class XmiLine3D(XmiBaseGeometry):
    __slots__ = ('_start_point', '_end_point')

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot != "_entity_type"]

    def __init__(self,
                 start_point: XmiPoint3D,
                 end_point: XmiPoint3D,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs):
        entity_type = "XmiLine3D"

        # Ensure material_type is provided
        if start_point is None:
            raise ValueError(
                "The 'start_point' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if end_point is None:
            raise ValueError(
                "The 'end_point' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id,
                         name=name,
                         ifcguid=ifcguid,
                         description=description,
                         entity_type=entity_type
                         )

        # Initialize attributes
        self.set_attributes(start_point, end_point, **kwargs)

    def set_attributes(self, start_point, end_point, **kwargs):
        attributes = [
            ('start_point', start_point),
            ('end_point', end_point),
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
    def start_point(self):
        return self._start_point

    @start_point.setter
    def start_point(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("start_point should be an XmiPoint3D")
        self._start_point = value

    @property
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("end_point should be an XmiPoint3D")
        self._end_point = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiPoint3D:
        error_logs = []
        processed_data = obj.copy()

        for attr in cls._attributes_needed:
            if attr not in obj:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        start_point_found = processed_data['start_point']
        end_point_found = processed_data['end_point']

        # remove compulsory keys for proper class instantiation
        del processed_data['start_point']
        del processed_data['end_point']
        try:
            instance = cls(
                start_point=start_point_found,
                end_point=end_point_found,
                **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating XmiLine3D: {obj}"))

        return instance, error_logs
