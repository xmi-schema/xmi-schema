# import pytest
# from src.xmi.v1.entities.xmi_structural_cross_section import XmiStructuralCrossSection
# from src.xmi.v1.entities.xmi_structural_material import XmiStructuralMaterial
# from src.xmi.v1.enums.xmi_structural_cross_section_enums import XmiStructuralCrossSectionShapeEnum
# from src.xmi.v1.enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum
# from src.xmi.v1.xmi_errors import *
# import json


# def test_xmi_structural_cross_section_ok_1():
#     json_path = "tests/xmi/v1/test_inputs/xmi_structural_cross_section/xmi_structural_material_test.json"
#     with open(json_path, 'r') as f:
#         data = json.load(f)

#     id = data['ID']
#     name = data['Name']
#     description = data['Description']
#     ifcguid = data['IFCGUID']
#     material_type = XmiStructuralMaterialTypeEnum.CONCRETE
#     grade = data['Grade']
#     unit_weight = data['UnitWeight']
#     e_modulus = data['EModulus']
#     g_modulus = data['GModulus']
#     poisson_ratio = data['PoissonRatio']
#     thermal_coefficient = data['ThermalCoefficient']

#     xmi_structural_material = XmiStructuralMaterial(
#         id=id,
#         name=name,
#         description=description,
#         ifcguid=ifcguid,
#         material_type=material_type,
#         grade=grade,
#         unit_weight=unit_weight,
#         e_modulus=e_modulus,
#         g_modulus=g_modulus,
#         poisson_ratio=poisson_ratio,
#         thermal_coefficient=thermal_coefficient
#     )

#     shape = XmiStructuralCrossSectionShapeEnum.CIRCULAR
#     parameters = (100,)  # value is shown in mm for testing purposes
#     xmi_structural_cross_section = XmiStructuralCrossSection(
#         material=xmi_structural_material,
#         shape=shape,
#         parameters=parameters
#     )

#     assert isinstance(xmi_structural_cross_section, XmiStructuralCrossSection)
#     assert xmi_structural_cross_section.Material == xmi_structural_material
#     assert xmi_structural_cross_section.Parameters == parameters
#     assert xmi_structural_cross_section.Shape == shape
#     assert isinstance(xmi_structural_cross_section.Parameters, tuple)


# def test_xmi_structural_cross_section_fail():
#     json_path = "tests/xmi/v1/test_inputs/xmi_structural_cross_section/xmi_structural_material_test.json"
#     with open(json_path, 'r') as f:
#         data = json.load(f)

#     id = data['ID']
#     name = data['Name']
#     description = data['Description']
#     ifcguid = data['IFCGUID']
#     material_type = XmiStructuralMaterialTypeEnum.CONCRETE
#     grade = data['Grade']
#     unit_weight = data['UnitWeight']
#     e_modulus = data['EModulus']
#     g_modulus = data['GModulus']
#     poisson_ratio = data['PoissonRatio']
#     thermal_coefficient = data['ThermalCoefficient']

#     xmi_structural_material = XmiStructuralMaterial(
#         id=id,
#         name=name,
#         description=description,
#         ifcguid=ifcguid,
#         material_type=material_type,
#         grade=grade,
#         unit_weight=unit_weight,
#         e_modulus=e_modulus,
#         g_modulus=g_modulus,
#         poisson_ratio=poisson_ratio,
#         thermal_coefficient=thermal_coefficient
#     )

#     shape = XmiStructuralCrossSectionShapeEnum.CIRCULAR
#     parameters = (100, 100)  # value is shown in mm for testing purposes
#     with pytest.raises(XmiInconsistentDataAttributeError, match="The parameter length is different than required XmiStructuralCrossSectionShapeEnum"):
#         xmi_structural_cross_section = XmiStructuralCrossSection(
#             material=xmi_structural_material,
#             shape=shape,
#             parameters=parameters
#         )
#         print(xmi_structural_cross_section)


# def test_xmi_structural_cross_section_ok_2():
#     json_path = "tests/xmi/v1/test_inputs/xmi_structural_cross_section/xmi_structural_cross_section_test.json"
#     with open(json_path, 'r') as f:
#         data = json.load(f)
#     structural_material_dict = data['StructuralMaterial'][0]
#     structural_cross_section_dict = data['StructuralCrossSection'][0]

#     id = structural_material_dict['ID']
#     name = structural_material_dict['Name']
#     description = structural_material_dict['Description']
#     ifcguid = structural_material_dict['IFCGUID']
#     material_type = XmiStructuralMaterialTypeEnum.from_attribute_get_enum(
#         structural_material_dict['Type'])
#     grade = structural_material_dict['Grade']
#     unit_weight = structural_material_dict['UnitWeight']
#     e_modulus = structural_material_dict['EModulus']
#     g_modulus = structural_material_dict['GModulus']
#     poisson_ratio = structural_material_dict['PoissonRatio']
#     thermal_coefficient = structural_material_dict['ThermalCoefficient']

#     xmi_structural_material = XmiStructuralMaterial(
#         id=id,
#         name=name,
#         description=description,
#         ifcguid=ifcguid,
#         material_type=material_type,
#         grade=grade,
#         unit_weight=unit_weight,
#         e_modulus=e_modulus,
#         g_modulus=g_modulus,
#         poisson_ratio=poisson_ratio,
#         thermal_coefficient=thermal_coefficient
#     )

#     expected_shape = XmiStructuralCrossSectionShapeEnum.from_attribute_get_enum(
#         structural_cross_section_dict['Shape'])

#     expected_parameters = tuple(
#         [float(param) for param in structural_cross_section_dict['Parameters'].split(";")])
#     xmi_structural_cross_section = XmiStructuralCrossSection(
#         material=xmi_structural_material,
#         shape=expected_shape,
#         parameters=expected_parameters
#     )

#     assert isinstance(xmi_structural_cross_section, XmiStructuralCrossSection)
#     assert xmi_structural_cross_section.Material == xmi_structural_material
#     assert xmi_structural_cross_section.Parameters == expected_parameters
#     assert xmi_structural_cross_section.Shape == expected_shape
#     assert isinstance(xmi_structural_cross_section.Parameters, tuple)
