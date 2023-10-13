from src.xmi.v1.xmi_structural_material import XmiStructuralMaterial
from src.xmi.v1.enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum

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
    grade = data['Grade']
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
    assert xmi_structural_material.ID == id
    assert xmi_structural_material.Name == name
    assert xmi_structural_material.Description == description
    assert xmi_structural_material.IFCGUID == ifcguid
    assert xmi_structural_material.Type == material_type
    assert xmi_structural_material.Grade == grade
    assert xmi_structural_material.UnitWeight == unit_weight
    assert xmi_structural_material.EModulus == e_modulus
    assert xmi_structural_material.GModulus == g_modulus
    assert xmi_structural_material.PoissonRatio == poisson_ratio
    assert xmi_structural_material.ThermalCoefficient == thermal_coefficient


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

    assert xmi_structural_material.ID == id
    assert xmi_structural_material.Name == name
    assert xmi_structural_material.Description == description
    assert xmi_structural_material.IFCGUID == ifcguid
    assert xmi_structural_material.Type == XmiStructuralMaterialTypeEnum.from_attribute_get_enum(
        material_type_string)
    assert xmi_structural_material.Grade == grade
    assert xmi_structural_material.UnitWeight == unit_weight
    assert xmi_structural_material.EModulus == e_modulus
    assert xmi_structural_material.GModulus == g_modulus
    assert xmi_structural_material.PoissonRatio == poisson_ratio
    assert xmi_structural_material.ThermalCoefficient == thermal_coefficient


def test_xmi_structural_material_json_object_only_error_type():
    json_path = "tests/xmi/v1/test_inputs/xmi_structural_material/xmi_parser_structural_material_only.json"
    with open(json_path, 'r') as f:
        data = json.load(f)

    # modded to make data wrong
    data['Type'] = 'STEEL'

    xmi_structural_material, error_logs = XmiStructuralMaterial.from_dict(data)
    assert xmi_structural_material == None
    assert len(error_logs) == 1


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

    assert xmi_structural_material.ID == id
    assert xmi_structural_material.Name == name
    assert xmi_structural_material.Description == description
    assert xmi_structural_material.IFCGUID == ifcguid
    assert xmi_structural_material.Type == XmiStructuralMaterialTypeEnum.from_attribute_get_enum(
        material_type_string)
    assert xmi_structural_material.Grade == grade
    assert xmi_structural_material.UnitWeight == unit_weight
    assert xmi_structural_material.EModulus == e_modulus
    assert xmi_structural_material.GModulus == g_modulus
    assert xmi_structural_material.PoissonRatio == poisson_ratio
    assert xmi_structural_material.ThermalCoefficient == thermal_coefficient
