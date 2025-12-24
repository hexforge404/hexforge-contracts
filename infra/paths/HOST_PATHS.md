# Host Paths — Authoritative Mount Points

These are canonical host paths used across the HexForge stack.
Changing these requires updating docker mounts and nginx aliases.

## Root
- `/mnt/hdd-storage/` — primary storage root on Proxmox

## Engine Output Roots
- `/mnt/hdd-storage/ai-tools/engines/hexforge3d/`
  - `surface/`  → public surface outputs (textures/enclosures/previews)
  - `relief/`   → public relief/heightmap-to-STL outputs (if separate)
  - `output/`   → existing heightmap outputs (legacy path used by store)
  - `pack/`     → packaged bundles (zip manifests etc.)
  - `docs/`     → generated documentation artifacts (optional)
  - `audit/`    → audit logs / reports
  - `foundry/`  → future assembly/pipeline outputs

## Store Repo
- `/mnt/hdd-storage/hexforge-store/` — main stack repo (compose + nginx + app)

## Content Engine
- `/mnt/hdd-storage/hexforge-content-engine/` — media_api build context + media workflows
