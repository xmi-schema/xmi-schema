import uuid
from .xmi_base import XmiBase


class XmiStructuralPointConnection(XmiBase):
    __slots__ = XmiBase.__slots__ + ('_Storey', '_X',
                                     '_Y', '_Z')

    def __init__(self,
                 x: float,
                 y: float,
                 z: float,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None):
        uuid_value = uuid.uuid4()
        id = id if id else uuid_value
        name = name if name else "{class_name}_{uuid_value}".format(
            class_name=type(self).__name__, uuid_value=uuid_value)

        super().__init__(id=id, name=name, ifcguid=ifcguid, description=description)
        self.X = x
        self.Y = y
        self.Z = z

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("X should be an int or float")
        self._X = value

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Y should be an int or float")
        self._Y = value

    @property
    def Z(self):
        return self._Z

    @Z.setter
    def Z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Z should be an int or float")
        self._Z = value
