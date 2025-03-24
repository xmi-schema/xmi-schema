# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseRelationship, XmiBaseEntity
from ..constants import *


class XmiHasPoint3D(XmiBaseRelationship):
    __slots__ = XmiBaseRelationship.__slots__

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self, source: XmiBaseEntity, target: XmiBaseEntity, name='hasPoint3D', **kwargs):
        name = 'hasPoint3D'
        entity_type = "XmiRelHasPoint3D"

        super().__init__(source, target, name, entity_type=entity_type)

        for key, value in kwargs.items():
            if key in self.__slots__:
                # Use the property setter for type checking
                setattr(self, key, value)
