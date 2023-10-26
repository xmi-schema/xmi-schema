# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseGeometry


class XmiPoint3D(XmiBaseGeometry):
    __slots__ = ('_x', '_y', '_z')

    def __init__(self, x: float | int, y: float | int, z: float | int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
