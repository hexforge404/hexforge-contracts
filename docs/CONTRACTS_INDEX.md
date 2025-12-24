# HexForge Contracts Index

This index is the single “map of the map” for every HexForge engine/agent contract.

## Core shared schemas

- `schemas/job_status.schema.json`  
  Standard status envelope all engines MUST return.

## Engines

### GlyphEngine (surface v1 engine)
- Filesystem: `engines/glyphengine/FILESYSTEM.md`
- Interfaces: `engines/glyphengine/INTERFACES.md`

## Contract rules (global)

- Engines MUST write public outputs under `/assets/<engine>/...` via the nginx-served host mount.
- Engines MUST return ONLY relative public URLs beginning with `/assets/`.
- Engines MUST return status using the `job_status.schema.json` envelope.
- Engines MUST NOT write internal/debug artifacts into public asset paths.
