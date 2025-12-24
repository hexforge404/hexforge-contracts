# Assistant Interfaces — Contract

## Internal URL
- `http://assistant:11435` (or container name `hexforge-assistant`)

## Health
- `GET /health` → 200 OK

## Public edge routes (nginx)
- `/tool/*` → assistant tool routes
- `/mcp/*`  → assistant MCP routes
- `/ws`     → websocket streaming

## Rule
Assistant must treat engine outputs as immutable once jobs are complete.
