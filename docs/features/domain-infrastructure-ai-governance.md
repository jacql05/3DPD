# Domain: Infrastructure + AI Governance

## Why

This domain exists so runtime platforms, data stores, networking, CI/CD, observability, and AI systems share enforceable guardrails—secrets, tenancy, logging, model use, and cost—so feature domains do not each invent incompatible “infra.”

## Scope

### In scope

- Cloud and platform choices, environments, backups, monitoring, and incident baselines.
- AI usage policy: allowed models, data residency constraints, logging, human review gates, and kill switches.
- Cross-cutting security controls consumed by other domains.

### Out of scope

- Product-specific UX logic (Client Experience / Creator Console).
- Legal interpretation of AI outputs (Compliance + Legal).
- Pricing and payout rules (Payments + Tax).

## Owner

### Accountable

Engineering + platform leadership; AI governance changes require Compliance + Legal when outputs affect users or regulated data.

### Consulted

All domains for intake requests; Operations Console for on-call and incident tooling.

## Dependencies

### Hard dependencies

- Compliance + Legal: data classification and AI constraints where regulated.

### Soft dependencies

- Every domain: consumes APIs, storage, and AI capabilities provided here.

### Temporal dependencies

- Vendor migrations or model upgrades: phased rollouts with explicit rollback tags aligned to release policy.
