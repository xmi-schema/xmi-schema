from .xmi_enums import XmiEnum
from enum import unique


@unique
class XmiStructuralCurveMemberTypeEnum(XmiEnum):
    BEAM = "Beam"
    COLUMN = "Column"
    BRACING = "Bracing"
    OTHER = "Other"


@unique
class XmiStructuralCurveMemberSystemLineEnum(XmiEnum):
    TOP_MIDDLE = "TopMiddle"
    TOP_LEFT = "TopLeft"
    TOP_RIGHT = "TopRight"
    MIDDLE_MIDDLE = "MiddleMiddle"
    MIDDLE_LEFT = "MiddleLeft"
    MIDDLE_RIGHT = "MiddleRight"
    BOTTOM_LEFT = "BottomLeft"
    BOTTOM_MIDDLE = "BottomMiddle"
    BOTTOM_RIGHT = "BottomRight"
