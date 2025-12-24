# Container Mounts — Authoritative Mapping

This defines how host paths are mounted into containers so that:
- engines can write outputs
- nginx can serve assets
- services can reference stable public URLs

## nginx container
Mount:
- Host: `/mnt/hdd-storage/ai-tools/engines/hexforge3d`
- Container: `/var/www/hexforge3d`

Meaning:
- `/var/www/hexforge3d/surface` → serves `/assets/surface/`
- `/var/www/hexforge3d/output`  → serves `/assets/heightmap/` (legacy)

## glyphengine container (surface engine renamed)
Mount:
- Host: `/mnt/hdd-storage/ai-tools/engines/hexforge3d`
- Container: `/data/hexforge3d`

Meaning:
- Engine writes to: `/data/hexforge3d/surface/...`
- Engine returns URLs starting with: `/assets/surface/...`

## assistant container
Mount:
- Host: `/mnt/hdd-storage/ai-tools/engines/hexforge3d`
- Container: `/data/hexforge3d`

Meaning:
- Assistant can read outputs (public assets)
- Assistant may create jobs via API (preferred) and validate files exist
