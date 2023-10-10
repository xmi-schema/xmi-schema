from src.xmi.v1.xmi_parser import XmiParser
from src.xmi.v1.xmi_file import XmiFile


def test_xmi_parser_1():
    json_path = "tests/xmi/v1/test_inputs/xmi_parser/xmi_parser.json"
    xmi_parser = XmiParser()
    xmi_file = xmi_parser.read_xmi(json_path=json_path)
    assert isinstance(xmi_file, XmiFile)
