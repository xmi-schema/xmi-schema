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

        # Check for mutual exclusivity, things that are optional should be inside any
        # if kwargs and any([
        #     id, name, description, ifcguid
        # ]):
        #     raise ValueError(
        #         "Please use either standard parameters or kwargs, not both.")

        super().__init__(id, name, ifcguid, description, **kwargs)
