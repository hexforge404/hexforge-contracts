# Filesystem Contract (GlyphEngine)

GlyphEngine writes all public outputs under a web-served assets root.
This document locks the canonical layout for all generated jobs.

## Canonical Public Root

`/assets/surface/`

> Note: Public URL root is `/assets/surface/` and must remain stable for v1.
> The engine name is GlyphEngine, but the **surface v1 public contract remains “surface”.**
> This avoids breaking existing paths and consumers.

## Canonical Layout (Single Source of Truth)

`/assets/surface/`
- `<subfolder?>/`
  - `<job_id>/`
    - `job.json`
    - `previews.json`
    - `enclosure/`
      - `enclosure.stl`
      - `enclosure.obj` *(optional)*
      - `enclosure.glb` *(optional)*
    - `textures/`
      - `texture.png`
      - `heightmap.png`
      - `heightmap.exr` *(optional)*
    - `previews/`
      - `hero.png`
      - `iso.png`
      - `top.png`
      - `side.png`

## Subfolder Rules

- `subfolder` is optional.
- If omitted or invalid: write directly under `/assets/surface/<job_id>/`.
- If present: write under `/assets/surface/<subfolder>/<job_id>/`.
- `subfolder` MUST be sanitized to a safe single directory name:
  - allowed: letters, numbers, dash (-), underscore (_)
  - forbidden: slashes, dots, traversal sequences

## Job ID Rules

- `job_id` is canonical and filesystem-safe.
- `job_id` MUST be unique per job.
- `job_id` folder is the stable unit of caching, download, and lookup.
- Human-friendly labels may exist inside `job.json` but are NOT used as folder names.

## Guaranteed Outputs (v1)

- `job.json`
- `previews.json`
- `enclosure/enclosure.stl`
- `textures/texture.png`
- `textures/heightmap.png`
- `previews/hero.png`, `previews/iso.png`, `previews/top.png`, `previews/side.png`

## Optional Outputs

- `textures/heightmap.exr`
- `enclosure/enclosure.obj` OR `enclosure/enclosure.glb`

## Public vs Internal

Public:
- Everything under `/assets/surface/**` is public and must be safe to serve.

Internal-only (never written under `/assets/surface/`):
- temp files, caches, intermediate renders, raw inference artifacts, debug dumps

## Do Not Break These Paths

- `/assets/surface/` MUST remain stable across versions.
- `<job_id>/` boundary is the stable unit of caching and download.
- `previews/*` and `textures/*` paths must remain stable once shipped.
