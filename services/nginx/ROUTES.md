# nginx Routes — Contract

nginx is the public edge for:
- hexforgelabs.com (main app)
- tools.hexforgelabs.com (tools endpoints)

## Public routes (stable)

### React SPA
- `/` → frontend build output

### Backend API
- `/api/` → backend service (Node/Express)

### Surface API (public name stays `/api/surface`)
- `/api/surface/` → glyphengine internal service

### Public assets
- `/assets/surface/` → surface outputs
- `/assets/heightmap/` → legacy heightmap outputs
- `/images/` → uploaded images alias (uploads folder)

## Important rule
Public route names MUST NOT change just because internal services are renamed.
Internal renames are handled by nginx upstreams only.
