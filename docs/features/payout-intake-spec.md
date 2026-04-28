# Feature spec: Payout intake (payments-tax)

| Field | Value |
| --- | --- |
| **Domain** | `payments-tax` |
| **Domain branch** | `domain/payments-tax` |
| **Feature branch** | `feature/payments-tax/payout-intake` |
| **Baseline** | `v0.5-release-baseline` |
| **Domain spec** | `docs/features/domain-payments-tax.md` |

## Purpose

Capture a **minimal, non-executing** payout request intake: amount, currency, and payee reference for validation only. Used to prove the **payments-tax** promotion chain without touching real money, card data, or third-party processors (no Stripe, no live rails).

## Explicitly out of scope

- Executing payouts, settlements, or tax filing.
- Stripe or any PSP API keys, webhooks, or `PaymentIntent` objects.
- PCI payloads (PAN, CVV, raw card numbers).

## States (draft)

`not_started` → `in_progress` after successful validation of the intake record (same pattern as other intake baselines).
