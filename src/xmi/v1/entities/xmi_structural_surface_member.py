import uuid

from .xmi_structural_material import XmiStructuralMaterial
from .xmi_structural_point_connection import XmiStructuralPointConnection
from ..xmi_base import XmiBaseEntity, XmiBaseRelationship
from ..enums.xmi_structural_surface_member_enums import *
from ..enums.xmi_enums import XmiSegmentTypeEnum


class XmiStructuralSurfaceMember(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + \
        ('_Storey', '_Material',
         '_Type', '_SpanType', '_Thickness', '_SystemPlane', '_Nodes', '_Edges', '_Area')

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 storey,
                 material,
                 surface_member_type,
                 span_type,
                 thickness,
                 system_plane,
                 nodes,
                 edges,
                 area,
                 id=None,
                 name=None,
                 description=None,
                 ifcguid=None
                 ):

        uuid_value = uuid.uuid4()
        id = id if id else uuid_value
        name = name if name else "{class_name}_{uuid_value}".format(
            class_name=surface_member_type(self).__name__, uuid_value=uuid_value)

        super().__init__(id=id, name=name, ifcguid=ifcguid, description=description)
        self.Material = material
        self.Storey = storey
        self.Type = surface_member_type
        self.Edges = edges
        self.SystemPlane = system_plane
        self.Thickness = thickness
        self.SpanType = span_type
        self.Nodes = nodes
        self.Area = area

    @property
    def Material(self):
        return self._Material

    @Material.setter
    def Material(self, value):
        if not isinstance(value, XmiStructuralMaterial):
            raise TypeError(
                "Length should be of type float or integer")
        self._Material = value

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
        if not isinstance(value, XmiStructuralSurfaceMemberTypeEnum):
            raise TypeError(
                "Type should be type XmiStructuralSurfaceMemberTypeEnum")
        self._Type = value

    @property
    def Edges(self):
        return self._Edges

    @Edges.setter
    def Edges(self, value):
        if not isinstance(value, list):
            raise TypeError(
                "Edges should be type list")
        for item in value:
            if not isinstance(item, XmiSegmentTypeEnum):
                raise ValueError(
                    f"All items must be instances of type XmiSegmentEnum, got {type(item)} instead.")
        self._Edges = value

    @property
    def SystemPlane(self):
        return self._SystemPlane

    @SystemPlane.setter
    def SystemPlane(self, value):
        if not isinstance(value, XmiStructuralSurfaceMemberSystemPlaneEnum):
            raise TypeError(
                "SystemPlane should be of type XmiStructuralSurfaceMemberSystemPlaneEnum")
        self._SystemPlane = value

    @property
    def Thickness(self):
        return self._Thickness

    @Thickness.setter
    def Thickness(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "Thickness should be of type float")
        self._Thickness = value

    @property
    def SpanType(self):
        return self._SpanType

    @SpanType.setter
    def SpanType(self, value):
        if not isinstance(value, XmiStructuralSurfaceMemberSpanTypeEnum):
            raise TypeError(
                "SpanType should be of type XmiStructuralSurfaceMemberSpanTypeEnum")
        self._SpanType = value

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
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, value):
        if not isinstance(value, float):
            raise TypeError(
                "Area should be of type float")
        self._Area = value
