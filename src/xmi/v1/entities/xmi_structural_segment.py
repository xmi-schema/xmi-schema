# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..constants import *

from ..xmi_errors import *
from ..xmi_base import XmiBaseEntity


"""
1. Need to standardize "Parameters" property

"""


class XmiStructuralCrossSection(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_segment_type',
                                           '_geometry')
