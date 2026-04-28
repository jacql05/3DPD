# Domain: Identity + Verification

## Why

This domain exists so that people and organizations interacting with LuXeel, UNBND, and 3DPD can be distinguished, authenticated, and verified to the level required by product, payments, and compliance—without every other domain re-implementing identity primitives.

## Scope

### In scope

- User and organization identity lifecycle as consumed by product surfaces (sign-in, session, roles at the identity layer).
- Verification workflows required for trust (e.g. KYC-adjacent steps only where this domain owns the orchestration).
- Delegation of authoritative decisions to Compliance + Legal where regulation dictates outcome.

### Out of scope

- Detailed tax logic or payment rail selection (Payments + Tax).
- Final legal interpretation or regulatory filing (Compliance + Legal).
- Marketing identity or public storytelling (Brand + Public Narrative).

## Owner

### Accountable

Product + platform leadership, jointly with Compliance + Legal sign-off for any change that affects regulated verification outcomes.

### Consulted

Payments + Tax (payout eligibility), Operations Console (fraud ops), Infrastructure + AI Governance (secrets, keys, audit logging).

## Dependencies

### Hard dependencies

- Infrastructure + AI Governance: secure storage of credentials, keys, and audit trails for identity events.

### Soft dependencies

- Compliance + Legal: policy thresholds and evidence requirements.
- Client Experience / Creator Console: UX surfaces that invoke identity flows without owning policy.

### Temporal dependencies

- CRM + Growth: campaign attribution may attach to identity ids only after stable identity rules exist (integration phase).
