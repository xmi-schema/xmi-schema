from src.xmi.v1.entities.xmi_structural_material import XmiStructuralMaterial
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
    assert xmi_structural_material.id == id
    assert xmi_structural_material.name == name
    assert xmi_structural_material.description == description
    assert xmi_structural_material.ifcguid == ifcguid
    assert xmi_structural_material.material_type == material_type
    assert xmi_structural_material.grade == grade
    assert xmi_structural_material.unit_weight == unit_weight
    assert xmi_structural_material.e_modulus == e_modulus
    assert xmi_structural_material.g_modulus == g_modulus
    assert xmi_structural_material.poisson_ratio == poisson_ratio
    assert xmi_structural_material.thermal_coefficient == thermal_coefficient


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

    xmi_structural_material, error_logs = XmiStructuralMaterial.from_xmi_dict_obj(
        data)

    assert xmi_structural_material.id == id
    assert xmi_structural_material.name == name
    assert xmi_structural_material.description == description
    assert xmi_structural_material.ifcguid == ifcguid
    assert xmi_structural_material.material_type == XmiStructuralMaterialTypeEnum.from_attribute_get_enum_v2(
        material_type_string)
    assert xmi_structural_material.grade == grade
    assert xmi_structural_material.unit_weight == unit_weight
    assert xmi_structural_material.e_modulus == e_modulus
    assert xmi_structural_material.g_modulus == g_modulus
    assert xmi_structural_material.poisson_ratio == poisson_ratio
    assert xmi_structural_material.thermal_coefficient == thermal_coefficient


def test_xmi_structural_material_json_object_only_error_type():

    data = {

    }

    # modded to make data wrong
    data['Type'] = 'STEEL'

    xmi_structural_material, error_logs = XmiStructuralMaterial.from_xmi_dict_obj(
        data)
    assert xmi_structural_material == None
    # assert len(error_logs) == 1


def test_xmi_structural_material_json_object_only_pass():
    data = {
        "name": "416902",
        "material_type": "Concrete",
        "grade": 50.0,
        "unit_weight": 0.0,
        "e_modulus": 6248400000.0,
        "g_modulus": 0.0,
        "poisson_ratio": 0.2,
        "thermal_coefficient": 9.9999999999999991e-6,
        "description": "Concrete - Cast-in-Place Concrete - C40/50",
        "id": "d2bef6b7-d442-4cc0-9c4a-2da9c02c1921-00065c86",
        "ifcguid": "3IllQtr49Cm9nABQd0AaMd"
    }

    id = data['id']
    name = data['name']
    description = data['description']
    ifcguid = data['ifcguid']
    material_type_string = data['material_type']
    grade = data['grade']
    unit_weight = data['unit_weight']
    e_modulus = data['e_modulus']
    g_modulus = data['g_modulus']
    poisson_ratio = data['poisson_ratio']
    thermal_coefficient = data['thermal_coefficient']

    xmi_structural_material, error_logs = XmiStructuralMaterial.from_dict(
        data)

    assert xmi_structural_material.id == id
    assert xmi_structural_material.name == name
    assert xmi_structural_material.description == description
    assert xmi_structural_material.ifcguid == ifcguid
    assert xmi_structural_material.material_type == XmiStructuralMaterialTypeEnum.from_attribute_get_enum_v2(
        material_type_string)
    assert xmi_structural_material.grade == grade
    assert xmi_structural_material.unit_weight == unit_weight
    assert xmi_structural_material.e_modulus == e_modulus
    assert xmi_structural_material.g_modulus == g_modulus
    assert xmi_structural_material.poisson_ratio == poisson_ratio
    assert xmi_structural_material.thermal_coefficient == thermal_coefficient


def test_xmi_structural_material_json_object_only_pass_missing_e_modulus():
    data = {
        "name": "416902",
        "material_type": "Concrete",
        "grade": 50.0,
        "unit_weight": 0.0,
        # "e_modulus": 6248400000.0,
        "g_modulus": 0.0,
        "poisson_ratio": 0.2,
        "thermal_coefficient": 9.9999999999999991e-6,
        "description": "Concrete - Cast-in-Place Concrete - C40/50",
        "id": "d2bef6b7-d442-4cc0-9c4a-2da9c02c1921-00065c86",
        "ifcguid": "3IllQtr49Cm9nABQd0AaMd"
    }

    id = data['id']
    name = data['name']
    description = data['description']
    ifcguid = data['ifcguid']
    material_type_string = data['material_type']
    grade = data['grade']
    unit_weight = data['unit_weight']
    # e_modulus = data['e_modulus']
    g_modulus = data['g_modulus']
    poisson_ratio = data['poisson_ratio']
    thermal_coefficient = data['thermal_coefficient']

    xmi_structural_material, error_logs = XmiStructuralMaterial.from_dict(
        data)

    assert xmi_structural_material.id == id
    assert xmi_structural_material.name == name
    assert xmi_structural_material.description == description
    assert xmi_structural_material.ifcguid == ifcguid
    assert xmi_structural_material.material_type == XmiStructuralMaterialTypeEnum.from_attribute_get_enum_v2(
        material_type_string)
    assert xmi_structural_material.grade == grade
    assert xmi_structural_material.unit_weight == unit_weight
    assert xmi_structural_material.e_modulus == None
    assert xmi_structural_material.g_modulus == g_modulus
    assert xmi_structural_material.poisson_ratio == poisson_ratio
    assert xmi_structural_material.thermal_coefficient == thermal_coefficient
