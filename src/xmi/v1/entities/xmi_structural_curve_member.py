# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

import uuid

from ..entities.xmi_structural_cross_section import XmiStructuralCrossSection

from .xmi_structural_point_connection import XmiStructuralPointConnection
from ..xmi_base import XmiBaseEntity, XmiBaseRelationship
from ..enums.xmi_structural_curve_member_enums import XmiStructuralCurveMemberTypeEnum
from ..enums.xmi_enums import XmiSegmentEnum

from ..xmi_errors import *


class XmiStructuralCurveMember(XmiBaseEntity):
    __slots__ = XmiBaseEntity.__slots__ + \
        ('_cross_section',
         '_storey',
         '_curve_member_type',
         '_nodes',
         '_segments',
         '_system_line',
         '_begin_node',
         '_end_node',
         '_length',
         '_local_axis_x',
         '_local_axis_y',
         '_local_axis_z',
         '_begin_node_x_offset',
         '_end_node_x_offset',
         '_begin_node_y_offset',
         '_end_node_y_offset',
         '_begin_node_z_offset',
         '_end_node_z_offset',
         '_end_fixity_start',
         '_end_fixity_end',
         )

    attributes_needed = [slot[1:] if slot.startswith(
        '_') else slot for slot in __slots__]

    def __init__(self,
                 cross_section,
                 curve_member_type,
                 nodes,
                 segments,
                 system_line,
                 begin_node,
                 end_node,
                 local_axis_x,
                 local_axis_y,
                 local_axis_z,
                 begin_node_x_offset,
                 end_node_x_offset,
                 begin_node_y_offset,
                 end_node_y_offset,
                 begin_node_z_offset,
                 end_node_z_offset,
                 length: int | float | None = None,
                 #  end_fixity_start,  # optional
                 #  end_fixity_end,  # optional
                 storey: str | None = None,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 ifcguid: str = None,
                 **kwargs
                 ):

        # Check for mutual exclusivity
        if kwargs and any([
                length,
                storey,
                id, name, description, ifcguid
        ]):
            raise ValueError(
                "Please use either standard parameters or kwargs, not both.")

        # Ensure cross_section is provided
        if cross_section is None and 'cross_section' not in kwargs:
            raise ValueError(
                "The 'cross_section' parameter is compulsory and must be provided.")

        # Ensure curve_member_type is provided
        if curve_member_type is None and 'curve_member_type' not in kwargs:
            raise ValueError(
                "The 'curve_member_type' parameter is compulsory and must be provided.")

        # Ensure nodes is provided
        if nodes is None and 'nodes' not in kwargs:
            raise ValueError(
                "The 'nodes' parameter is compulsory and must be provided.")

        # Ensure segments is provided
        if segments is None and 'segments' not in kwargs:
            raise ValueError(
                "The 'segments' parameter is compulsory and must be provided.")

        # Ensure system_line is provided
        if system_line is None and 'system_line' not in kwargs:
            raise ValueError(
                "The 'system_line' parameter is compulsory and must be provided.")

        # Ensure begin_node is provided
        if begin_node is None and 'begin_node' not in kwargs:
            raise ValueError(
                "The 'begin_node' parameter is compulsory and must be provided.")

        # Ensure end_node is provided
        if end_node is None and 'end_node' not in kwargs:
            raise ValueError(
                "The 'end_node' parameter is compulsory and must be provided.")

        # Ensure local_axis_x is provided
        if local_axis_x is None and 'local_axis_x' not in kwargs:
            raise ValueError(
                "The 'local_axis_x' parameter is compulsory and must be provided.")

        # Ensure local_axis_y is provided
        if local_axis_y is None and 'local_axis_y' not in kwargs:
            raise ValueError(
                "The 'local_axis_y' parameter is compulsory and must be provided.")

        # Ensure local_axis_z is provided
        if local_axis_z is None and 'local_axis_z' not in kwargs:
            raise ValueError(
                "The 'local_axis_z' parameter is compulsory and must be provided.")

        # Ensure begin_node_x_offset is provided
        if begin_node_x_offset is None and 'begin_node_x_offset' not in kwargs:
            raise ValueError(
                "The 'begin_node_x_offset' parameter is compulsory and must be provided.")

        # Ensure begin_node_y_offset is provided
        if begin_node_y_offset is None and 'begin_node_y_offset' not in kwargs:
            raise ValueError(
                "The 'begin_node_y_offset' parameter is compulsory and must be provided.")

        # Ensure begin_node_z_offset is provided
        if begin_node_z_offset is None and 'begin_node_z_offset' not in kwargs:
            raise ValueError(
                "The 'begin_node_z_offset' parameter is compulsory and must be provided.")

        # Ensure end_node_x_offset is provided
        if end_node_x_offset is None and 'end_node_x_offset' not in kwargs:
            raise ValueError(
                "The 'end_node_x_offset' parameter is compulsory and must be provided.")

        # Ensure end_node_y_offset is provided
        if end_node_y_offset is None and 'end_node_y_offset' not in kwargs:
            raise ValueError(
                "The 'end_node_y_offset' parameter is compulsory and must be provided.")

        # Ensure end_node_z_offset is provided
        if end_node_z_offset is None and 'end_node_z_offset' not in kwargs:
            raise ValueError(
                "The 'end_node_z_offset' parameter is compulsory and must be provided.")

        # Ensure end_node_z_offset is provided
        if end_node_z_offset is None and 'end_node_z_offset' not in kwargs:
            raise ValueError(
                "The 'end_node_z_offset' parameter is compulsory and must be provided.")

        # Ensure end_node_z_offset is provided
        if end_node_z_offset is None and 'end_node_z_offset' not in kwargs:
            raise ValueError(
                "The 'end_node_z_offset' parameter is compulsory and must be provided.")

        # Initialize parent class
        super().__init__(id=id, name=name, ifcguid=ifcguid,
                         description=description) if not kwargs else super().__init__(**kwargs)

        # Initialize attributes
        self.set_attributes(
            cross_section,
            curve_member_type,
            nodes,
            segments,
            system_line,
            begin_node,
            end_node,
            local_axis_x,
            local_axis_y,
            local_axis_z,
            begin_node_x_offset,
            end_node_x_offset,
            begin_node_y_offset,
            end_node_y_offset,
            begin_node_z_offset,
            end_node_z_offset,
            length,
            storey,
            **kwargs)

    def set_attributes(self,
                       cross_section,
                       curve_member_type,
                       nodes,
                       segments,
                       system_line,
                       begin_node,
                       end_node,
                       local_axis_x,
                       local_axis_y,
                       local_axis_z,
                       begin_node_x_offset,
                       end_node_x_offset,
                       begin_node_y_offset,
                       end_node_y_offset,
                       begin_node_z_offset,
                       end_node_z_offset,
                       length,
                       storey,
                       **kwargs):

        attributes = [
            ('cross_section', cross_section),
            ('curve_member_type', curve_member_type),
            ('nodes', nodes),
            ('segments', segments),
            ('system_line', system_line),
            ('begin_node', begin_node),
            ('end_node', end_node),
            ('local_axis_x', local_axis_x),
            ('local_axis_y', local_axis_y),
            ('local_axis_z', local_axis_z),
            ('begin_node_x_offset', begin_node_x_offset),
            ('end_node_x_offset', end_node_x_offset),
            ('begin_node_y_offset', begin_node_y_offset),
            ('end_node_y_offset', end_node_y_offset),
            ('begin_node_z_offset', begin_node_z_offset),
            ('end_node_z_offset', end_node_z_offset),
            ('length', length),
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
    def storey(self):
        return self._storey

    @storey.setter
    def storey(self, value):
        if not isinstance(value, str):
            raise TypeError("storey attribute should be an str")
        self._storey = value

    @property
    def curve_member_type(self):
        return self._curve_member_type

    @curve_member_type.setter
    def curve_member_type(self, value):
        if not isinstance(value, (XmiStructuralCurveMemberTypeEnum)):
            raise TypeError(
                "curve_member_type should be type XmiStructuralCurveMemberTypeEnum")
        self._curve_member_type = value

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        if not isinstance(value, list):
            raise TypeError("nodes attribute should be a list")
        for item in value:
            if not isinstance(item, XmiStructuralPointConnection):
                raise ValueError(
                    f"All items must be instances of XmiStructuralPointConnection, got {type(item)} instead.")
        self._nodes = value

    @property
    def begin_node(self):
        return self._begin_node

    @begin_node.setter
    def begin_node(self, value):
        if not isinstance(value, XmiStructuralPointConnection):
            raise TypeError(
                "begin_node should be of type XmiStructuralPointConnection")
        self._begin_node = value

    @property
    def end_node(self):
        return self._end_node

    @end_node.setter
    def end_node(self, value):
        if not isinstance(value, XmiStructuralPointConnection):
            raise TypeError(
                "EndNode should be of type XmiStructuralPointConnection")
        self._end_node = value

    @property
    def cross_section(self):
        return self._cross_section

    @cross_section.setter
    def cross_section(self, value):
        if not isinstance(value, XmiStructuralCrossSection):
            raise TypeError(
                "cross_section should be of type XmiStructuralCrossSection")
        self._cross_section = value

    @property
    def segments(self):
        return self._segments

    @segments.setter
    def segments(self, value):
        if not isinstance(value, list):
            raise TypeError(
                "Segments should be of type list")

        for item in value:
            if not isinstance(item, XmiSegmentEnum):
                raise ValueError(
                    f"All items must be instances of XmiStructuralCurveMemberSegmentEnum, got {type(item)} instead.")
        self._segments = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float, None)):
            raise TypeError(
                "length should be of type float or integer")
        self._length = value

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
    def begin_node_x_offset(self):
        return self._begin_node_x_offset

    @begin_node_x_offset.setter
    def begin_node_x_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "begin_node_x_offset should be of type float or int")
        self._begin_node_x_offset = value

    @property
    def begin_node_y_offset(self):
        return self._begin_node_y_offset

    @begin_node_y_offset.setter
    def begin_node_y_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "begin_node_y_offset should be of type float or int")
        self._begin_node_y_offset = value

    @property
    def begin_node_z_offset(self):
        return self._begin_node_z_offset

    @begin_node_z_offset.setter
    def begin_node_z_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "begin_node_z_offset should be of type float or int")
        self._begin_node_z_offset = value

    @property
    def end_node_x_offset(self):
        return self._end_node_x_offset

    @end_node_x_offset.setter
    def end_node_x_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "end_node_x_offset should be of type float or int")
        self._end_node_x_offset = value

    @property
    def end_node_y_offset(self):
        return self._end_node_y_offset

    @end_node_y_offset.setter
    def end_node_y_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "end_node_y_offset should be of type float or int")
        self._end_node_y_offset = value

    @property
    def end_node_z_offset(self):
        return self._end_node_z_offset

    @end_node_z_offset.setter
    def end_node_z_offset(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(
                "end_node_z_offset should be of type float or int")
        self.end_node_z_offset = value

    @classmethod
    def from_dict(cls, obj: dict) -> XmiStructuralCrossSection:
        instance = None
        error_logs = []
        processed_data = obj.copy()

        for attr in cls.attributes_needed:
            if attr not in processed_data:
                error_logs.append(Exception(f"Missing attribute: {attr}"))
                processed_data[attr] = None

        # for type conversion when reading dictionary
        try:
            # check for material found
            material_found = processed_data['material']
            if material_found is None:
                error_logs.append(XmiMissingReferenceInstanceError(
                    "Please provide material value of type XmiStructuralMaterial"))
                return None, error_logs
            else:
                if not isinstance(material_found, XmiStructuralMaterial):
                    error_logs.append(XmiInconsistentDataTypeError(
                        "material provided need to be of instance XmiStructuralMaterial"))

            # check for conversion of parameters to tuple of parameters suitable for the Shape
            shape_found = processed_data['shape']
            if shape_found is None:
                error_logs.append(XmiMissingRequiredAttributeError(
                    "Please provide value of type XmiStructuralCrossSectionShapeTypeEnum for the shape attribute"))
                return None, error_logs
            else:
                shape_found = XmiStructuralCrossSectionShapeEnum.from_attribute_get_enum(
                    processed_data['shape'])
                if not isinstance(shape_found, XmiStructuralCrossSectionShapeEnum):
                    error_logs.append(XmiInconsistentDataTypeError(
                        "shape value provided need to be of instance XmiStructuralCrossSectionShapeEnum"))
                    return None, error_logs
                processed_data['shape'] = shape_found

            # check for params
            parameters_found = processed_data['parameters']
            if parameters_found is None:
                error_logs.append(XmiMissingRequiredAttributeError(
                    "Please provide value for the parameters attribute"))
                return None, error_logs
            else:
                parameters_found = XmiStructuralCrossSection.convert_parameter_string_to_tuple(
                    processed_data['parameters'])

                if not isinstance(parameters_found, tuple):
                    error_logs.append(XmiInconsistentDataTypeError(
                        "parameters value after conversion using the convert_parameter_string_to_tuple function should be of type tuple"))
                    return None, error_logs
                processed_data['parameters'] = parameters_found
        except KeyError as e:
            error_logs.append(e)
            return None, error_logs

        del processed_data['material']

        try:
            instance = cls(
                material=material_found, **processed_data)
        except Exception as e:
            error_logs.append(
                Exception(f"Error instantiating XmiStructuralCrossSection: {obj}"))

        return instance, error_logs

    # additional parameters are used to inject reference elements
    @classmethod
    def from_xmi_dict_obj(cls, xmi_dict_obj: dict,
                          cross_section: XmiStructuralCrossSection = None,
                          nodes: list[XmiStructuralPointConnection] = None) -> XmiStructuralCurveMember:
        # Define a mapping from snake_case keys to custom keys
        KEY_MAPPING = {
            "CrossSection": "cross_section",
            "Storey": "storey",
            "Type": "curve_member_type",
            "Nodes": "nodes",
            "Segments": "segments",
            "SystemLine": "system_line",
            "BeginNode": "begin_node",
            "EndNode": "end_node",
            "Length": "length",
            "LocalAxisX": "local_axis_x",
            "LocalAxisY": "local_axis_y",
            "LocalAxisZ": "local_axis_z",
            "BeginNodeXOffset": "begin_node_x_offset",
            "EndNodeXOffset": "end_node_x_offset",
            "BeginNodeYOffset": "begin_node_y_offset",
            "EndNodeYOffset": "end_node_y_offset",
            "BeginNodeZOffset": "begin_node_z_offset",
            "EndNodeZOffset": "end_node_z_offset",
            "EndFixityStart": "end_fixity_start",
            "EndFixityEnd": "end_fixity_end",
            "Name": "name",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid",
            # "CircularArcCentre": "circular_arc_centre", # NOT IN USE
            # "CircularArcRadius": "circular_arc_radius", # NOT IN USE
            # "StiffnessModifierArea": "stiffness_modifier_area",
            # "StiffnessModifierAsy": "stiffness_modifier_shear_local_y_axis",
            # "StiffnessModifierAsz": "stiffness_modifier_shear_local_z_axis",
            # "StiffnessModifierTorsion": "stiffness_modifier_shear_torsion",
            # "StiffnessModifierIyy": "stiffness_modifier_moment_local_y_axis",
            # "StiffnessModifierIzz": "stiffness_modifier_moment_local_z_axis",
            # "StiffnessModifierMass": "stiffness_modifier_moment_mass",
            # "StiffnessModifierWeight": "stiffness_modifier_moment_weight",
            # "EndFixityAxialStart": "end_fixity_axial_start",
            # "EndFixityShearMajorStart": "end_fixity_shear_major_start",
            # "EndFixityShearMinorStart": "end_fixity_shear_minor_start",
            # "EndFixityTorsionStart": "end_fixity_torsion_start",
            # "EndFixityMomentMajorStart": "end_fixity_moment_major_start",
            # "EndFixityMomentMinorStart": "end_fixity_moment_minor_start",
            # "EndFixityAxialEnd": "end_fixity_axial_end",
            # "EndFixityShearMajorEnd": "end_fixity_shear_major_end",
            # "EndFixityShearMinorEnd": "end_fixity_shear_minor_end",
            # "EndFixityTorsionEnd": "end_fixity_torsion_end/",
            # "EndFixityMomentMajorEnd": "begin_node_y_offset",
            # "EndFixityMomentMinorEnd": "end_node_y_offset",
            # "LateralRestrain": "begin_node",
            # "LateralRestrainLocation": "end_node",
            # "LengthEffectiveMajor": "length",
            # "LengthEffectiveMinor": "local_axis_x",
            # "SwayInMajor": "local_axis_y",
            # "SwayInMinor": "local_axis_z",
            # "BracedAbtMajor": "begin_node_y_offset",
            # "BracedAbtMinor": "end_node_y_offset",
        }

        instance: XmiStructuralCurveMember | None = None
        error_logs: list[Exception] = []
        processed_data: dict = {KEY_MAPPING.get(
            key, key): value for key, value in xmi_dict_obj.items()}

        if 'cross_section' in processed_data.keys() and cross_section is not None:
            processed_data['cross_section'] = cross_section

        if 'nodes' in processed_data.keys() and nodes is not None:
            processed_data['nodes'] = nodes

        instance, error_logs_found = cls.from_dict(
            processed_data)

        error_logs.extend(error_logs_found)

        return instance, error_logs
