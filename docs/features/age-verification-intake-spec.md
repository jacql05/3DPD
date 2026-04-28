# Feature spec: Age verification intake (compliance-legal)

| Field | Value |
| --- | --- |
| **Domain** | `compliance-legal` |
| **Domain branch** | `domain/compliance-legal` |
| **Feature branch** | `feature/compliance-legal/age-verification` |
| **Baseline** | `v0.4-execution-baseline` |
| **Domain spec** | `docs/features/domain-compliance-legal.md` |
| **Related** | `docs/features/verification-intake-spec.md` (identity intake; this spec covers **age** evidence only) |

## Purpose

Minimal intake for **age-related** compliance checks: capture subject age or birth date plus jurisdiction placeholder, without implementing full KYC or identity proofing (Identity + Verification domain).

## Out of scope

- Identity document capture / liveness (Identity + Verification).
- Payout eligibility (Payments + Tax).

## States (draft)

Same pattern as identity intake: `not_started` → `in_progress` on successful validation of submitted fields.
