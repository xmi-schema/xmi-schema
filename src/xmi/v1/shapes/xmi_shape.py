from ..enums.xmi_shape_enums import XmiShapeEnum

# RECTANGULAR = (1, "Rectangular", 2, ("H", "B"))
# CIRCULAR = (2, "Circular", 1, ("D"))
# L_SHAPE = (3, "L Shape", 4, ("H", "B", "T", "t"))
# T_SHAPE = (4, "T Shape", 4, ("H", "B", "T", "t"))
# C_SHAPE = (5, "C Shape", 5, ("H", "B", "T1", "T2", "t"))
# I_SHAPE = (6, "I Shape", 5, ("D", "B", "T", "t", "r"))
# SQUARE_HOLLOW = (7, "Square Hollow", 2, ("D", "t"))
# RECTANGULAR_HOLLOW = (8, "Rectangular Hollow", 3, ("D", "B", "t"))
# OTHERS = (9, "Others", 0, ())


class XmiShape():

    def __init__(self, shape: XmiShapeEnum,
                 parameter_quantity: int,
                 parameter_names: tuple[str]) -> None:
        self.shape: XmiShapeEnum = shape
        self.parameter_quantity: int = parameter_quantity
        self.parameter_names: tuple[str] = parameter_names


class XmiShapeRectangle(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.RECTANGULAR
        parameter_quantity = 2
        parameter_names = ("H", "B")

        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeCircle(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.CIRCULAR
        parameter_quantity = 1
        parameter_names = ("D")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeL(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.L_SHAPE
        parameter_quantity = 4
        parameter_names = ("H", "B", "T", "t")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeC(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.C_SHAPE
        parameter_quantity = 5
        parameter_names = ("H", "B", "T1", "T2", "t")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeI(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.I_SHAPE
        parameter_quantity = 5
        parameter_names = ("D", "B", "T", "t", "r")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeT(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.T_SHAPE
        parameter_quantity = 4
        parameter_names = ("H", "B", "T", "t")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeSquareHollow(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.SQUARE_HOLLOW
        parameter_quantity = 2
        parameter_names = ("D", "t")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeRectangularHollow(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.RECTANGULAR_HOLLOW
        parameter_quantity = 3
        parameter_names = ("D", "B", "t")
        super().__init__(shape, parameter_quantity, parameter_names)


class XmiShapeOthers(XmiShape):
    def __init__(self) -> None:
        shape = XmiShapeEnum.OTHERS
        parameter_quantity = 0
        parameter_names = tuple()
        super().__init__(shape, parameter_quantity, parameter_names)
