"""Payout intake validation only — see docs/features/payout-intake-spec.md.

No external calls, no Stripe, no movement of real funds.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any


def _forbidden_payment_vendor_keys(payload: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    stripe_msg = "stripe-related fields are not accepted in payout intake"
    stripe_reported = False
    for key in payload:
        kl = str(key).lower()
        if "stripe" in kl:
            if not stripe_reported:
                errs.append(stripe_msg)
                stripe_reported = True
        elif kl in ("card_number", "pan", "cvv", "payment_intent_id"):
            errs.append(f"forbidden sensitive field: {key}")
    return errs


def validate_payout_intake(payload: dict[str, Any]) -> tuple[list[str], dict[str, str] | None]:
    """Validate a payout intake record. Does not execute payouts.

    Returns ``(errors, normalized)`` where ``normalized`` is ``None`` if validation failed.
    """
    errors: list[str] = []
    if not isinstance(payload, dict):
        return (["payload must be an object"], None)

    errors.extend(_forbidden_payment_vendor_keys(payload))
    currency = str(payload.get("currency") or "").strip().upper()
    ref = str(payload.get("payee_reference") or "").strip()
    amount_raw = payload.get("amount")

    if len(ref) < 3:
        errors.append("payee_reference must be at least 3 characters")
    if len(currency) != 3 or not currency.isalpha():
        errors.append("currency must be three letters (ISO-style placeholder)")

    amt: Decimal | None = None
    try:
        amt = Decimal(str(amount_raw))
    except (InvalidOperation, TypeError):
        errors.append("amount must be a decimal number")
    else:
        if amt <= 0:
            errors.append("amount must be positive")
        if amt > Decimal("999999.99"):
            errors.append("amount exceeds maximum intake placeholder")
        if amt.as_tuple().exponent < -2:
            errors.append("amount supports at most 2 decimal places")

    if errors:
        return (errors, None)

    assert amt is not None
    return (
        [],
        {
            "amount": format(amt, "f"),
            "currency": currency,
            "payee_reference": ref,
        },
    )


def process_payout_intake_submission(payload: dict[str, Any]) -> dict[str, Any]:
    errs, normalized = validate_payout_intake(payload)
    if errs:
        return {"ok": False, "state": "not_started", "errors": errs, "record": None}
    return {"ok": True, "state": "in_progress", "errors": [], "record": normalized}
