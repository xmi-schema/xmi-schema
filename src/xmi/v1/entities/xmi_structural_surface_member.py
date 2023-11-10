# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from .xmi_structural_material import XmiStructuralMaterial
from .xmi_structural_point_connection import XmiStructuralPointConnection
from ..xmi_base import XmiBaseEntity
from ..enums.xmi_structural_surface_member_enums import *
from ..enums.xmi_enums import XmiSegmentTypeEnum
from ..entities.xmi_segment import XmiSegment


class XmiStructuralSurfaceMember(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + \
        ('_material',
         '_surface_member_type',
         '_span_type',
         '_thickness',
         '_system_plane',
         '_nodes',
         '_edges',
         '_area',
         '_storey',
         '_segments',
         '_z_offset',
         '_local_axis_x',
         '_local_axis_y',
         '_local_axis_z',
         '_height',
         )

    _attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 material: XmiStructuralMaterial,
                 surface_member_type: XmiStructuralSurfaceMemberTypeEnum,
                 span_type: XmiStructuralSurfaceMemberSpanTypeEnum,
                 thickness: float | int,
                 system_plane: XmiStructuralSurfaceMemberSystemPlaneEnum,
                 segments: list[XmiSegment] = [],
                 nodes: list[XmiStructuralPointConnection] = [],
                 area: float | int | None = None,
                 z_offset: float | int = 0.0,
                 local_axis_x: tuple = (1.0, 0.0, 0.0),
                 local_axis_y: tuple = (0.0, 1.0, 0.0),
                 local_axis_z: tuple = (0.0, 0.0, 1.0),
                 storey: str = None,
                 id=None,
                 name=None,
                 description=None,
                 ifcguid=None,
                 **kwargs
                 ):

        if material is None:
            raise ValueError(
                "The 'material' parameter is compulsory and must be provided.")

        if surface_member_type is None:
            raise ValueError(
                "The 'surface_member_type' parameter is compulsory and must be provided.")

        if span_type is None:
            raise ValueError(
                "The 'span_type' parameter is compulsory and must be provided.")

        if thickness is None:
            raise ValueError(
                "The 'thickness' parameter is compulsory and must be provided.")

        if system_plane is None:
            raise ValueError(
                "The 'system_plane' parameter is compulsory and must be provided.")

        if segments is None:
            raise ValueError(
                "The 'segments' parameter is compulsory and must be provided.")

        if nodes is None:
            raise ValueError(
                "The 'nodes' parameter is compulsory and must be provided.")

        if area is None:
            raise ValueError(
                "The 'area' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description)

        # Initialize attributes
        self.set_attributes(material=material,
                            surface_member_type=surface_member_type,
                            span_type=span_type,
                            thickness=thickness,
                            system_plane=system_plane,
                            segments=segments,
                            nodes=nodes,
                            z_offset=z_offset,
                            local_axis_x=local_axis_x,
                            local_axis_y=local_axis_y,
                            local_axis_z=local_axis_z,
                            area=area,
                            storey=storey,
                            **kwargs
                            )

    def set_attributes(self,
                       material: XmiStructuralMaterial,
                       surface_member_type: XmiStructuralSurfaceMemberTypeEnum,
                       span_type: XmiStructuralSurfaceMemberSpanTypeEnum,
                       thickness: float | int,
                       system_plane: XmiStructuralSurfaceMemberSystemPlaneEnum,
                       segments: list[XmiSegment],
                       nodes: list[XmiStructuralPointConnection],
                       z_offset: float | int,
                       local_axis_x: tuple,
                       local_axis_y: tuple,
                       local_axis_z: tuple,
                       area: float | int,
                       storey: str = None,
                       **kwargs):
        attributes = [
            ('material', material),
            ('surface_member_type', surface_member_type),
            ('span_type', span_type),
            ('thickness', thickness),
            ('system_plane', system_plane),
            ('segments', segments),
            ('nodes', nodes),
            ('z_offset', z_offset),
            ('local_axis_x', local_axis_x),
            ('local_axis_y', local_axis_y),
            ('local_axis_z', local_axis_z),
            ('area', area),
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
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, XmiStructuralMaterial):
            raise TypeError(
                "material should be of type XmiStructuralMaterial")
        self._material = value

    @property
    def surface_member_type(self):
        return self._surface_member_type

    @surface_member_type.setter
    def surface_member_type(self, value):
        if not isinstance(value, XmiStructuralSurfaceMemberTypeEnum):
            raise TypeError(
                "surface_member_type should be type XmiStructuralSurfaceMemberTypeEnum")
        self._surface_member_type = value

    @property
    def span_type(self):
        return self._span_type

    @span_type.setter
    def span_type(self, value):
        if not isinstance(value, XmiStructuralSurfaceMemberSpanTypeEnum):
            raise TypeError(
                "span_type should be of type XmiStructuralSurfaceMemberSpanTypeEnum")
        self._span_type = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "thickness should be of type float or int")
        self._thickness = value

    @property
    def system_plane(self):
        return self._system_plane

    @system_plane.setter
    def system_plane(self, value):
        if not isinstance(value, XmiStructuralSurfaceMemberSystemPlaneEnum):
            raise TypeError(
                "system_plane should be of type XmiStructuralSurfaceMemberSystemPlaneEnum")
        self._system_plane = value

    @property
    def segments(self):
        return self._segments

    @segments.setter
    def segments(self, value):
        if not isinstance(value, list):
            raise TypeError(
                "segments should be type list")

        if len(value) < 2:
            raise ValueError(
                "'segments' list should have at least 3 items of type XmiSegment")

        for item in value:
            if not isinstance(item, XmiSegment):
                raise ValueError(
                    f"All items must be instances of type XmiSegment, got {type(item)} instead.")
        self._segments = value

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        if not isinstance(value, list):
            raise TypeError("Nodes should be a list")
        for item in value:
            if not isinstance(item, XmiStructuralPointConnection):
                raise ValueError(
                    f"All items must be instances of XmiStructuralPointConnection, got {type(item)} instead.")
        self._nodes = value

    @property
    def z_offset(self):
        return self._z_offset

    @z_offset.setter
    def z_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "z_offset should be type flaot or int")
        self._z_offset = value

    @property
    def local_axis_x(self):
        return self._local_axis_x

    @local_axis_x.setter
    def local_axis_x(self, value):
        if not isinstance(value, tuple):
            raise TypeError(
                "local_axis_x should be type XmiStructuralCurveMemberTypeEnum")
        self._local_axis_x = value

    @property
    def local_axis_y(self):
        return self._local_axis_y

    @local_axis_y.setter
    def local_axis_y(self, value):
        if not isinstance(value, tuple):
            raise TypeError(
                "local_axis_y should be type XmiStructuralCurveMemberTypeEnum")
        self._local_axis_y = value

    @property
    def local_axis_z(self):
        return self._local_axis_z

    @local_axis_z.setter
    def local_axis_z(self, value):
        if not isinstance(value, tuple):
            raise TypeError(
                "local_axis_z should be type XmiStructuralCurveMemberTypeEnum")
        self._local_axis_z = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "Area should be of type float or int")
        self._area = value

    @property
    def storey(self):
        return self._storey

    @storey.setter
    def storey(self, value):
        if not isinstance(value, str):
            raise TypeError("Storey should be an str")
        self._storey = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiStructuralCurveMember:
        instance = None
        exceptions = []
        processed_data = obj.copy()

        for attr in cls._attributes_needed:
            if attr not in processed_data:
                exceptions.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        # for type conversion when reading dictionary
        try:
            # check for cross_section_found
            cross_section_found = processed_data['cross_section']
            if cross_section_found is None:
                exceptions.append(XmiMissingReferenceInstanceError(
                    "Please provide cross_section value of type XmiStructuralCrossSection"))
                return None, exceptions
            if not isinstance(cross_section_found, XmiStructuralCrossSection):
                exceptions.append(XmiInconsistentDataTypeError(
                    "cross_section provided need to be of instance XmiStructuralCrossSection"))
                return None, exceptions

            # check for nodes
            nodes_found = processed_data['nodes']
            if nodes_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the nodes attribute"))
                return None, exceptions

            if not isinstance(nodes_found, list):
                exceptions.append(XmiInconsistentDataTypeError(
                    "nodes value provided need to be of instance list"))
                return None, exceptions
            for node in nodes_found:
                if not isinstance(node, XmiStructuralPointConnection):
                    exceptions.append(XmiInconsistentDataTypeError(
                        "nodes value provided need to be of instance XmiStructuralPointConnection"))
                    return None, exceptions

            # check for segments
            segments_found = processed_data['segments']
            if segments_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the segments attribute"))
                return None, exceptions
            # if segments length = 0, return error
            if len(segments_found) == 0:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "The 'segments' parameter requires at least 1 segment of Type XmiSegment"))
                return None, exceptions
            # if segment is not type list, return error
            if not isinstance(segments_found, list):
                exceptions.append(XmiInconsistentDataTypeError(
                    "segments value provided need to be of instance list"))
                return None, exceptions

            # check for all segment datatypes
            for segment in segments_found:
                if not isinstance(segment, XmiSegment):
                    exceptions.append(XmiInconsistentDataTypeError(
                        "segment value provided need to be of instance XmiSegment"))
                    return None, exceptions

            # setting up begin_node and end_node of element
            if len(segments_found) > 0:
                segment_begin: XmiSegment = segments_found[0]
                segment_end: XmiSegment = segments_found[len(segments_found)-1]

                begin_node_found = next(
                    (spc for spc in nodes_found if spc == segment_begin.begin_node), None)
                end_node_found = next(
                    (spc for spc in nodes_found if spc == segment_end.end_node), None)

                # check against xmi_dict provided
                if begin_node_found.name != processed_data['begin_node']:
                    exceptions.append(ValueError(
                        "'begin_node' in dictionary differs than the 1 defined in dictionary"))
                    return None, exceptions
                if end_node_found.name != processed_data['end_node']:
                    exceptions.append(ValueError(
                        "'end_node' in dictionary differs than the 1 defined in dictionary"))
                    return None, exceptions

                processed_data['begin_node'] = begin_node_found
                processed_data['end_node'] = end_node_found

            # check for local_axis_x
            local_axis_x_found = processed_data['local_axis_x']
            if local_axis_x_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the parameters attribute"))
                return None, exceptions

            local_axis_x_found = XmiStructuralCurveMember.convert_local_axis_string_to_tuple(
                'x', processed_data['local_axis_x'])

            if not isinstance(local_axis_x_found, tuple):
                exceptions.append(XmiInconsistentDataTypeError(
                    "local_axis_x value after conversion using the convert_parameter_string_to_tuple function should be of type tuple"))
                return None, exceptions
            processed_data['local_axis_x'] = local_axis_x_found

            # check for local_axis_y
            local_axis_y_found = processed_data['local_axis_y']
            if local_axis_y_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the parameters attribute"))
                return None, exceptions
            local_axis_y_found = XmiStructuralCurveMember.convert_local_axis_string_to_tuple(
                'y', processed_data['local_axis_y'])

            if not isinstance(local_axis_y_found, tuple):
                exceptions.append(XmiInconsistentDataTypeError(
                    "local_axis_y value after conversion using the convert_parameter_string_to_tuple function should be of type tuple"))
                return None, exceptions
            processed_data["local_axis_y"] = local_axis_y_found

            # check for local_axis_z
            local_axis_z_found = processed_data['local_axis_z']
            if local_axis_z_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the parameters attribute"))
                return None, exceptions
            local_axis_z_found = XmiStructuralCurveMember.convert_local_axis_string_to_tuple(
                'z', processed_data['local_axis_z'])
            if not isinstance(local_axis_z_found, tuple):
                exceptions.append(XmiInconsistentDataTypeError(
                    "local_axis_z value after conversion using the convert_parameter_string_to_tuple function should be of type tuple"))
                return None, exceptions
            processed_data["local_axis_z"] = local_axis_z_found

            # check system_line
            system_line_found = processed_data['system_line']
            if system_line_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the system_line attribute"))
                return None, exceptions
            system_line_found = XmiStructuralCurveMemberSystemLineEnum.from_attribute_get_enum(
                processed_data['system_line'])
            processed_data["system_line"] = system_line_found

            # check curve_member_type
            curve_member_type_found = processed_data['curve_member_type']
            if curve_member_type_found is None:
                exceptions.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the curve_member_type attribute"))
                return None, exceptions
            curve_member_type_found = XmiStructuralCurveMemberTypeEnum.from_attribute_get_enum(
                processed_data['curve_member_type'])
            processed_data["curve_member_type"] = curve_member_type_found

        except KeyError as e:
            exceptions.append(e)
            return None, exceptions

        try:
            instance = cls(
                ** processed_data)
        except Exception as e:
            exceptions.append(
                Exception(f"Error instantiating XmiStructuralCurveMember: {obj}"))

        return instance, exceptions

    @classmethod
    def from_xmi_dict_obj(cls,
                          xmi_dict_obj: dict,
                          material: XmiStructuralMaterial = None,
                          nodes: list[XmiStructuralPointConnection] = None,
                          segments: list[XmiBaseEntity] = None,
                          ) -> XmiStructuralSurfaceMember:
        # Define a mapping from snake_case keys to custom keys
        KEY_MAPPING = {
            "Material": "material",
            "Storey": "storey",
            "Type": "surface_member_type",
            "Nodes": "nodes",
            "SystemPlane": "system_plane",
            "Area": "area",
            "LocalAxisX": "local_axis_x",
            "LocalAxisY": "local_axis_y",
            "LocalAxisZ": "local_axis_z",
            "ZOffset": "z_offset",
            "Height": "height",
            "Name": "name",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid",
            # "StiffnessModifierFxx": "circular_arc_centre", # NOT IN USE
            # "StiffnessModifierFyy": "circular_arc_radius", # NOT IN USE
            # "StiffnessModifierFxy": "stiffness_modifier_area",
            # "StiffnessModifierMxx": "stiffness_modifier_shear_local_y_axis",
            # "StiffnessModifierMyy": "stiffness_modifier_shear_local_z_axis",
            # "StiffnessModifierMxy": "stiffness_modifier_shear_torsion",
            # "StiffnessModifierVxz": "stiffness_modifier_moment_local_y_axis",
            # "StiffnessModifierVyz": "stiffness_modifier_moment_local_z_axis",
            # "StiffnessModifierMass": "stiffness_modifier_moment_mass",
            # "StiffnessModifierWeight": "stiffness_modifier_moment_weight",
        }

        instance: XmiStructuralSurfaceMember | None = None
        exceptions: list[Exception] = []
        processed_data: dict = {KEY_MAPPING.get(
            key, key): value for key, value in xmi_dict_obj.items()}

        if material is not None:
            processed_data['material'] = material

        if nodes is not None:
            processed_data['nodes'] = nodes

        if segments is not None:
            processed_data['segments'] = segments

        # if segment_types is not None:
        #     processed_data['segment_types'] = segment_types

        instance, exceptions_found = cls.from_dict(
            processed_data)

        exceptions.extend(exceptions_found)

        return instance, exceptions
