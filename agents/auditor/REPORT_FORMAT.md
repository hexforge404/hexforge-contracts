# Auditor Report Format — Contract

Auditor outputs a single report JSON plus human summary.

## Files
- `audit_report.json`
- `audit_report.md`

## JSON shape (minimum)
```json
{
  "run_id": "audit_YYYYMMDD_HHMMSS",
  "status": "pass|warn|fail",
  "checks": [
    {
      "id": "nginx.assets.surface.alias",
      "status": "pass|warn|fail",
      "message": "…",
      "evidence": ["optional strings"]
    }
  ]
}



