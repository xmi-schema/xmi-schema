from enum import Enum, unique
from typing import Optional
from pydantic import BaseModel, field_validator

@unique
class XmiBaseEnum(str, Enum): 
    @classmethod
    def from_name_get_enum(cls, name_str: str) -> Optional["XmiBaseEnum"]:
        try:
            return cls[name_str]
        except KeyError:
            return None

    @classmethod
    def from_attribute_get_enum(cls, attribute_str: str) -> Optional["XmiBaseEnum"]:
        for member in cls:
            if member.value == attribute_str:
                return member
        return None

@unique
class XmiUnitEnum(XmiBaseEnum):
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
class XmiSegmentTypeEnum(XmiBaseEnum):
    LINE = "Line"
    CIRCULAR_ARC = "Circular Arc"
    PARABOLIC_ARC = "Parabolic Arc"
    BEZIER = "Bezier"
    SPLINE = "Spline"
    OTHERS = "Others"

    def get_geometry_class(self):
        from ..geometries.xmi_line_3d import XmiLine3D
        from ..geometries.xmi_arc_3d import XmiArc3D

        mapping = {
            XmiSegmentTypeEnum.LINE: XmiLine3D,
            XmiSegmentTypeEnum.CIRCULAR_ARC: XmiArc3D,
        }
        return mapping.get(self)