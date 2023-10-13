# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .xmi_base import XmiBase


class XmiStructuralPointConnection(XmiBase):
    __slots__ = XmiBase.__slots__ + ('_Storey', '_X',
                                     '_Y', '_Z')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 x: float,
                 y: float,
                 z: float,
                 storey: str = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None, **kwargs):

        # Check for mutual exclusivity
        if kwargs and any([x, y, z, storey]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # Ensure material_type is provided
        if x is None and 'X' not in kwargs:
            raise ValueError(
                "The 'x' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if y is None and 'Y' not in kwargs:
            raise ValueError(
                "The 'y' parameter is compulsory and must be provided.")
        # Ensure material_type is provided
        if z is None and 'Z' not in kwargs:
            raise ValueError(
                "The 'z' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description) if not kwargs else super().__init__(**kwargs)

        # Initialize attributes
        self.set_attributes(x, y, z, storey, **kwargs)

    def set_attributes(self, x, y, z, storey, **kwargs):
        attributes = [
            ('X', x),
            ('Y', y),
            ('Z', z),
            ('Storey', storey)
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
    def X(self):
        return self._X

    @X.setter
    def X(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("X should be an int or float")
        self._X = value

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Y should be an int or float")
        self._Y = value

    @property
    def Z(self):
        return self._Z

    @Z.setter
    def Z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Z should be an int or float")
        self._Z = value

    @property
    def Storey(self):
        return self._Storey

    @Storey.setter
    def Storey(self, value):
        if not isinstance(value, str):
            raise TypeError("Storey should be an str")
        self._Storey = value

    @classmethod
    def from_dict(cls, data: dict) -> XmiStructuralPointConnection:
        error_logs = []
        processed_data = data.copy()

        for attr in cls.attributes_needed:
            if attr not in data:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None
        return cls(processed_data['X'],
                   processed_data['Y'],
                   processed_data['Z']
                   ** processed_data), error_logs
