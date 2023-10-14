# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum
from ..xmi_base import XmiBaseEntity, XmiBaseRelationship


class XmiStructuralMaterial(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_material_type',
                                           '_grade',
                                           '_unit_weight',
                                           '_e_modulus',
                                           '_g_modulus',
                                           '_poisson_ratio',
                                           '_thermal_coefficient')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 material_type: XmiStructuralMaterialTypeEnum,
                 grade: float = None,
                 unit_weight=None,
                 e_modulus: float = None,
                 g_modulus: float = None,
                 poisson_ratio: float = None,
                 thermal_coefficient: float = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 relationships: list[XmiBaseRelationship] = [],
                 **kwargs
                 ):

        # Check for mutual exclusivity
        if kwargs and any([grade, unit_weight, e_modulus, g_modulus, poisson_ratio, thermal_coefficient, id, name, description, ifcguid, relationships]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # Ensure material_type is provided
        if material_type is None and 'material_type' not in kwargs:
            raise ValueError(
                "The 'material_type' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description, relationships=relationships) if not kwargs else super().__init__(**kwargs)

        # Initialize attributes
        self.set_attributes(material_type, grade, unit_weight, e_modulus,
                            g_modulus, poisson_ratio, thermal_coefficient, **kwargs)

    def set_attributes(self, material_type, grade, unit_weight, e_modulus, g_modulus, poisson_ratio, thermal_coefficient, **kwargs):
        attributes = [
            ('material_type', material_type),
            ('grade', grade),
            ('unit_weight', unit_weight),
            ('e_modulus', e_modulus),
            ('g_modulus', g_modulus),
            ('poisson_ratio', poisson_ratio),
            ('thermal_coefficient', thermal_coefficient)
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
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        if not isinstance(value, XmiStructuralMaterialTypeEnum):
            raise TypeError(
                "Type should be an XmiStructuralMaterialTypeEnum")
        self._material_type = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Grade should be of type float or None")
        self._grade = value

    # Similarly, for other properties:

    @property
    def unit_weight(self):
        return self._unit_weight

    @unit_weight.setter
    def unit_weight(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("UnitWeight should be of type float or None")
        self._unit_weight = value

    @property
    def e_modulus(self):
        return self._e_modulus

    @e_modulus.setter
    def e_modulus(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("EModulus should be of type float or None")
        self._e_modulus = value

    @property
    def g_modulus(self):
        return self._g_modulus

    @g_modulus.setter
    def g_modulus(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("GModulus should be of type float or None")
        self._g_modulus = value

    @property
    def poisson_ratio(self):
        return self._poisson_ratio

    @poisson_ratio.setter
    def poisson_ratio(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("PoissonRatio should be of type float or None")
        self._poisson_ratio = value

    @property
    def thermal_coefficient(self):
        return self._thermal_coefficient

    @thermal_coefficient.setter
    def thermal_coefficient(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "ThermalCoefficient should be of type float, integer, or None")
        self._thermal_coefficient = value

    @classmethod
    def from_dict(cls, data: dict) -> XmiStructuralMaterial:
        instance = None
        error_logs = []
        processed_data = data.copy()

        for attr in cls.attributes_needed:
            if attr not in data:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        # for type conversion when reading dictionary
        try:
            processed_data["material_type"] = XmiStructuralMaterialTypeEnum.from_attribute_get_enum(
                data['material_type'])
            if processed_data['material_type'] is None and 'Type' in data:
                error_logs.append(Exception(
                    "Cannot Identify XmiStructuralMaterialTypeEnum: {data_value}".format(data_value=data['material_type'])))
                return None, error_logs
        except KeyError as e:
            error_logs.append(e)
            processed_data["material_type"] = None
            return None, error_logs
        instance = cls(
            material_type=processed_data['material_type'], **processed_data)

        return instance, error_logs
