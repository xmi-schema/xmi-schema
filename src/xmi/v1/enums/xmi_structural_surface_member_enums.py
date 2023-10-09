from enum import Enum


class XmiStructuralSurfaceMemberTypeEnum(Enum):
    SLAB = "Beam"
    WALL = "Column"
    PAD_FOOTING = "Bracing"
    STRIP_FOOTING = "Other"
    PILECAP = "Pilecap"  # i think this shouldn't be here
    ROOF_PANEL = "RoofPanel"  # this sounds like archi. should not be here
    WALL_PANEL = "WallPanel"  # this sounds like archi. should not be here
    RAFT = "Raft"  # For future changes to be shifted to foundation type elements


class XmiStructuralSurfaceMemberSpanTypeEnum(Enum):
    ONE_WAY = "OneWay"
    TWO_WAY = "TwoWay"


class XmiStructuralSurfaceMemberSystemPlaneEnum(Enum):
    BOTTOM = "Bottom"
    TOP = "Top"
    MIDDLE = "Middle"
    LEFT = "Left"
    RIGHT = "Right"
