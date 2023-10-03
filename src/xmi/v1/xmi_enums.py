from enum import Enum


class XmiStructuralCurveMemberTypeEnum(Enum):
    BEAM = "Beam"
    COLUMN = "Column"
    BRACING = "Bracing"
    OTHER = "Other"


class XmiStructuralCurveMemberSegmentEnum(Enum):
    LINE = "Line"
    CIRCULAR_ARC = "Circular Arc"
    PARABOLIC_ARC = "Parabolic Arc"
    BEZIER = "Bezier"
    SPLINE = "Spline"
    OTHERS = "Others"


class XmiUnitEnum(Enum):
    METER3 = "m^3"
    METER2 = "m^2"
    METER = "m"
    METER4 = "m^4"
    MILLIMETER4 = "mm^4"
    MILLIMETER = "mm"
    CENTIMETER = "cm"
