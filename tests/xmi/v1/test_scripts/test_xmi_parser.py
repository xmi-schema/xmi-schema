from src.xmi.v1.xmi_parser import XmiParser


def test_xmi_parser():
    json_path = "tests/xmi/v1/test_inputs/xmi_parser/xmi_parser_structural_material_only.json"
    xmi_parser = XmiParser()
    xmi_file = xmi_parser.read_xmi(json_path=json_path)
    print(xmi_file)
