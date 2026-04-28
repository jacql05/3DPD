"""Minimal verification intake validation and submission handling.

See docs/features/verification-intake-spec.md (states: not_started, in_progress).
"""

from __future__ import annotations

import re
from typing import Any

_EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validate_intake(payload: dict[str, Any]) -> tuple[list[str], dict[str, str] | None]:
    """Return (errors, normalized_fields). normalized is None when invalid."""
    errors: list[str] = []
    if not isinstance(payload, dict):
        return (["payload must be an object"], None)

    full_name = str(payload.get("full_name") or "").strip()
    email = str(payload.get("email") or "").strip()
    raw_j = str(payload.get("jurisdiction") or "").strip().upper()
    jurisdiction = raw_j if raw_j else "ZZ"

    if len(full_name) < 2:
        errors.append("full_name must be at least 2 characters")
    if not email:
        errors.append("email is required")
    elif not _EMAIL_RE.match(email):
        errors.append("email format is invalid")
    if jurisdiction != "ZZ" and len(jurisdiction) != 2:
        errors.append("jurisdiction must be two letters or omitted")

    if errors:
        return (errors, None)
    return (
        [],
        {
            "full_name": full_name,
            "email": email.lower(),
            "jurisdiction": jurisdiction,
        },
    )


def process_intake_submission(payload: dict[str, Any]) -> dict[str, Any]:
    """Simulate form submission: validate then move subject to in_progress on success."""
    errs, normalized = validate_intake(payload)
    if errs:
        return {"ok": False, "state": "not_started", "errors": errs, "record": None}
    return {"ok": True, "state": "in_progress", "errors": [], "record": normalized}
