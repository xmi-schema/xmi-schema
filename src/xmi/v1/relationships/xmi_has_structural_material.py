# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseRelationship, XmiBaseEntity

from ..constants import *


class XmiHasStructuralMaterial(XmiBaseRelationship):
    __slots__ = XmiBaseRelationship.__slots__

    def __init__(self, source: XmiBaseEntity, target: XmiBaseEntity, material_type: str = None, **kwargs):
        name = 'hasStructuralMaterial'
        super().__init__(source, target, name, **kwargs)
        self._material_type = material_type
