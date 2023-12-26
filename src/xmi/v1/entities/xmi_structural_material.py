# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum
from ..xmi_base import XmiBaseEntity


class XmiStructuralMaterial(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_material_type',
                                           '_grade',
                                           '_unit_weight',
                                           '_e_modulus',
                                           '_g_modulus',
                                           '_poisson_ratio',
                                           '_thermal_coefficient')

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot != "_entity_type"]

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
                 **kwargs
                 ):
        entity_type = "XmiStructuralMaterial"
        # Ensure material_type is provided
        if material_type is None:
            raise ValueError(
                "The 'material_type' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id,
                         name=name,
                         ifcguid=ifcguid,
                         description=description,
                         entity_type=entity_type
                         )

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
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError("Grade should be of type float, integer, or None")
        self._grade = value

    # Similarly, for other properties:

    @property
    def unit_weight(self):
        return self._unit_weight

    @unit_weight.setter
    def unit_weight(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "UnitWeight should be of type float, integer, or None")
        self._unit_weight = value

    @property
    def e_modulus(self):
        return self._e_modulus

    @e_modulus.setter
    def e_modulus(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "EModulus should be of type float, integer, or None")
        self._e_modulus = value

    @property
    def g_modulus(self):
        return self._g_modulus

    @g_modulus.setter
    def g_modulus(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "GModulus should be of type float, integer, or None")
        self._g_modulus = value

    @property
    def poisson_ratio(self):
        return self._poisson_ratio

    @poisson_ratio.setter
    def poisson_ratio(self, value):
        if value is not None and not isinstance(value, (float, int)):
            raise TypeError(
                "PoissonRatio should be of type float, integer, or None")
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
    def from_dict(cls, obj: dict) -> XmiStructuralMaterial:
        instance = None
        error_logs: list[Exception] = []
        processed_data: dict = obj.copy()

        for attr in cls._attributes_needed:
            if attr not in processed_data:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        # for type conversion when reading dictionary
        try:
            material_type_found = XmiStructuralMaterialTypeEnum.from_attribute_get_enum(
                processed_data['material_type'])

            if material_type_found is None:
                error_logs.append(Exception(
                    "Cannot Identify XmiStructuralMaterialTypeEnum: {data_value}".format(data_value=obj['material_type'])))
                return None, error_logs
        except KeyError as e:
            error_logs.append(e)
            return None, error_logs

        del processed_data['material_type']

        try:
            instance = cls(
                material_type=material_type_found, **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating StructuralMaterial: {obj}"))

        return instance, error_logs

    @classmethod
    def from_xmi_dict_obj(cls, xmi_dict_obj: dict) -> XmiStructuralMaterial:
        # Define a mapping from snake_case keys to custom keys
        KEY_MAPPING = {
            "Name": "name",
            "Type": "material_type",
            "Grade": "grade",
            "UnitWeight": "unit_weight",
            "EModulus": "e_modulus",
            "GModulus": "g_modulus",
            "PoissonRatio": "poisson_ratio",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid",
            "ThermalCoefficient": "thermal_coefficient"
        }

        instance = None
        error_logs = []
        processed_data = {KEY_MAPPING.get(
            key, key): value for key, value in xmi_dict_obj.items()}

        instance, error_logs_found = cls.from_dict(
            processed_data)

        error_logs.extend(error_logs_found)

        return instance, error_logs
