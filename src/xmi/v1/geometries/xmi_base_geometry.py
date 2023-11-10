from ..xmi_base import XmiBaseEntity


class XmiBaseGeometry(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ()

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 ifcguid: str = None,
                 description: str = None,
                 ** kwargs):

        super().__init__(id, name, ifcguid, description, **kwargs)
