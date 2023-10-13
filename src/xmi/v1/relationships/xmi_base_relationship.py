# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..entities.xmi_base_entity import XmiBaseEntity


class XmiBaseRelationship():

    def __init__(self, source: XmiBaseEntity, target: XmiBaseEntity, name: str = None) -> XmiBaseRelationship:
        """_summary_

        Parameters
        ----------
        source : XmiBaseEntity
            _description_
        target : XmiBaseEntity
            _description_
        name : str, optional
            _description_, by default None

        Returns
        -------
        XmiBaseRelationship
            _description_
        """
        self.source = source
        self.target = target
        self.name = name
