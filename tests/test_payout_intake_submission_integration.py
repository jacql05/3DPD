"""Integration-style tests: payout intake submission."""

from payments_tax_payout_intake.payout_intake import process_payout_intake_submission


def test_submission_normalizes_currency_and_amount_on_success() -> None:
    result = process_payout_intake_submission(
        {
            "amount": "50.00",
            "currency": "eur",
            "payee_reference": "seller-ledger-42",
        }
    )
    assert result["ok"] is True
    assert result["state"] == "in_progress"
    assert result["record"]["currency"] == "EUR"
    assert result["record"]["amount"] == "50.00"


def test_submission_rejects_empty_payload() -> None:
    result = process_payout_intake_submission({})
    assert result["ok"] is False
    assert result["state"] == "not_started"
    assert result["record"] is None
