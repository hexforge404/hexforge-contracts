# Interfaces (Routes, Ports, Contracts)

This document defines the public and internal interface contract for **HexForge GlyphEngine**.
All consumers (frontend, backend, assistant, foundry, auditor) must conform to this contract.

## Service Identity

- Service name (docker): `glyphengine`
- Internal base URL: `http://glyphengine:8092`

> Public API prefix remains `/api/surface/` for v1 stability.

## Ports

- `8092/tcp` : GlyphEngine HTTP API (Surface v1 routes)
- `8188/tcp` : Optional local ComfyUI (internal only)
- Blender integration runs headless; no public port required

## API Overview (v1)

- All endpoints are versioned implicitly by repository version.
- All responses MUST include `job_id` and `status`.
- Status envelope SHOULD conform to `schemas/job_status.schema.json` from the contracts repo.
- All public file references MUST be relative paths starting with `/assets/`.

## Routes (stable v1)

### POST `/api/surface/jobs`
Creates a new surface + enclosure job.

Minimal request body example:
```json
{
  "subfolder": "optional-project-or-product",
  "enclosure": {
    "inner_mm": [70, 40, 18],
    "wall_mm": 2.4,
    "lid_split": "z",
    "lid_ratio": 0.25,
    "features": {
      "standoffs": [],
      "cutouts": []
    }
  },
  "texture": {
    "prompt": "circuit board, cyberpunk, clean lines",
    "seed": 123,
    "size": [1024, 1024]
  }
}
GET /api/surface/jobs/{job_id}
Returns job status and public asset references when complete.

GET /api/surface/jobs/{job_id}/assets
Returns a structured list of downloadable public assets.

Response Contract (example)
json
Copy code
{
  "job_id": "ge_2025-12-22_abcdef",
  "status": "complete",
  "result": {
    "public": {
      "root": "/assets/surface/<subfolder?>/<job_id>/",
      "enclosure": {
        "stl": "/assets/surface/.../enclosure/enclosure.stl",
        "handoff": "/assets/surface/.../enclosure/enclosure.obj"
      },
      "textures": {
        "texture_png": "/assets/surface/.../textures/texture.png",
        "heightmap_png": "/assets/surface/.../textures/heightmap.png",
        "heightmap_exr": "/assets/surface/.../textures/heightmap.exr"
      },
      "previews": {
        "hero": "/assets/surface/.../previews/hero.png",
        "iso": "/assets/surface/.../previews/iso.png",
        "top": "/assets/surface/.../previews/top.png",
        "side": "/assets/surface/.../previews/side.png"
      },
      "job_json": "/assets/surface/.../job.json"
    }
  }
}
URL Rules
Engine returns ONLY relative URLs for public assets.

Consumers resolve absolute URLs using environment config (nginx/proxy safe).

This ensures compatibility with nginx, reverse proxies, and Cloudflare.

Subfolder Rules
subfolder is optional.

If provided, it MUST be sanitized to a single folder name:

allowed: letters, numbers, dash (-), underscore (_)

forbidden: slashes, dots, traversal sequences

Invalid subfolders MUST be ignored or replaced with a sanitized value.

Permissions
Allowed (assistant/foundry)
Create jobs

Poll status

Read public asset paths

Forbidden
Direct filesystem writes into engine public root by consumers

Modifying completed jobs

Accessing internal-only directories

yaml
Copy code

---

# ✅ Save everything fast (commands)
If you want to write all of these with commands instead of manual pasting, say so and I’ll give you a **copy/paste “cat <<EOF” bundle**.

For now, after you paste/save:

```bash
cd ~/hexforge/contracts
git status
git add .
git commit -m "init: contracts index + job status schema + glyphengine contracts"