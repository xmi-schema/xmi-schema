from .xmi_enums import XmiEnum
from enum import unique


@unique
class XmiStructuralSurfaceMemberTypeEnum(XmiEnum):
    SLAB = (1, "Beam")
    WALL = (2, "Column")
    PAD_FOOTING = (3, "Bracing")
    STRIP_FOOTING = (4, "Other")
    PILECAP = (5, "Pilecap")  # i think this shouldn't be here
    ROOF_PANEL = (6, "RoofPanel")  # this sounds like archi. should not be here
    WALL_PANEL = (7, "WallPanel")  # this sounds like archi. should not be here
    # For future changes to be shifted to foundation type elements
    RAFT = (8, "Raft")


@unique
class XmiStructuralSurfaceMemberSpanTypeEnum(XmiEnum):
    ONE_WAY = (1, "OneWay")
    TWO_WAY = (2, "TwoWay")


@unique
class XmiStructuralSurfaceMemberSystemPlaneEnum(XmiEnum):
    BOTTOM = (1, "Bottom")
    TOP = (2, "Top")
    MIDDLE = (3, "Middle")
    LEFT = (4, "Left")
    RIGHT = (5, "Right")
