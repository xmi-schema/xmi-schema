from pydantic import Field, field_validator
from typing import Optional, Tuple, List
from ..bases.xmi_base_geometry import XmiBaseGeometry

class XmiPoint3D(XmiBaseGeometry):
    x: float = Field(..., description="X coordinate")
    y: float = Field(..., description="Y coordinate")
    z: float = Field(..., description="Z coordinate")

    @field_validator("x", "y", "z")
    @classmethod
    def check_coordinate(cls, v, field):
        if not isinstance(v, (int, float)):
            raise TypeError(f"{field.name} must be a number")
        return float(v)

    @classmethod
    def from_dict(cls, data: dict) -> Tuple["XmiPoint3D", List[Exception]]:
        error_logs: List[Exception] = []

        required_keys = ["x", "y", "z"]
        for key in required_keys:
            if key not in data:
                error_logs.append(Exception(f"Missing required attribute: {key}"))
                data[key] = 0.0

        try:
            instance = cls(**data)
        except Exception as e:
            error_logs.append(Exception(f"Failed to create XmiPoint3D: {str(e)}"))
            instance = None

        return instance, error_logs

    @classmethod
    def from_xmi_dict_obj(cls, xmi_dict_obj: dict) -> Tuple["XmiPoint3D", List[Exception]]:
        key_map = {
            "Name": "name",
            "X": "x",
            "Y": "y",
            "Z": "z",
            "Description": "description",
            "ID": "id",
            "IFCGUID": "ifcguid",
        }

        processed = {key_map.get(k, k): v for k, v in xmi_dict_obj.items() if k in key_map}
        return cls.from_dict(processed)