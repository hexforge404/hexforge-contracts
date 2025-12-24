# Backend ENV — Contract

Backend is the API gateway + persistence layer.

## Required
- `MONGO_URI` (or components for building it)
- `SESSION_SECRET`
- `MEDIA_API_URL`
- `MEDIA_API_KEY`

## Optional / integrations
- Stripe keys
- Mailgun keys
- Script lab token

## Contract rule
Backend must never leak secrets in API responses or logs.
