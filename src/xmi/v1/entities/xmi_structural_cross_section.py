# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..constants import *
from ..enums.xmi_structural_cross_section_enums import XmiStructuralCrossSectionShapeEnum

from ..xmi_errors import XmiInconsistentDataAttributeError
from .xmi_base import XmiBase
from .xmi_structural_material import XmiStructuralMaterial

"""
1. Need to standardize "Parameters" property

"""


class XmiStructuralCrossSection(XmiBase):
    __slots__ = XmiBase.__slots__ + ('_Material',
                                     '_Shape',
                                     '_Parameters',
                                     '_Area',
                                     '_Ix', '_Iy', "_rx", "_ry", "_Ex", "_Ey", "_Zx", "_Zy", "_J")

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 material: XmiStructuralMaterial,
                 shape: XmiStructuralCrossSectionShapeEnum,
                 parameters: list | tuple,
                 second_moment_of_area_x_axis: float | int | None = None,
                 second_moment_of_area_y_axis: float | int | None = None,
                 radius_of_gyration_x_axis: float | int | None = None,
                 radius_of_gyration_y_axis: float | int | None = None,
                 elastic_modulus_x_axis: float | int | None = None,
                 elastic_modulus_y_axis: float | int | None = None,
                 plastic_modulus_x_axis: float | int | None = None,
                 plastic_modulus_y_axis: float | int | None = None,
                 torsional_constant: float | int | None = None,
                 area: float | int | None = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs
                 ):

        # Check for mutual exclusivity
        if kwargs and any([
                second_moment_of_area_x_axis,
                second_moment_of_area_y_axis,
                radius_of_gyration_x_axis,
                radius_of_gyration_y_axis,
                elastic_modulus_x_axis,
                elastic_modulus_y_axis,
                plastic_modulus_x_axis,
                plastic_modulus_y_axis,
                torsional_constant,
                area,
                id, name, description, ifcguid
        ]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # Ensure material_type is provided
        if material is None and 'Material' not in kwargs:
            raise ValueError(
                "The 'material' parameter is compulsory and must be provided.")

        # Ensure material_type is provided
        if shape is None and 'Shape' not in kwargs:
            raise ValueError(
                "The 'shape' parameter is compulsory and must be provided.")

        # Ensure material_type is provided
        if parameters is None and 'Parameters' not in kwargs:
            raise ValueError(
                "The 'parameters' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description) if not kwargs else super().__init__(**kwargs)

        # Initialize attributes
        self.set_attributes(
            material,
            shape,
            parameters,
            second_moment_of_area_x_axis,
            second_moment_of_area_y_axis,
            radius_of_gyration_x_axis,
            radius_of_gyration_y_axis,
            elastic_modulus_x_axis,
            elastic_modulus_y_axis,
            plastic_modulus_x_axis,
            plastic_modulus_y_axis,
            torsional_constant,
            area,
            **kwargs)

    def set_attributes(self,
                       material,
                       shape,
                       parameters,
                       second_moment_of_area_x_axis,
                       second_moment_of_area_y_axis,
                       radius_of_gyration_x_axis,
                       radius_of_gyration_y_axis,
                       elastic_modulus_x_axis,
                       elastic_modulus_y_axis,
                       plastic_modulus_x_axis,
                       plastic_modulus_y_axis,
                       torsional_constant,
                       area,
                       **kwargs):
        attributes = [
            ('Material', material),
            ('Shape', shape),
            ('Parameters', parameters),
            ('Area', area),
            ('Ix', second_moment_of_area_x_axis),
            ('Iy', second_moment_of_area_y_axis),
            ('rx', radius_of_gyration_x_axis),
            ('ry', radius_of_gyration_y_axis),
            ('Ex', elastic_modulus_x_axis),
            ('Ey', elastic_modulus_y_axis),
            ('Zx', plastic_modulus_x_axis),
            ('Zy', plastic_modulus_y_axis),
            ('J', torsional_constant)
        ]

        for attr_name, attr_value in attributes:
            value = kwargs.get(attr_name, attr_value)
            try:
                setattr(self, attr_name, value)
            except AttributeError as e:
                print(
                    f"Caught an AttributeError while setting {attr_name}: {e}")
                setattr(self, attr_name, None)

    @property
    def Material(self):
        return self._Material

    @Material.setter
    def Material(self, value):
        if not isinstance(value, XmiStructuralMaterial):
            raise TypeError(
                "Material should be an XmiStructuralMaterial")
        self._Material = value

    @property
    def Shape(self):
        return self._Shape

    @Shape.setter
    def Shape(self, value):
        if not isinstance(value, XmiStructuralCrossSectionShapeEnum):
            raise TypeError(
                "Shape should be of type XmiStructuralCrossSectionShapeEnum")
        self._Shape = value

    # Similarly, for other properties:

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, value):
        # check if the datatype is correct
        if not isinstance(value, (list, tuple)):
            raise TypeError(
                "Parameters should be of type list or tuple")

        # check for quantity of params
        if self.Shape and self.Shape != XmiStructuralCrossSectionShapeEnum.OTHERS and value:
            param_required_length = self.Shape.get_quantity_of_cross_section_params()
            value_length = len(value)
            if value_length != param_required_length:
                raise XmiInconsistentDataAttributeError(
                    f"The parameter length is different than required XmiStructuralCrossSectionShapeEnum")
        # check for every item within the list of tuple to be an int or float value and all data needs to be at least 0.0
        for item in value:
            if not isinstance(item, (int, float)):
                raise ValueError(
                    f"All items must be instances of float or int, got {type(item)} instead.")
            if item < 0.0:
                raise ValueError(
                    f"Value cannot be smaller than 0"
                )
        self._Parameters = tuple(value)

    # to be considered optional as of now
    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError("Area should be of type float,int or None")
        if value is not None and value <= 0.0:
            raise ValueError("Area should be larger than 0.0")
        self._Area = value

    @property
    def Ix(self):
        return self._Ix

    @Ix.setter
    def Ix(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "Ix (Second Moment of Area - x axis) should be of type float,int or None")
        if value is not None and value <= 0.0:
            raise ValueError("Ix should be larger than 0.0")
        self._Ix = value

    @property
    def Iy(self):
        return self._Iy

    @Iy.setter
    def Iy(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "Iy (Second Moment of Area - y axis) should be of type float,int or None")
        if value is not None and value <= 0.0:
            raise ValueError("Iy should be larger than 0.0")
        self._Iy = value

    @property
    def rx(self):
        return self._rx

    @rx.setter
    def rx(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "rx (Radius of Gyration - x axis) should be of type float or None")
        if value is not None and value <= 0.0:
            raise ValueError("rx should be larger than 0.0")
        self._rx = value

    @property
    def ry(self):
        return self._ry

    @ry.setter
    def ry(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "ry (Radius of Gyration - y axis) should be of type float or None")
        if value is not None and value <= 0.0:
            raise ValueError("ry should be larger than 0.0")
        self._ry = value

    @property
    def Ex(self):
        return self._Ex

    @Ex.setter
    def Ex(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Ex (E Modulus - x axis) should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError("Ex should be larger than 0.0")
        self._Ex = value

    @property
    def Ey(self):
        return self._Ey

    @Ey.setter
    def Ey(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Ey (E Modulus - y axis) should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError("Ey should be larger than 0.0")
        self._Ey = value

    @property
    def J(self):
        return self._J

    @J.setter
    def J(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Torsional Constant should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError("Torsional Constant should be larger than 0.0")
        self._J = value
