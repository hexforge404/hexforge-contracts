from datetime import datetime, timezone
from typing import Dict, Optional, Any


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def job_status_envelope(
    *,
    job_id: str,
    status: str,
    public_root: str,
    updated_at: Optional[str] = None,
    service: Optional[str] = None,
    subfolder: Optional[str] = None,
    message: Optional[str] = None,
    progress: Optional[float] = None,
    artifacts: Optional[Dict[str, Any]] = None,
    errors: Optional[list] = None,
) -> Dict[str, Any]:
    env = {
        "job_id": job_id,
        "status": status,
        "public_root": public_root,
        "updated_at": updated_at or now_iso(),
    }

    if service is not None:
        env["service"] = service
    if subfolder is not None:
        env["subfolder"] = subfolder
    if message is not None:
        env["message"] = message
    if progress is not None:
        env["progress"] = progress
    if artifacts is not None:
        env["artifacts"] = artifacts
    if errors is not None:
        env["errors"] = errors

    return env
