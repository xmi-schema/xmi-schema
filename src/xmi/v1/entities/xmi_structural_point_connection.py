# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseEntity
from ..geometries.xmi_point_3d import XmiPoint3D


class XmiStructuralPointConnection(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_point',
                                           '_storey')

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot != "_entity_type"]

    def __init__(self,
                 point: XmiPoint3D,
                 storey: str = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs):
        entity_type = "XmiStructuralPointConnection"

        # Check for mutual exclusivity, things that are optional should be inside any
        # if kwargs and any([storey, id, name, description, ifcguid]):
        #     raise ValueError(
        #         "Please use either standard parameters or kwargs, not both.")

        # # Ensure point is provided
        if point is None:
            raise ValueError(
                "The 'point' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id,
                         name=name,
                         ifcguid=ifcguid,
                         description=description,
                         entity_type=entity_type
                         )

        # Initialize attributes
        self.set_attributes(point, storey, **kwargs)

    def set_attributes(self, point, storey, **kwargs):
        attributes = [
            ('point', point),
            ('storey', storey)
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
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("point should be an XmiPoint3D")
        self._point = value

    @property
    def storey(self):
        return self._storey

    @storey.setter
    def storey(self, value):
        if not isinstance(value, str):
            raise TypeError("Storey should be an str")
        self._storey = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiStructuralPointConnection:
        error_logs = []
        processed_data = obj.copy()

        for attr in cls._attributes_needed:
            if attr not in obj:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        try:
            instance = cls(
                **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating StructuralPointConnection: {obj}"))

        return instance, error_logs

    @classmethod
    def from_xmi_dict_obj(cls, xmi_dict_obj: dict):
        # Define a mapping from snake_case keys to custom keys
        KEY_MAPPING = {
            "Name": "name",
            # "X": "x",
            # "Y": "y",
            # "Z": "z",
            "Storey": "storey",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid"
        }
        instance = None
        error_logs = []
        processed_data = {KEY_MAPPING.get(
            key, key): value for key, value in xmi_dict_obj.items()}

        instance, error_logs_found = cls.from_dict(
            processed_data)

        error_logs.extend(error_logs_found)

        return instance, error_logs
