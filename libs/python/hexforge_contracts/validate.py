import json
from jsonschema import Draft202012Validator


def validate_json(data: dict, schema: dict) -> None:
    Draft202012Validator(schema).validate(data)


def load_schema(name: str) -> dict:
    from .paths import load_schema_text
    return json.loads(load_schema_text(name))
