from src.xmi.v1.xmi_structural_cross_section import XmiStructuralCrossSection
from src.xmi.v1.xmi_structural_material import XmiStructuralMaterial
from src.xmi.v1.enums.xmi_structural_cross_section_enums import XmiStructuralCrossSectionShapeEnum
from src.xmi.v1.enums.xmi_structural_material_enums import XmiStructuralMaterialTypeEnum

import json


def test_xmi_structural_cross_section_ok_1():
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

    shape = XmiStructuralCrossSectionShapeEnum.CIRCULAR
    parameters = (100,)  # value is shown in mm for testing purposes
    xmi_structural_cross_section = XmiStructuralCrossSection(
        material=xmi_structural_material,
        shape=shape,
        parameters=parameters
    )

    assert isinstance(xmi_structural_cross_section, XmiStructuralCrossSection)
    assert xmi_structural_cross_section.Material == xmi_structural_material
    assert xmi_structural_cross_section.Parameters == parameters
    assert xmi_structural_cross_section.Shape == shape
