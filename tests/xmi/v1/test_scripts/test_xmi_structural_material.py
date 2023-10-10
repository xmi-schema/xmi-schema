from src.xmi.v1.xmi_structural_material import XmiStructuralMaterial
from src.xmi.v1.enums.xmi_structural_material_enums import *

import json


def test_xmi_structural_material_ok():
    json_path = "tests/xmi/v1/test_inputs/xmi_structural_material/xmi_parser_structural_material_only.json"
    with open(json_path, 'r') as f:
        data = json.load(f)

    id = data['ID']
    name = data['Name']
    description = data['Description']
    ifcguid = data['IFCGUID']
    material_type = XmiStructuralMaterialTypeEnum.CONCRETE
    grade = 50.0
    unit_weight = data['UnitWeight']
    e_modulus = data['EModulus']
    g_modulus = data['GModulus']
    poisson_ratio = data['PoissonRatio']
    thermal_coefficient = data['ThermalCoefficient']

    xmi_structural_material = XmiStructuralMaterial(
        id=id,
        name=name,
        description=description,
        ifcguid=ifcguid,
        material_type=material_type,
        grade=grade,
        unit_weight=unit_weight,
        e_modulus=e_modulus,
        g_modulus=g_modulus,
        poisson_ratio=poisson_ratio,
        thermal_coefficient=thermal_coefficient
    )
    assert id == xmi_structural_material.ID
    assert name == xmi_structural_material.Name
    assert description == xmi_structural_material.Description
    assert ifcguid == xmi_structural_material.IFCGUID
    assert material_type == xmi_structural_material.Type
    assert grade == xmi_structural_material.Grade
    assert unit_weight == xmi_structural_material.UnitWeight
    assert e_modulus == xmi_structural_material.EModulus
    assert g_modulus == xmi_structural_material.GModulus
    assert poisson_ratio == xmi_structural_material.PoissonRatio
    assert thermal_coefficient == xmi_structural_material.ThermalCoefficient


def test_xmi_structural_material_json_object_only():
    json_path = "tests/xmi/v1/test_inputs/xmi_structural_material/xmi_parser_structural_material_only.json"
    with open(json_path, 'r') as f:
        data = json.load(f)

    id = data['ID']
    name = data['Name']
    description = data['Description']
    ifcguid = data['IFCGUID']
    material_type_string = data['Type']
    grade = data['Grade']
    unit_weight = data['UnitWeight']
    e_modulus = data['EModulus']
    g_modulus = data['GModulus']
    poisson_ratio = data['PoissonRatio']
    thermal_coefficient = data['ThermalCoefficient']

    xmi_structural_material, error_logs = XmiStructuralMaterial.from_dict(data)
    assert id == xmi_structural_material.ID
    assert name == xmi_structural_material.Name
    assert description == xmi_structural_material.Description
    assert ifcguid == xmi_structural_material.IFCGUID
    assert material_type_string == XmiStructuralMaterialTypeEnum.from_enum_get_enum_attribute(
        xmi_structural_material.Type)
    assert grade == xmi_structural_material.Grade
    assert unit_weight == xmi_structural_material.UnitWeight
    assert e_modulus == xmi_structural_material.EModulus
    assert g_modulus == xmi_structural_material.GModulus
    assert poisson_ratio == xmi_structural_material.PoissonRatio
    assert thermal_coefficient == xmi_structural_material.ThermalCoefficient
