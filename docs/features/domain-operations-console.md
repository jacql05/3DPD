# Domain: Operations Console

## Why

This domain exists so internal teams can run the business safely: support, fraud, fulfillment, and configuration—without using creator or client surfaces as a back door, and with actions that are auditable and policy-bound.

## Scope

### In scope

- Internal tools for queues, overrides, configuration, and observability hooks used by operations and support.
- Manual interventions that require human judgment (refunds, account holds) within policy.

### Out of scope

- Defining regulatory policy (Compliance + Legal).
- Public-facing UX (Client Experience / Creator Console).
- Growth experiments (CRM + Growth) except where ops executes an approved playbook.

## Owner

### Accountable

Head of operations (or equivalent); destructive or financial actions require dual control per internal policy.

### Consulted

Compliance + Legal, Payments + Tax, Identity + Verification, Infrastructure + AI Governance.

## Dependencies

### Hard dependencies

- Infrastructure + AI Governance: authn/z for internal tools, audit logs, environment separation.

### Soft dependencies

- All customer-facing domains: read/write surfaces must respect their ownership boundaries.

### Temporal dependencies

- Incident response: temporary elevated access windows documented per procedure.
