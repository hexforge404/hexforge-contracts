# HexForge Contracts

Single source of truth for how HexForge engines and agents:
- expose APIs
- write outputs to disk
- report status
- reference public assets

This repo is **authoritative**. Engines must implement these contracts. The Auditor enforces them.

## Layout

- `docs/CONTRACTS_INDEX.md` — index of all contracts
- `schemas/` — shared JSON schemas (job status, manifest formats)
- `engines/<engine>/` — per-engine filesystem + interface contracts
- `templates/` — boilerplate docs for new engines
