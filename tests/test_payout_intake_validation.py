"""Unit tests: payout intake validation."""

from decimal import Decimal

from payments_tax_payout_intake.payout_intake import validate_payout_intake


def test_rejects_stripe_key_field() -> None:
    errs, norm = validate_payout_intake(
        {
            "amount": "10.00",
            "currency": "aud",
            "payee_reference": "creator-001",
            "stripe_secret": "sk_test_xxx",
        }
    )
    assert norm is None
    assert any("stripe" in e.lower() for e in errs)


def test_rejects_multiple_stripe_key_fields_with_single_stripe_message() -> None:
    errs, norm = validate_payout_intake(
        {
            "amount": "10.00",
            "currency": "aud",
            "payee_reference": "creator-001",
            "stripe_secret": "sk_test_xxx",
            "stripe_publishable": "pk_test_xxx",
        }
    )
    assert norm is None
    stripe_msgs = [e for e in errs if "stripe" in e.lower()]
    assert len(stripe_msgs) == 1


def test_rejects_amount_with_more_than_two_decimal_places() -> None:
    errs, norm = validate_payout_intake(
        {
            "amount": "10.001",
            "currency": "AUD",
            "payee_reference": "creator-001",
        }
    )
    assert norm is None
    assert any("decimal" in e.lower() for e in errs)


def test_accepts_valid_intake() -> None:
    errs, norm = validate_payout_intake(
        {
            "amount": Decimal("123.45"),
            "currency": "usd",
            "payee_reference": "acct-xyz-99",
        }
    )
    assert errs == []
    assert norm is not None
    assert norm["currency"] == "USD"
    assert norm["amount"] == "123.45"


def test_rejects_short_payee_reference() -> None:
    errs, norm = validate_payout_intake(
        {"amount": "1", "currency": "AUD", "payee_reference": "ab"}
    )
    assert norm is None
    assert any("payee_reference" in e for e in errs)
