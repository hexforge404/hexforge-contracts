from __future__ import annotations

from importlib import resources
from pathlib import Path


_SCHEMAS_DIR = resources.files("hexforge_contracts").joinpath("schemas", "common")


def schema_path(name: str) -> Path:
    # Returns a Traversable; Path-like enough for reading, but we keep it as Path
    # only if the implementation supports it. We'll return Traversable/Path compatible.
    return _SCHEMAS_DIR.joinpath(name)  # type: ignore[return-value]


def load_schema_text(name: str) -> str:
    return _SCHEMAS_DIR.joinpath(name).read_text(encoding="utf-8")
