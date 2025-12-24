# Assistant ENV — Contract

Assistant is an orchestration agent that:
- creates jobs in engines
- polls status
- validates outputs exist
- routes tool calls

## Required
- `OLLAMA_URL`
- `OLLAMA_MODEL`

## Tool integrations
- `SCRIPT_LAB_URL`
- `SCRIPT_LAB_TOKEN`
- `CONTENT_ENGINE_URL`

## Filesystem read-only expectations
Assistant may read:
- `/data/hexforge3d/*` (mounted engine root)

Assistant must NOT write directly into public asset roots unless explicitly allowed by an engine contract.
