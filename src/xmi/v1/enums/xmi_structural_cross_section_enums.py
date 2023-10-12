# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .xmi_enums import XmiEnum
from enum import unique, Enum

# After adding these shapes, an image of how it is being defined is needed


@unique
class XmiStructuralCrossSectionShapeEnum(Enum):
    RECTANGULAR = (1, "Rectangular", 2, ("H", "B"))
    CIRCULAR = (2, "Circular", 1, ("D"))
    L_SHAPE = (3, "L Shape", 4, ("H", "B", "T", "t"))
    T_SHAPE = (4, "T Shape", 4, ("H", "B", "T", "t"))
    C_SHAPE = (5, "C Shape", 5, ("H", "B", "T1", "T2", "t"))
    I_SHAPE = (6, "I Shape", 5, ("D", "B", "T", "t", "r"))
    SQUARE_HOLLOW = (7, "Square Hollow", 2, ("D", "t"))
    RECTANGULAR_HOLLOW = (8, "Rectangular Hollow", 3, ("D", "B", "t"))
    OTHERS = (9, "Others", 0, ())

    @classmethod
    def from_name_get_enum(cls, name_str):
        try:
            return cls[name_str]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def from_attribute_get_enum(cls, attribute_str: str):
        for member in cls:
            if member.value[1] == attribute_str:
                return member
        return None  # Or raise a custom exception if you prefer

    @classmethod
    def from_name_get_enum_attribute(cls, name_str: str):
        try:
            return cls[name_str].value[1]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def get_attribute(cls):
        try:
            return cls.value[1]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def from_name_get_enum_value(cls, name_str: str):
        try:
            return cls[name_str].value[0]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def get_quantity_of_cross_section_params(cls, enum: Enum):
        try:
            return enum.value[2]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    def get_quantity_of_cross_section_params(self):
        try:
            return self.value[2]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def get_cross_section_params(cls):
        try:
            return cls.value[3]
        except KeyError:
            return None  # Or raise a custom exception if you prefer
