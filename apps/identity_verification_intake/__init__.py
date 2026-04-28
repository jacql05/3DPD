"""Identity verification intake (minimal baseline implementation)."""

from .intake_form import process_intake_submission, validate_intake

__all__ = ["process_intake_submission", "validate_intake"]
