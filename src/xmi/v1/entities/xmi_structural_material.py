# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum
from .xmi_base import XmiBase


class XmiStructuralMaterial(XmiBase):
    __slots__ = XmiBase.__slots__ + ('_Type',
                                     '_Grade',
                                     '_UnitWeight',
                                     '_EModulus',
                                     '_GModulus',
                                     '_PoissonRatio',
                                     '_ThermalCoefficient')

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
                 **kwargs
                 ):

        # Check for mutual exclusivity
        if kwargs and any([grade, unit_weight, e_modulus, g_modulus, poisson_ratio, thermal_coefficient, id, name, description, ifcguid]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # Ensure material_type is provided
        if material_type is None and 'Type' not in kwargs:
            raise ValueError(
                "The 'material_type' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description) if not kwargs else super().__init__(**kwargs)

        # Initialize attributes
        self.set_attributes(material_type, grade, unit_weight, e_modulus,
                            g_modulus, poisson_ratio, thermal_coefficient, **kwargs)

    def set_attributes(self, material_type, grade, unit_weight, e_modulus, g_modulus, poisson_ratio, thermal_coefficient, **kwargs):
        attributes = [
            ('Type', material_type),
            ('Grade', grade),
            ('UnitWeight', unit_weight),
            ('EModulus', e_modulus),
            ('GModulus', g_modulus),
            ('PoissonRatio', poisson_ratio),
            ('ThermalCoefficient', thermal_coefficient)
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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, value):
        if not isinstance(value, XmiStructuralMaterialTypeEnum):
            raise TypeError(
                "Type should be an XmiStructuralMaterialTypeEnum")
        self._Type = value

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Grade should be of type float or None")
        self._Grade = value

    # Similarly, for other properties:

    @property
    def UnitWeight(self):
        return self._UnitWeight

    @UnitWeight.setter
    def UnitWeight(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("UnitWeight should be of type float or None")
        self._UnitWeight = value

    @property
    def EModulus(self):
        return self._EModulus

    @EModulus.setter
    def EModulus(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("EModulus should be of type float or None")
        self._EModulus = value

    @property
    def GModulus(self):
        return self._GModulus

    @GModulus.setter
    def GModulus(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("GModulus should be of type float or None")
        self._GModulus = value

    @property
    def PoissonRatio(self):
        return self._PoissonRatio

    @PoissonRatio.setter
    def PoissonRatio(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("PoissonRatio should be of type float or None")
        self._PoissonRatio = value

    @property
    def ThermalCoefficient(self):
        return self._ThermalCoefficient

    @ThermalCoefficient.setter
    def ThermalCoefficient(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(
                "ThermalCoefficient should be of type float, integer, or None")
        self._ThermalCoefficient = value

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
            processed_data["Type"] = XmiStructuralMaterialTypeEnum.from_attribute_get_enum(
                data['Type'])
            if processed_data['Type'] is None and 'Type' in data:
                error_logs.append(Exception(
                    "Cannot Identify XmiStructuralMaterialTypeEnum: {data_value}".format(data_value=data['Type'])))
                return None, error_logs
        except KeyError as e:
            error_logs.append(e)
            processed_data["Type"] = None
            return None, error_logs
        instance = cls(
            material_type=processed_data['Type'], **processed_data)

        return instance, error_logs
