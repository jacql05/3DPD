# Domain: Compliance + Legal

## Why

This domain exists to hold regulatory and contractual truth: what the business must do, what evidence must exist, and how exceptions are decided—so other domains do not silently encode law or policy in code comments.

## Scope

### In scope

- Regulatory and contractual requirements expressed as authoritative requirements and evidence expectations.
- Approval gates for high-risk changes (payments, data, minors, AI outputs where regulated).
- Retention, consent, and cross-border constraints as they apply to the platform.

### Out of scope

- Implementation of payment rails (Payments + Tax).
- Day-to-day fraud queue handling (Operations Console).
- Public marketing copy (Brand + Public Narrative).

## Owner

### Accountable

Legal / compliance leadership; promotion of “truth” documents follows `docs/governance/AUTHORITY-PROMOTION.md`.

### Consulted

Identity + Verification, Payments + Tax, Infrastructure + AI Governance, CRM + Growth (where data use affects compliance).

## Dependencies

### Hard dependencies

- None for defining policy; enforcement depends on Infrastructure + Identity + Payments for technical realization.

### Soft dependencies

- All domains: each must consult when scope touches personal data, money, or regulated content.

### Temporal dependencies

- Product launches: time-boxed reviews until launch checklist is complete.
