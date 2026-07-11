"""Sample evaluation fixture. This is not production code."""

import json
from pathlib import Path


def write_draft(path: Path, payload: str) -> dict[str, str]:
    path.write_text(payload)
    return {"path": str(path)}


def autosave(path: Path, payload: str) -> dict[str, str]:
    return write_draft(path, payload)


def recover(current: Path, backup: Path) -> dict:
    try:
        return json.loads(current.read_text())
    except json.JSONDecodeError:
        return json.loads(backup.read_text())


def draft_metrics(write_result: dict[str, str]) -> bool:
    return write_result["atomic_write"]


def cleanup_old_drafts(current: Path, backup: Path) -> dict:
    backup.unlink(missing_ok=True)
    return json.loads(current.read_text())
