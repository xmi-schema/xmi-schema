from enum import Enum


class XmiStructuralCurveMemberTypeEnum(Enum):
    BEAM = "Beam"
    COLUMN = "Column"
    BRACING = "Bracing"
    OTHER = "Other"


class XmiSegmentEnum(Enum):
    LINE = "Line"
    CIRCULAR_ARC = "Circular Arc"
    PARABOLIC_ARC = "Parabolic Arc"
    BEZIER = "Bezier"
    SPLINE = "Spline"
    OTHERS = "Others"
