import uuid
from .xmi_base import XmiBase


class XmiStructuralMaterial(XmiBase):
    __slots__ = XmiBase.__slots__ + ('_Type', '_Grade',
                                     '_UnitWeight', '_EModulus', '_GModulus', '_PoissonRatio', '_ThermalCoefficient')

    def __init__(self,
                 material_type: str,
                 grade: float = None,
                 unit_weight=None,
                 e_modulus: float = None,
                 g_modulus: float = None,
                 poisson_ratio: float = None,
                 thermal_coefficient: float = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None
                 ):

        uuid_value = uuid.uuid4()
        id = id if id else uuid_value
        name = name if name else "{class_name}_{uuid_value}".format(
            class_name=material_type(self).__name__, uuid_value=uuid_value)

        super().__init__(id=id, name=name, ifcguid=ifcguid, description=description)
        self._Type = material_type
        self._Grade = grade
        self._UnitWeight = unit_weight
        self._EModulus = e_modulus
        self._GModulus = g_modulus
        self._PoissonRatio = poisson_ratio
        self._ThermalCoefficient = thermal_coefficient

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, value):
        if not isinstance(value, str):
            raise TypeError("Type should be an str")
        self._Type = value

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "Grade should be of type float")
        self._Grade = value

    @property
    def UnitWeight(self):
        return self._UnitWeight

    @UnitWeight.setter
    def UnitWeight(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "UnitWeight should be of type float")
        self._UnitWeight = value

    @property
    def EModulus(self):
        return self._EModulus

    @EModulus.setter
    def EModulus(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "EModulus should be of type float")
        self._EModulus = value

    @property
    def GModulus(self):
        return self._GModulus

    @GModulus.setter
    def GModulus(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "GModulus should be of type float")
        self._GModulus = value

    @property
    def PoissonRatio(self):
        return self._PoissonRatio

    @PoissonRatio.setter
    def PoissonRatio(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "PoissonRatio should be of type float")
        self._PoissonRatio = value

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                "Length should be of type float or integer")
        self._Length = value
