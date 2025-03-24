from enum import unique, Enum
from .xmi_enums import XmiEnum


@unique
class XmiShapeEnum(XmiEnum):
    RECTANGULAR = "Rectangular"
    CIRCULAR = "Circular"
    L_SHAPE = "L Shape"
    T_SHAPE = "T Shape"
    C_SHAPE = "C Shape"
    I_SHAPE = "I Shape"
    SQUARE_HOLLOW = "Square Hollow"
    RECTANGULAR_HOLLOW = "Rectangular Hollow"
    OTHERS = "Others"
