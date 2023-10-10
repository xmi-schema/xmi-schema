from .xmi_enums import XmiEnum
from enum import unique

# After adding these shapes, an image of how it is being defined is needed


@unique
class XmiStructuralCrossSectionShapeEnum(XmiEnum):
    RECTANGULAR = (1, "Rectangular")
    CIRCULAR = (2, "Circular")
    L_SHAPE = (3, "L Shape")
    T_SHAPE = (4, "T Shape")
    C_SHAPE = (5, "C Shape")
    I_SHAPE = (6, "I Shape")
    H_SHAPE = (7, "H Shape")  # For Structural Columns, to verify with vendor
    SQUARE_HOLLOW = (8, "Square Hollow")
    RECTANGULAR_HOLLOW = (9, "Rectangular Hollow")
    OTHERS = (10, "Others")
