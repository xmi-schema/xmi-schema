import uuid

from ..enums.xmi_enums import XmiUnitEnum
from ..xmi_base import XmiBaseEntity, XmiBaseRelationship


class XmiStructuralUnit(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_Entity', '_Attribute',
                                           '_Unit')

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot != "_entity_type"]

    def __init__(self,
                 entity,
                 attribute,
                 unit,
                 id=None,
                 name=None,
                 description=None,
                 ifcguid=None,
                 **kwargs):
        entity_type = "XmiStructuralUnit"

        uuid_value = uuid.uuid4()
        id = id if id else uuid_value
        name = name if name else "{class_name}_{uuid_value}".format(
            class_name=type(self).__name__, uuid_value=uuid_value)

        # Initialize parent class
        super().__init__(id=id,
                         name=name,
                         ifcguid=ifcguid,
                         description=description,
                         entity_type=entity_type
                         )

        self.Entity = entity
        self.Attribute = attribute
        self.Unit = unit

    @property
    def Entity(self):
        return self._Entity

    @Entity.setter
    def Entity(self, value):
        if not isinstance(value, str):
            raise TypeError("Entity should be an str")
        self._Entity = value

    @property
    def Attribute(self):
        return self._Attribute

    @Attribute.setter
    def Attribute(self, value):
        if not isinstance(value, str):
            raise TypeError("Attribute should be an str")
        self._Attribute = value

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, value):
        if not isinstance(value, XmiUnitEnum):
            raise TypeError("Unit should be an int or float")
        self._Unit = value
