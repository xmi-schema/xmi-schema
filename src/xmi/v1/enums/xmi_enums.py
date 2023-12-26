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
            if member.value == attribute_str:
                return member
        return None  # Or raise a custom exception if you prefer


@unique
class XmiUnitEnum(XmiEnum):
    METER3 = "m^3"
    METER2 = "m^2"
    METER = "m"
    METER4 = "m^4"
    MILLIMETER4 = "mm^4"
    MILLIMETER = "mm"
    CENTIMETER = "cm"
    MILLIMETER3 = "mm^3"
    MILLIMETER2 = "mm^2"
    SECOND = "sec"


@unique
class XmiSegmentTypeEnum(XmiEnum):
    LINE = "Line"
    CIRCULAR_ARC = "Circular Arc"
    PARABOLIC_ARC = "Parabolic Arc"
    BEZIER = "Bezier"
    SPLINE = "Spline"
    OTHERS = "Others"

    def get_geometry_class(self):
        try:
            if len(self.value) < 3:
                return None
            return self.value[2]
        except KeyError:
            return None  # Or raise a custom exception if you prefer
