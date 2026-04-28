# Feature spec: Verification intake

| Field | Value |
| --- | --- |
| **Domain** | `identity-verification` |
| **Domain branch** | `domain/identity-verification` |
| **Feature branch** | `feature/identity-verification/verification-intake-spec` |
| **Baseline** | `v0.3-governance-baseline` (authority chain); implementation PRs MUST state newer `main` SHA if ahead. |
| **Domain spec** | `docs/features/domain-identity-verification.md` |

## Purpose

Define how a subject (user or organization) **enters** verification: triggers, required inputs, states, and handoffs to Compliance + Legal and Payments + Tax—without prescribing implementation stack.

## Actors

- Subject (creator, client, or org representative).
- System (Identity + Verification domain).
- Consulted: Compliance + Legal (policy thresholds), Payments + Tax (payout gating), Operations Console (exceptions).

## States (draft)

Use names only; state machine detail belongs in a later revision after accountable sign-off.

1. **Not started** — eligible to begin verification.
2. **In progress** — user action required.
3. **Pending review** — automated checks complete; human or policy queue.
4. **Verified** / **Rejected** / **Expired** — terminal outcomes (definitions tied to Compliance policy).

## Data and evidence (draft)

- What evidence types are allowed (document classes), retention pointers (Compliance), and **out of scope** data (e.g. raw payment PAN — Payments domain).

## APIs and surfaces (placeholder)

- No endpoints named here until a follow-up spec references this document and `domain-identity-verification.md` §Scope.

## Open questions

- List explicit questions for Accountable owner; none resolved in this intake-only draft.

## Change log

- **Initial draft** — spec-only branch; no runtime code.
