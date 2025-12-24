# SSL — Contract

This stack uses certbot/letsencrypt certificates mounted into nginx.

## Required host path
- `/etc/letsencrypt/live/hexforgelabs.com/fullchain.pem`
- `/etc/letsencrypt/live/hexforgelabs.com/privkey.pem`

## nginx requirements
- listen 443 ssl
- http2 enabled
- supports Cloudflare forwarding headers

## Cloudflare note
If Cloudflare is proxying traffic, ensure nginx respects:
- `X-Forwarded-Proto`
- redirect logic should avoid loops
