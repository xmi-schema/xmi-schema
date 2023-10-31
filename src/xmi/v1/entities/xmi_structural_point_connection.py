# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseEntity, XmiBaseRelationship
from ..geometries.xmi_point_3d import XmiPoint3D


class XmiStructuralPointConnection(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + ('_node',
                                           '_storey')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 node: XmiPoint3D,
                 #  x: float = 0.0,
                 #  y: float = 0.0,
                 #  z: float = 0.0,
                 storey: str = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs):

        # Check for mutual exclusivity
        if kwargs and any([]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # # Ensure point is provided
        if node is None and 'node' not in kwargs:
            raise ValueError(
                "The 'node' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description)

        # Initialize attributes
        self.set_attributes(node, storey, **kwargs)

    def set_attributes(self, node, storey, **kwargs):
        attributes = [
            ('node', node),
            ('storey', storey)
        ]

        for attr_name, attr_value in attributes:
            value = kwargs.get(attr_name, attr_value)
            try:
                setattr(self, attr_name, value)
            except AttributeError as e:
                print(
                    f"Caught an AttributeError while setting {attr_name}: {e}")
                setattr(self, attr_name, None)

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        if not isinstance(value, XmiPoint3D):
            raise TypeError("node should be an XmiPoint3D")
        self._node = value

    @property
    def storey(self):
        return self._storey

    @storey.setter
    def storey(self, value):
        if not isinstance(value, str):
            raise TypeError("Storey should be an str")
        self._storey = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiStructuralPointConnection:
        error_logs = []
        processed_data = obj.copy()

        for attr in cls.attributes_needed:
            if attr not in obj:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        node_found = processed_data['node']

        # remove compulsory keys for proper class instantiation
        del processed_data['node']

        try:
            instance = cls(
                node=node_found,
                **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating StructuralPointConnection: {obj}"))

        return instance, error_logs

    @classmethod
    def from_xmi_dict_obj(cls, xmi_dict_obj: dict):
        # Define a mapping from snake_case keys to custom keys
        KEY_MAPPING = {
            "Name": "name",
            # "X": "x",
            # "Y": "y",
            # "Z": "z",
            "Storey": "storey",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid"
        }
        instance = None
        error_logs = []
        processed_data = {KEY_MAPPING.get(
            key, key): value for key, value in xmi_dict_obj.items()}

        instance, error_logs_found = cls.from_dict(
            processed_data)

        error_logs.extend(error_logs_found)

        return instance, error_logs
