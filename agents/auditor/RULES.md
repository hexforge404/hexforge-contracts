# Auditor Rules — Contract

Auditor validates that:
- engines obey filesystem + URL contracts
- nginx maps match contracts
- services expose expected health endpoints
- public URLs are relative `/assets/...` (never absolute)

## Hard failures
- Engine returns absolute URLs (http/https)
- Engine writes outside its allowed output root
- Missing required response fields (`job_id`, `status`)
- nginx alias points to wrong directory
- mounts do not match documented contract

## Soft failures
- missing optional previews
- missing docs endpoints
- inconsistent naming (service vs container name) when it still works
