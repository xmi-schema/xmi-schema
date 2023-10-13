import uuid

from .xmi_structural_point_connection import XmiStructuralPointConnection
from .xmi_base_entity import XmiBaseEntity
from ..enums.xmi_structural_curve_member_enums import XmiStructuralCurveMemberTypeEnum
from ..enums.xmi_enums import XmiSegmentEnum


class XmiStructuralCurveMember(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + \
        ('_CrossSection', '_Storey', '_Type', '_Nodes',
         '_Segments', '_BeginNode', '_EndNode', '_Length')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 cross_section,
                 storey,
                 curve_member_type,
                 nodes,
                 segments,
                 begin_node,
                 end_node,
                 length,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None
                 ):

        uuid_value = uuid.uuid4()
        id = id if id else uuid_value
        name = name if name else "{class_name}_{uuid_value}".format(
            class_name=curve_member_type(self).__name__, uuid_value=uuid_value)

        super().__init__(id=id, name=name, ifcguid=ifcguid, description=description)
        self.CrossSection = cross_section
        self.Storey = storey
        self.Type = curve_member_type
        self.Nodes = nodes
        self.Segments = segments
        self.BeginNode = begin_node
        self.EndNode = end_node
        self.Length = length

    @property
    def Storey(self):
        return self._Storey

    @Storey.setter
    def Storey(self, value):
        if not isinstance(value, str):
            raise TypeError("Storey should be an str")
        self._Storey = value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, value):
        if not isinstance(value, (XmiStructuralCurveMemberTypeEnum)):
            raise TypeError(
                "Type should be type XmiStructuralCurveMemberTypeEnum")
        self._Type = value

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, value):
        if not isinstance(value, list):
            raise TypeError("Nodes should be a list")
        for item in value:
            if not isinstance(item, XmiStructuralPointConnection):
                raise ValueError(
                    f"All items must be instances of XmiStructuralPointConnection, got {type(item)} instead.")
        self._Nodes = value

    @property
    def BeginNode(self):
        return self._BeginNode

    @BeginNode.setter
    def BeginNode(self, value):
        if not isinstance(value, XmiStructuralPointConnection):
            raise TypeError(
                "BeginNode should be of type XmiStructuralPointConnection")
        self._BeginNode = value

    @property
    def EndNode(self):
        return self._EndNode

    @EndNode.setter
    def EndNode(self, value):
        if not isinstance(value, XmiStructuralPointConnection):
            raise TypeError(
                "EndNode should be of type XmiStructuralPointConnection")
        self._EndNode = value

    @property
    def CrossSection(self):
        return self._CrossSection

    @CrossSection.setter
    def CrossSection(self, value):
        if not isinstance(value, str):
            raise TypeError(
                "CrossSection should be of type str")
        self._CrossSection = value

    @property
    def Segments(self):
        return self._Segments

    @Segments.setter
    def Segments(self, value):
        if not isinstance(value, list):
            raise TypeError(
                "Segments should be of type list")

        for item in value:
            if not isinstance(item, XmiSegmentEnum):
                raise ValueError(
                    f"All items must be instances of XmiStructuralCurveMemberSegmentEnum, got {type(item)} instead.")
        self._Segments = value

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                "Length should be of type float or integer")
        self._Length = value
