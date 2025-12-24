# Backend Interfaces — Contract

## Internal DNS
- Service name: `backend`
- Suggested internal URL: `http://backend:8000` (or `http://hexforge-backend:8000`)

## Public edge
- nginx exposes `/api/*` → backend

## Health
- `GET /health` must return 200 OK

## Asset references
Backend responses that reference generated engine outputs MUST use:
- relative `/assets/...` paths only
