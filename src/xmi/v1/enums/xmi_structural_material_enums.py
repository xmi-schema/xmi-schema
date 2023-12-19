from .xmi_enums import XmiEnum
from enum import unique


@unique
class XmiStructuralMaterialTypeEnum(XmiEnum):
    CONCRETE = "Concrete"
    STEEL = "Steel"
    TIMBER = "Timber"
    ALUMINIUM = "Aluminium"
    COMPOSITE = "Composite"
    MASONRY = "Masonry"
    OTHERS = "Others"
    REBAR = "Rebar"  # to be removed
    TENDON = "Tendon"  # to be removed
