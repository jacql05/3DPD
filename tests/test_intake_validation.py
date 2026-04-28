"""Unit tests: intake validation rules."""

from identity_verification_intake.intake_form import validate_intake


def test_validate_rejects_short_name() -> None:
    errs, norm = validate_intake({"full_name": "A", "email": "a@b.co"})
    assert norm is None
    assert any("full_name" in e for e in errs)


def test_validate_rejects_bad_email() -> None:
    errs, norm = validate_intake({"full_name": "Valid Name", "email": "not-an-email"})
    assert norm is None
    assert any("email" in e for e in errs)


def test_validate_accepts_minimal_payload() -> None:
    errs, norm = validate_intake({"full_name": "Valid Name", "email": "User@Example.com"})
    assert errs == []
    assert norm is not None
    assert norm["email"] == "user@example.com"
    assert norm["jurisdiction"] == "ZZ"


def test_validate_accepts_jurisdiction() -> None:
    errs, norm = validate_intake(
        {"full_name": "Valid Name", "email": "u@example.com", "jurisdiction": "au"}
    )
    assert errs == []
    assert norm is not None
    assert norm["jurisdiction"] == "AU"
