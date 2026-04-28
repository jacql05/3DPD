"""Minimal age-intake validation aligned with docs/features/age-verification-intake-spec.md."""

from __future__ import annotations

from datetime import date
from typing import Any


def _parse_iso_date(value: str) -> date | None:
    parts = value.split("-")
    if len(parts) != 3:
        return None
    try:
        y, m, d = (int(parts[0]), int(parts[1]), int(parts[2]))
        return date(y, m, d)
    except ValueError:
        return None


def validate_age_intake(payload: dict[str, Any]) -> tuple[list[str], dict[str, Any] | None]:
    """Return (errors, normalized). Either subject_age (int) or birth_date (YYYY-MM-DD) required."""
    errors: list[str] = []
    if not isinstance(payload, dict):
        return (["payload must be an object"], None)

    jurisdiction = str(payload.get("jurisdiction") or "").strip().upper() or "ZZ"
    if jurisdiction != "ZZ" and len(jurisdiction) != 2:
        errors.append("jurisdiction must be two letters or omitted")

    age: int | None = None
    birth_display: str | None = None

    raw_age = payload.get("subject_age")
    birth = str(payload.get("birth_date") or "").strip()

    if raw_age is not None and str(raw_age).strip() != "":
        try:
            age = int(raw_age)
        except (TypeError, ValueError):
            errors.append("subject_age must be an integer")
        else:
            if age < 0 or age > 130:
                errors.append("subject_age out of supported range")
    elif birth:
        bd = _parse_iso_date(birth)
        if bd is None:
            errors.append("birth_date must be YYYY-MM-DD")
        else:
            birth_display = birth
            today = date.today()
            age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
            if age < 0 or age > 130:
                errors.append("derived age out of supported range")
    else:
        errors.append("subject_age or birth_date is required")

    if errors:
        return (errors, None)

    assert age is not None
    return (
        [],
        {"subject_age": age, "jurisdiction": jurisdiction, "birth_date": birth_display},
    )


def process_age_intake_submission(payload: dict[str, Any]) -> dict[str, Any]:
    errs, normalized = validate_age_intake(payload)
    if errs:
        return {"ok": False, "state": "not_started", "errors": errs, "record": None}
    return {"ok": True, "state": "in_progress", "errors": [], "record": normalized}
