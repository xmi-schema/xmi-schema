import json

from src.xmi.v1.xmi_manager import XmiManager
from src.xmi.v1.entities.xmi_structural_material import XmiStructuralMaterial
from src.xmi.v1.entities.xmi_structural_cross_section import XmiStructuralCrossSection
from src.xmi.v1.entities.xmi_structural_point_connection import XmiStructuralPointConnection


def test_xmi_manager_1():
    json_path = "tests/xmi/v1/test_inputs/xmi_manager/xmi_structural_manager_test_1.json"
    with open(json_path, 'r') as f:
        xmi_file_dict = json.load(f)

    xmi_manager = XmiManager()
    xmi_manager.read_xmi_dict(xmi_file_dict)

    print(xmi_manager)

    # StructuralMaterial = 1
    # StructuralPointConnectionn = 562
    # StructuralCrossSection = 8

    assert len(xmi_manager.entities) == 563
    assert len(xmi_manager.relationships) == 0

    xmi_structural_materials_found = [
        obj for obj in xmi_manager.entities if isinstance(obj, XmiStructuralMaterial)]
    xmi_structural_cross_sections_found = [
        obj for obj in xmi_manager.entities if isinstance(obj, XmiStructuralCrossSection)]
    xmi_structural_point_connections_found = [
        obj for obj in xmi_manager.entities if isinstance(obj, XmiStructuralPointConnection)]

    assert len(xmi_structural_materials_found) == 1
    assert len(xmi_structural_cross_sections_found) == 0
    assert len(xmi_structural_point_connections_found) == 562
