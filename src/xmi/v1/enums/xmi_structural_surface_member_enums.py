from .xmi_enums import XmiEnum
from enum import unique


@unique
class XmiStructuralSurfaceMemberTypeEnum(XmiEnum):
    SLAB = "Slab"
    WALL = "Wall"
    PAD_FOOTING = "PadFooting"
    STRIP_FOOTING = "StripFooting"
    PILECAP = "Pilecap"  # i think this shouldn't be here
    ROOF_PANEL = "RoofPanel"  # this sounds like archi. should not be here
    WALL_PANEL = "WallPanel"  # this sounds like archi. should not be here
    # For future changes to be shifted to foundation type elements
    RAFT = "Raft"


@unique
class XmiStructuralSurfaceMemberSpanTypeEnum(XmiEnum):
    ONE_WAY = "OneWay"
    TWO_WAY = "TwoWay"


@unique
class XmiStructuralSurfaceMemberSystemPlaneEnum(XmiEnum):
    BOTTOM = "Bottom"
    TOP = "Top"
    MIDDLE = "Middle"
    LEFT = "Left"
    RIGHT = "Right"
