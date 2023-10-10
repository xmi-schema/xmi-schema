from .xmi_enums import XmiEnum


class XmiStructuralCurveMemberTypeEnum(XmiEnum):
    BEAM = 1, "Beam"
    COLUMN = 2, "Column"
    BRACING = 3, "Bracing"
    OTHER = 4, "Other"
