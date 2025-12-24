# URL Map — Disk ↔ nginx ↔ Public URLs

This repo treats URLs as a contract.
Engines MUST return relative public URLs beginning with `/assets/...`.

## Root mapping

| Purpose | Host Path | nginx Path | Public URL |
|---|---|---|---|
| Surface outputs | `/mnt/hdd-storage/ai-tools/engines/hexforge3d/surface` | `/var/www/hexforge3d/surface` | `/assets/surface/` |
| Heightmap outputs (legacy) | `/mnt/hdd-storage/ai-tools/engines/hexforge3d/output` | `/var/www/hexforge3d/output` | `/assets/heightmap/` |
| Uploads (store) | `./uploads` (repo) | `/uploads` | `/images/` (alias) |

## Rules
- Engines return ONLY relative paths: `/assets/...`
- nginx is responsible for converting disk → URL
- Clients resolve absolute origin using environment config
