# HexForge Contracts Index

This index is the single “map of the map” for every HexForge engine/agent contract.

---

## Core shared schemas (must be used by all engines)

- `schemas/job_status.schema.json`  
  Standard status envelope all engines MUST return.

- `schemas/job_manifest.schema.json`  
  Standard manifest describing public outputs written for a job (relative `/assets/...` paths).

---

## Engines

### GlyphEngine (Surface v1)
- Filesystem: `engines/glyphengine/FILESYSTEM.md`
- Interfaces: `engines/glyphengine/INTERFACES.md`

---

## Global contract rules (non-negotiable)

- Engines MUST write public outputs under `/assets/<namespace>/...` via the nginx-served host mount.
- Engines MUST return ONLY relative public URLs beginning with `/assets/`.
- Engines MUST return job status using `schemas/job_status.schema.json`.
- Engines MUST generate a job manifest using `schemas/job_manifest.schema.json`.
- Engines MUST NOT write internal/debug/temp artifacts into public asset paths.
- Consumers (frontend/backend/assistant/foundry) MUST NOT write directly into engine public roots.
