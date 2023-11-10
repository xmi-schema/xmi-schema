# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseEntity
from .xmi_base_geometry import XmiBaseGeometry


class XmiPoint3D(XmiBaseGeometry):

    __slots__ = XmiBaseEntity.__slots__ + ('_x', '_y', '_z')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot not in ('_ifcguid')]

    def __init__(self,
                 x: float,
                 y: float,
                 z: float,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs):

        # Check for mutual exclusivity, things that are optional should be inside any
        # if kwargs and any([
        #     id, name, description, ifcguid
        # ]):
        #     raise ValueError(
        #         "Please use either standard parameters or kwargs, not both.")

        # Ensure material_type is provided
        if x is None:
            raise ValueError(
                "The 'x' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if y is None:
            raise ValueError(
                "The 'y' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if z is None:
            raise ValueError(
                "The 'z' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description, **kwargs)

        # Initialize attributes
        self.set_attributes(x, y, z, **kwargs)

    def set_attributes(self, x, y, z, **kwargs):
        attributes = [
            ('x', x),
            ('y', y),
            ('z', z),
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
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("X should be an int or float")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Y should be an int or float")
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Z should be an int or float")
        self._z = value

    @property
    def storey(self):
        return self._storey

    @storey.setter
    def storey(self, value):
        if not isinstance(value, str):
            raise TypeError("Storey should be an str")
        self._storey = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiPoint3D:
        error_logs = []
        processed_data = obj.copy()

        for attr in cls.attributes_needed:
            if attr not in obj:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        x_found = processed_data['x']
        y_found = processed_data['y']
        z_found = processed_data['z']

        # remove compulsory keys for proper class instantiation
        del processed_data['x']
        del processed_data['y']
        del processed_data['z']
        try:
            instance = cls(
                x=x_found,
                y=y_found,
                z=z_found,
                **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating XmiPoint3D: {obj}"))

        return instance, error_logs

    @classmethod
    def from_xmi_dict_obj(cls, xmi_dict_obj: dict):
        # currently xmi_file doesnt support xmi id for reference, will assume structural_point_connection's id and name

        # Define a mapping from snake_case keys to custom keys
        KEY_MAPPING = {
            "Name": "name",
            "X": "x",
            "Y": "y",
            "Z": "z",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid",
        }
        instance = None
        error_logs = []
        processed_data = {KEY_MAPPING.get(
            key, key): value for key, value in xmi_dict_obj.items() if key in KEY_MAPPING}

        instance, error_logs_found = cls.from_dict(
            processed_data)

        error_logs.extend(error_logs_found)

        return instance, error_logs
