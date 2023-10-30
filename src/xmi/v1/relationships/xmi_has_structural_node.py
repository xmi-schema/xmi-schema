# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseRelationship, XmiBaseEntity
# from ..entities.xmi_structural_material import XmiStructuralMaterial
# from ..entities.xmi_structural_cross_section import XmiStructuralCrossSection
# from ..xmi_errors import XmiInconsistentDataTypeError
from ..constants import *


class XmiHasStructuralNode(XmiBaseRelationship):
    __slots__ = XmiBaseRelationship.__slots__

    def __init__(self, source: XmiBaseEntity, target: XmiBaseEntity, name='hasStructuralNode', **kwargs):
        super().__init__(source, target, name)
