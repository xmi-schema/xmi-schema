import json

from src.xmi.v1.xmi_manager import XmiManager
from src.xmi.v1.entities.xmi_structural_material import XmiStructuralMaterial


def test_xmi_manager_1():
    json_path = "tests/xmi/v1/test_inputs/xmi_manager/xmi_structural_manager_test_1.json"
    with open(json_path, 'r') as f:
        xmi_file_dict = json.load(f)

    xmi_manager = XmiManager()
    xmi_manager.read_xmi_dict(xmi_file_dict)

    print(xmi_manager)

    assert len(xmi_manager.entities) == 563
    assert len(xmi_manager.relationships) == 0

    xmi_structural_materials_found = [
        obj for obj in xmi_manager.entities if isinstance(obj, XmiStructuralMaterial)]
    assert len(xmi_structural_materials_found) == 1
