from .enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum
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
                 material_type: XmiStructuralMaterialTypeEnum = None,
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
        if not kwargs:
            super().__init__(id=id, name=name, ifcguid=ifcguid, description=description)
        else:
            super().__init__(**kwargs)
        attributes = [
            ('Type', kwargs.get('Type', material_type)),
            ('Grade', kwargs.get('Grade', grade)),
            ('UnitWeight', kwargs.get('UnitWeight', unit_weight)),
            ('EModulus', kwargs.get('EModulus', e_modulus)),
            ('GModulus', kwargs.get('GModulus', g_modulus)),
            ('PoissonRatio', kwargs.get('PoissonRatio', poisson_ratio)),
            ('ThermalCoefficient', kwargs.get(
                'ThermalCoefficient', thermal_coefficient))
        ]

        for attr_name, attr_value in attributes:
            try:
                setattr(self, attr_name, attr_value)
            except Exception as e:
                print(f"Caught an exception while setting {attr_name}: {e}")
                # Set to some default value or None
                setattr(self, attr_name, None)

        print("Object successfully created")

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, value):
        if value is not None and not isinstance(value, XmiStructuralMaterialTypeEnum):
            raise TypeError(
                "Type should be an XmiStructuralMaterialTypeEnum or None")
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
    def from_dict(cls, data: dict):
        error_logs = []
        processed_data = data.copy()

        for attr in cls.attributes_needed:
            if attr not in data:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        # for type conversion when reading dictionary
        try:
            processed_data["Type"] = XmiStructuralMaterialTypeEnum.from_attribute(
                data['Type'])
        except KeyError as e:
            error_logs.append(e)
            processed_data["Type"] = None
        return cls(**data), error_logs
