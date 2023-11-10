# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseRelationship, XmiBaseEntity
from ..constants import *


class XmiHasLine3D(XmiBaseRelationship):
    __slots__ = XmiBaseRelationship.__slots__ + ('_is_begin',
                                                 '_is_end'
                                                 )

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self, source: XmiBaseEntity, target: XmiBaseEntity, name='hasLine3D', **kwargs):
        name = 'hasLine3D'

        super().__init__(source, target, name)

        for key, value in kwargs.items():
            if key in self._attributes_needed:
                # Use the property setter for type checking
                setattr(self, key, value)

    @property
    def is_begin(self):
        return self._is_begin

    @is_begin.setter
    def is_begin(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_begin should be of type bool")
        self._is_begin = value

    @property
    def is_end(self):
        return self._is_end

    @is_end.setter
    def is_end(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_end should be of type bool")
        self._is_end = value
