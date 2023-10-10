from enum import Enum, unique


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

    @classmethod
    def from_enum_get_enum_attribute(cls, enum: Enum):
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


@unique
class XmiSegmentEnum(XmiEnum):
    LINE = (1, "Line")
    CIRCULAR_ARC = (2, "Circular Arc")
    PARABOLIC_ARC = (3, "Parabolic Arc")
    BEZIER = (4, "Bezier")
    SPLINE = (5, "Spline")
    OTHERS = (6, "Others")
