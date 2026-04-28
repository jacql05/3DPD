"""Integration-style tests: age intake submission."""

from compliance_legal_age.age_intake import process_age_intake_submission


def test_submission_happy_path_with_age() -> None:
    result = process_age_intake_submission({"subject_age": 17, "jurisdiction": "au"})
    assert result["ok"] is True
    assert result["state"] == "in_progress"
    assert result["record"]["subject_age"] == 17
    assert result["record"]["jurisdiction"] == "AU"


def test_submission_rejected_without_fields() -> None:
    result = process_age_intake_submission({})
    assert result["ok"] is False
    assert result["state"] == "not_started"
    assert result["record"] is None
