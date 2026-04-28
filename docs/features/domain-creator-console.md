# Domain: Creator Console

## Why

This domain exists so creators (LuXeel / UNBND / 3DPD supply side) have a coherent place to manage work, assets, earnings visibility, and settings—without leaking operations or compliance internals into ad-hoc surfaces.

## Scope

### In scope

- Creator-facing workflows: portfolios, deliverables, earnings summaries, tax and payout self-service entry points.
- Creator-specific configuration that does not belong in client-only or ops-only consoles.

### Out of scope

- Back-office administration (Operations Console).
- End-client buying journey (Client Experience).
- Underlying payment execution (Payments + Tax).

## Owner

### Accountable

Product owner for creator experience; changes affecting money or compliance require Payments + Tax / Compliance + Legal sign-off.

### Consulted

Payments + Tax, Identity + Verification, Operations Console (support escalations), Infrastructure + AI Governance (uploads, AI-assisted tools).

## Dependencies

### Hard dependencies

- Identity + Verification: creator accounts and roles.
- Infrastructure + AI Governance: media storage, AI feature guardrails where creators use them.

### Soft dependencies

- Payments + Tax: balances and payout status.
- CRM + Growth: lifecycle messaging where it touches in-product surfaces.

### Temporal dependencies

- New creator programs: campaign-specific UI may be temporal until standardized.
