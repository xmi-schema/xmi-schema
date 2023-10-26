from .xmi_enums import XmiEnum
from enum import unique


@unique
class XmiStructuralCurveMemberTypeEnum(XmiEnum):
    BEAM = (1, "Beam")
    COLUMN = (2, "Column")
    BRACING = (3, "Bracing")
    OTHER = (4, "Other")


@unique
class XmiStructuralCurveMemberSystemLineEnum(XmiEnum):
    TOP_MIDDLE = (1, "TopMiddle")
    TOP_LEFT = (2, "TopLeft")
    TOP_RIGHT = (3, "TopRight")
    MIDDLE_MIDDLE = (4, "MiddleMiddle")
    MIDDLE_LEFT = (5, "MiddleLeft")
    MIDDLE_RIGHT = (6, "MiddleRight")
    BOTTOM_LEFT = (7, "BottomLeft")
    BOTTOM_MIDDLE = (8, "BottomMiddle")
    BOTTOM_RIGHT = (9, "BottomRight")
