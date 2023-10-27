# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseGeometry


class XmiPoint3D(XmiBaseGeometry):

    __slots__ = ('_x', '_y', '_z')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 x: float,
                 y: float,
                 z: float,
                 **kwargs):

        # Check for mutual exclusivity
        if kwargs and any([x, y, z]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # Ensure material_type is provided
        if x is None and 'x' not in kwargs:
            raise ValueError(
                "The 'x' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if y is None and 'y' not in kwargs:
            raise ValueError(
                "The 'y' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if z is None and 'z' not in kwargs:
            raise ValueError(
                "The 'z' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__()

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
