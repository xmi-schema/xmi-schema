# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..constants import *
from ..enums.xmi_structural_cross_section_enums import XmiStructuralCrossSectionShapeEnum

from ..xmi_errors import XmiInconsistentDataAttributeError
from ..xmi_base import XmiBaseEntity, XmiBaseRelationship
from .xmi_structural_material import XmiStructuralMaterial

"""
1. Need to standardize "Parameters" property

"""


class XmiStructuralCrossSection(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_material',
                                           '_shape',
                                           '_parameters',
                                           '_area',
                                           '_second_moment_of_area_x_axis',
                                           '_second_moment_of_area_y_axis',
                                           "_radius_of_gyration_x_axis",
                                           "_radius_of_gyration_y_axis",
                                           "_elastic_modulus_x_axis",
                                           "_elastic_modulus_y_axis",
                                           "_plastic_modulus_x_axis",
                                           "_plastic_modulus_y_axis",
                                           "_torsional_constant")

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 material: XmiStructuralMaterial,
                 shape: XmiStructuralCrossSectionShapeEnum,
                 parameters: list | tuple,
                 area: float | int | None = None,
                 second_moment_of_area_x_axis: float | int | None = None,
                 second_moment_of_area_y_axis: float | int | None = None,
                 radius_of_gyration_x_axis: float | int | None = None,
                 radius_of_gyration_y_axis: float | int | None = None,
                 elastic_modulus_x_axis: float | int | None = None,
                 elastic_modulus_y_axis: float | int | None = None,
                 plastic_modulus_x_axis: float | int | None = None,
                 plastic_modulus_y_axis: float | int | None = None,
                 torsional_constant: float | int | None = None,
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
            ('material', material),
            ('shape', shape),
            ('parameters', parameters),
            ('area', area),
            ('second_moment_of_area_x_axis', second_moment_of_area_x_axis),
            ('second_moment_of_area_y_axis', second_moment_of_area_y_axis),
            ('radius_of_gyration_x_axis', radius_of_gyration_x_axis),
            ('radius_of_gyration_y_axis', radius_of_gyration_y_axis),
            ('elastic_modulus_x_axis', elastic_modulus_x_axis),
            ('elastic_modulus_y_axis', elastic_modulus_y_axis),
            ('plastic_modulus_x_axis', plastic_modulus_x_axis),
            ('plastic_modulus_y_axis', plastic_modulus_y_axis),
            ('torsional_constant', torsional_constant)
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
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, XmiStructuralMaterial):
            raise TypeError(
                "Material should be an XmiStructuralMaterial")
        self._material = value

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        if not isinstance(value, XmiStructuralCrossSectionShapeEnum):
            raise TypeError(
                "Shape should be of type XmiStructuralCrossSectionShapeEnum")
        self._shape = value

    # Similarly, for other properties:

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        # check if the datatype is correct
        if not isinstance(value, (list, tuple)):
            raise TypeError(
                "Parameters should be of type list or tuple")

        # check for quantity of params
        if self.shape and self.shape != XmiStructuralCrossSectionShapeEnum.OTHERS and value:
            param_required_length = self.shape.get_quantity_of_cross_section_params()
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
        self._parameters = tuple(value)

    # to be considered optional as of now
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError("Area should be of type float,int or None")
        if value is not None and value <= 0.0:
            raise ValueError("Area should be larger than 0.0")
        self._area = value

    @property
    def second_moment_of_area_x_axis(self):
        return self._second_moment_of_area_x_axis

    @second_moment_of_area_x_axis.setter
    def second_moment_of_area_x_axis(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "Ix (Second Moment of Area - x axis) should be of type float,int or None")
        if value is not None and value <= 0.0:
            raise ValueError("Ix should be larger than 0.0")
        self._second_moment_of_area_x_axis = value

    @property
    def second_moment_of_area_y_axis(self):
        return self._second_moment_of_area_y_axis

    @second_moment_of_area_y_axis.setter
    def second_moment_of_area_y_axis(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "Iy (Second Moment of Area - y axis) should be of type float,int or None")
        if value is not None and value <= 0.0:
            raise ValueError("Iy should be larger than 0.0")
        self._second_moment_of_area_y_axis = value

    @property
    def radius_of_gyration_x_axis(self):
        return self._radius_of_gyration_x_axis

    @radius_of_gyration_x_axis.setter
    def radius_of_gyration_x_axis(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "rx (Radius of Gyration - x axis) should be of type float or None")
        if value is not None and value <= 0.0:
            raise ValueError("rx should be larger than 0.0")
        self._radius_of_gyration_x_axis = value

    @property
    def radius_of_gyration_y_axis(self):
        return self._radius_of_gyration_y_axis

    @radius_of_gyration_y_axis.setter
    def radius_of_gyration_y_axis(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "ry (Radius of Gyration - y axis) should be of type float or None")
        if value is not None and value <= 0.0:
            raise ValueError("ry should be larger than 0.0")
        self._radius_of_gyration_y_axis = value

    @property
    def elastic_modulus_x_axis(self):
        return self._elastic_modulus_x_axis

    @elastic_modulus_x_axis.setter
    def elastic_modulus_x_axis(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Ex (E Modulus - x axis) should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError("Ex should be larger than 0.0")
        self._elastic_modulus_x_axis = value

    @property
    def elastic_modulus_y_axis(self):
        return self._elastic_modulus_y_axis

    @elastic_modulus_y_axis.setter
    def elastic_modulus_y_axis(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Ey (E Modulus - y axis) should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError("Ey should be larger than 0.0")
        self._elastic_modulus_y_axis = value

    @property
    def torsional_constant(self):
        return self._torsional_constant

    @torsional_constant.setter
    def torsional_constant(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Torsional Constant should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError("Torsional Constant should be larger than 0.0")
        self._torsional_constant = value

    @property
    def plastic_modulus_x_axis(self):
        return self._plastic_modulus_x_axis

    @plastic_modulus_x_axis.setter
    def plastic_modulus_x_axis(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Zx (Plastic Modulus - x axis) should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError(
                "Zx (Plastic Modulus - x axis) should be larger than 0.0")
        self._plastic_modulus_x_axis = value

    @property
    def plastic_modulus_y_axis(self):
        return self._plastic_modulus_y_axis

    @plastic_modulus_y_axis.setter
    def plastic_modulus_y_axis(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "Zy (Plastic Modulus - y axis) should be of type float, integer, or None")
        if value is not None and value <= 0.0:
            raise ValueError(
                "Zy (Plastic Modulus - y axis) should be larger than 0.0")
        self._plastic_modulus_y_axis = value

    def is_empty_or_whitespace(input_string: str) -> bool:
        return not input_string or not input_string.strip()

    @classmethod
    def convert_parameter_string_to_tuple(self, parameter_str: str) -> tuple[int, float]:
        parameter_list: list[str] = parameter_str.split(';')
        for param in parameter_list:
            if self.is_empty_or_whitespace(param):
                raise XmiInconsistentDataAttributeError(
                    f"The individual parameter [{param}] within the XmiStructuralCrossSection 'parameters' attribute should not be empty string or empty space")
            try:
                float_value = float(param)
            except ValueError:
                raise XmiInconsistentDataAttributeError(
                    f"The parameter [{param}] within the XmiStructuralCrossSection 'parameters' attribute should be convertible to float")

        parameter_tuple = tuple([float(param) for param in parameter_list])

        return parameter_tuple
