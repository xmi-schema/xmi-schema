import json
from json import JSONDecodeError

from .xmi_file import XmiFile
from .xmi_structural_point_connection import XmiStructuralPointConnection
from .xmi_structural_curve_member import XmiStructuralCurveMember
from .xmi_structural_surface_member import XmiStructuralSurfaceMember
from .xmi_structural_material import XmiStructuralMaterial
from .xmi_structural_unit import XmiStructuralUnit


class ErrorLog():
    def __init__(self, entity_type, index, message, obj=None):
        self.entity_type = entity_type
        self.index = index
        self.message = message
        self.obj = str(obj)


class XmiParser():
    def __init__(self):
        pass

    def read_xmi(self, json_path: str) -> XmiFile:
        xmi_file = XmiFile()
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise ValueError("JSON root should be a dictionary.")

            for key, values in data.items():
                if not isinstance(values, list):
                    raise ValueError(f"The value for {key} should be a list.")

                if key == "StructuralMaterial":
                    for index, value in enumerate(values):
                        try:
                            xmi_file.StructuralMaterial.append(value)

                            member, error_logs = XmiStructuralMaterial.from_dict(
                                value)
                            xmi_file.XmiStructuralMaterials.append(member)
                            xmi_file.errors.extend(
                                [ErrorLog(key, index, str(error_log), value) for error_log in error_logs])
                        except Exception as e:
                            xmi_file.errors.append(
                                ErrorLog(key, index, str(e)))
            print(xmi_file)
            return xmi_file

        except FileNotFoundError:
            print("The specified JSON file could not be found.")
        except JSONDecodeError:
            print("An error occurred while decoding the JSON file.")
        except ValueError as ve:
            print(f"Value error: {ve}")
        except TypeError as te:
            print(f"Type error: {te}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    json_path = "test_xmi_parser.json"
    xmi_parser = XmiParser()
    xmi_file = xmi_parser.read_xmi(json_path=json_path)
    print(xmi_file)
