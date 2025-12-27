from importlib import resources


def schema_path(name: str) -> str:
    return str(
        resources.files("hexforge_contracts")
        .joinpath("..", "..", "..", "schemas", "common", name)
    )


def load_schema_text(name: str) -> str:
    p = (
        resources.files("hexforge_contracts")
        .joinpath("..", "..", "..", "schemas", "common", name)
    )
    return p.read_text(encoding="utf-8")
