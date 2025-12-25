# HexForge Contracts Index

This index is the single “map of the map” for every HexForge engine and service
contract in the HexForge ecosystem.

---

## Core shared schemas (mandatory)

These schemas apply to **all engines and async services**.

- `schemas/job_status.schema.json`  
  Canonical job status envelope returned by all engines.

- `schemas/job_manifest.schema.json`  
  Canonical manifest describing all public assets written by a job.
  All paths MUST be relative and begin with `/assets/`.

---

## Engines

### GlyphEngine (Surface v1)
- Filesystem: `engines/glyphengine/FILESYSTEM.md`
- Interfaces: `engines/glyphengine/INTERFACES.md`

---

## Global contract rules (non-negotiable)

- Engines MUST write public outputs under `/assets/<namespace>/...`
- Engines MUST return ONLY relative public URLs beginning with `/assets/`
- Engines MUST return job state using `job_status.schema.json`
- Engines MUST generate a job manifest using `job_manifest.schema.json`
- Engines MUST NOT write temp, debug, cache, or internal artifacts into public paths
- Consumers MUST NOT write directly into engine public asset roots

---

## Versioning rules

- Public filesystem paths are **append-only**
- Existing paths MUST NOT change for a given major contract version
- New engines get new namespaces, not new roots

---

This file is the authoritative index for all HexForge contracts.
