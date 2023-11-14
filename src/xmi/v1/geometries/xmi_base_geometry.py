from ..xmi_base import XmiBaseEntity


class XmiBaseGeometry(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ()

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__ if slot != "_entity_type"]

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 ifcguid: str = None,
                 description: str = None,
                 ** kwargs):
        entity_type = "XmiBaseGeometry"

        # Initialize parent class
        super().__init__(id=id,
                         name=name,
                         ifcguid=ifcguid,
                         description=description,
                         entity_type=entity_type
                         )
