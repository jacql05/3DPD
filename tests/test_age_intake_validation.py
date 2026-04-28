"""Unit tests: age intake validation."""

from datetime import date

import pytest

import compliance_legal_age.age_intake as age_intake_mod
from compliance_legal_age.age_intake import validate_age_intake


def test_requires_age_or_birth_date() -> None:
    errs, norm = validate_age_intake({"jurisdiction": "US"})
    assert norm is None
    assert any("subject_age or birth_date" in e for e in errs)


def test_rejects_bad_age() -> None:
    errs, norm = validate_age_intake({"subject_age": 200})
    assert norm is None
    assert any("range" in e for e in errs)


def test_accepts_subject_age() -> None:
    errs, norm = validate_age_intake({"subject_age": 21, "jurisdiction": "gb"})
    assert errs == []
    assert norm is not None
    assert norm["subject_age"] == 21
    assert norm["jurisdiction"] == "GB"


def test_accepts_birth_date_with_fixed_today(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeDate(date):
        @classmethod
        def today(cls) -> date:
            return date(2020, 6, 15)

    monkeypatch.setattr(age_intake_mod, "date", FakeDate)
    errs, norm = validate_age_intake({"birth_date": "2000-01-01"})
    assert errs == []
    assert norm is not None
    assert norm["subject_age"] == 20
    assert norm["birth_date"] == "2000-01-01"
