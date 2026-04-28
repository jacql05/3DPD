# Domain: Payments + Tax

## Why

This domain exists to move money and tax-related obligations correctly for creators, clients, and the business—with clear ledgers, reconciliation hooks, and boundaries so compliance and operations are not guessed inside feature code.

## Scope

### In scope

- Pricing, invoicing, payouts, refunds, and tax handling as implemented in product and integrations.
- Reconciliation data exposed to Operations Console and evidence summaries requested by Compliance + Legal.

### Out of scope

- Identity proofing and KYC orchestration owned by Identity + Verification.
- Legal entity structure advice or filing obligations wording (Compliance + Legal).
- Growth campaigns and attribution (CRM + Growth).

## Owner

### Accountable

Finance + product ownership for money movement; tax positions require explicit Compliance + Legal alignment.

### Consulted

Operations Console (disputes, manual adjustments), Identity + Verification (payout eligibility inputs), Infrastructure + AI Governance (PCI-adjacent boundaries, secrets).

## Dependencies

### Hard dependencies

- Identity + Verification: who is paid and under which verified context.
- Infrastructure + AI Governance: secure processing, logging, and integration endpoints.

### Soft dependencies

- Compliance + Legal: jurisdictional rules and retention.
- Creator Console / Client Experience: checkout and payout UX.

### Temporal dependencies

- New market launch: temporary coordination spikes with Compliance + Legal and Operations Console until rails stabilize.
