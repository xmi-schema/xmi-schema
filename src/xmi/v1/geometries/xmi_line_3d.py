# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseGeometry
from .xmi_point_3d import XmiPoint3D


class XmiLine3D(XmiBaseGeometry):
    def __init__(self) -> None:
        super().__init__()
        self.start_point = None
