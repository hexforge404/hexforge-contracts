# Media API Interfaces — Contract

## Internal DNS
- `media_api` (compose) / `hexforge-media-api` (container)

## Internal URL
- `http://hexforge-media-api:8700`

## Auth
Requests must include:
- `X-Media-Api-Key: <MEDIA_API_KEY>`

## Health
- `GET /health` → 200 OK
