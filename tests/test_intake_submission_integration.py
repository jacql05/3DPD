"""Integration-style tests: end-to-end submission behavior."""

from identity_verification_intake.intake_form import process_intake_submission


def test_submission_happy_path_moves_to_in_progress() -> None:
    body = {
        "full_name": "Ada Lovelace",
        "email": "ada@example.com",
        "jurisdiction": "gb",
    }
    result = process_intake_submission(body)
    assert result["ok"] is True
    assert result["state"] == "in_progress"
    assert result["errors"] == []
    assert result["record"]["full_name"] == "Ada Lovelace"
    assert result["record"]["email"] == "ada@example.com"
    assert result["record"]["jurisdiction"] == "GB"


def test_submission_rejects_and_stays_not_started() -> None:
    result = process_intake_submission({"full_name": "", "email": "bad"})
    assert result["ok"] is False
    assert result["state"] == "not_started"
    assert result["record"] is None
    assert result["errors"]
