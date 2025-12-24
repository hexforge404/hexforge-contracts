# Pack Engine — Interfaces Contract

## Internal DNS
- `pack` (service name)

## API
- `POST /api/pack/jobs`
- `GET /api/pack/jobs/{pack_id}`
- `GET /api/pack/jobs/{pack_id}/assets`

## Response rule
Must include:
- `job_id`
- `status`
- `result.public.*` relative `/assets/...` URLs
