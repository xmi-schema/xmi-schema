from enum import Enum, NoAlias


class XmiEnum(Enum):
    _settings_ = NoAlias
    _fields_ = ['value', 'attribute']

    @classmethod
    def from_name(cls, name_str):
        try:
            return cls[name_str]
        except KeyError:
            return None  # Or raise a custom exception if you prefer

    @classmethod
    def from_attribute(cls, attribute_str):
        for member in cls:
            if member.attribute == attribute_str:
                return member
        return None  # Or raise a custom exception if you prefer


class XmiUnitEnum(XmiEnum):
    METER3 = 1, "m^3"
    METER2 = 2, "m^2"
    METER = 3, "m"
    METER4 = 4, "m^4"
    MILLIMETER4 = 5, "mm^4"
    MILLIMETER = 6, "mm"
    CENTIMETER = 7, "cm"


class XmiSegmentEnum(XmiEnum):
    LINE = 1, "Line"
    CIRCULAR_ARC = 2, "Circular Arc"
    PARABOLIC_ARC = 3, "Parabolic Arc"
    BEZIER = 4, "Bezier"
    SPLINE = 5, "Spline"
    OTHERS = 6, "Others"
