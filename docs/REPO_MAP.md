# Repo Map — HexForge Contracts

This repository is the single source of truth for how HexForge services/engines:
- expose APIs
- write outputs to disk
- reference public assets
- report status (for orchestration + UI)

## Layout

- `docs/`
  - `CONTRACTS_INDEX.md` — index of all contracts (start here)
  - `REPO_MAP.md` — this file

- `schemas/`
  - `common/` — shared JSON schemas used everywhere

- `engines/`
  - `glyphengine/` — texture-first surface + enclosure engine (authoritative)
  - `surface/` — legacy alias docs (public route name remains `/api/surface`)

- `services/`
  - `backend/` — API gateway + persistence layer
  - `media-api/` — content engine/media processing service
  - `mongo/` — database expectations
  - `nginx/` — routing + SSL expectations
  - `ollama/` — local LLM service expectations

- `agents/`
  - `assistant/` — orchestration agent contract

- `auditor/`
  - contract enforcement rules + report formats

- `infra/paths/`
  - host paths, container mounts, and URL mapping (the “truth table”)
