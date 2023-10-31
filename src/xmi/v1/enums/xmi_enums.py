from enum import Enum, unique
from ..geometries.xmi_line_3d import XmiLine3D
from ..geometries.xmi_arc_3d import XmiArc3D


@unique
class XmiEnum(Enum):

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

    def get_attribute_value(cls):
        try:
            return cls.value[1]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def get_attribute_value(cls, enum: Enum):
        try:
            return enum.value[1]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def from_name_get_enum_value(cls, name_str: str):
        try:
            return cls[name_str].value[0]
        except KeyError:
            return None  # Or raise a custom exception if you prefer


@unique
class XmiUnitEnum(XmiEnum):
    METER3 = (1, "m^3")
    METER2 = (2, "m^2")
    METER = (3, "m")
    METER4 = (4, "m^4")
    MILLIMETER4 = (5, "mm^4")
    MILLIMETER = (6, "mm")
    CENTIMETER = (7, "cm")
    MILLIMETER3 = (8, "mm^3")
    MILLIMETER2 = (9, "mm^2")
    SECOND = (10, "sec")


@unique
class XmiSegmentTypeEnum(XmiEnum):
    LINE = (1, "Line", XmiLine3D)
    CIRCULAR_ARC = (2, "Circular Arc", XmiArc3D)
    PARABOLIC_ARC = (3, "Parabolic Arc")
    BEZIER = (4, "Bezier")
    SPLINE = (5, "Spline")
    OTHERS = (6, "Others")

    def get_geometry_class(self):
        try:
            if len(self.value) < 3:
                return None
            return self.value[2]
        except KeyError:
            return None  # Or raise a custom exception if you prefer
