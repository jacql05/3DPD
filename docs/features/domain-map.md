# Domain Map

This file defines the current first-level domain boundaries for 3DPD.

## Naming Rules

- Git branch name MUST follow: `domain/<slug>`
- Domain spec file MUST follow: `docs/features/domain-<slug>.md`
- The `<slug>` MUST be identical across branch name and spec file.
- A domain cannot be considered valid unless both the branch and the spec file use the same slug.

## Evolution Rule

The current domain model contains nine first-level domains.

Adding, removing, renaming, or merging domains requires approval through `docs/governance/AUTHORITY-PROMOTION.md`.

No new domain may be created silently through an ad-hoc branch or document.

## Domains

| Domain | Slug | Spec |
| --- | --- | --- |
| Identity + Verification | `identity-verification` | `domain-identity-verification.md` |
| Payments + Tax | `payments-tax` | `domain-payments-tax.md` |
| Compliance + Legal | `compliance-legal` | `domain-compliance-legal.md` |
| Creator Console | `creator-console` | `domain-creator-console.md` |
| Client Experience | `client-experience` | `domain-client-experience.md` |
| Operations Console | `operations-console` | `domain-operations-console.md` |
| CRM + Growth | `crm-growth` | `domain-crm-growth.md` |
| Brand + Public Narrative | `brand-public-narrative` | `domain-brand-public-narrative.md` |
| Infrastructure + AI Governance | `infrastructure-ai-governance` | `domain-infrastructure-ai-governance.md` |

## Version chain

- Documentation and repo skeleton: `v0.1-docs-baseline`
- Domain architecture (this map + per-domain specs): `v0.2-domain-baseline`
- Governance execution (branch policy, pre-commit safe mode, JIT domain branches): `v0.3-governance-baseline`

Full ladder and rules: `docs/governance/RELEASE-POLICY.md`.

Later baselines extend this chain; they do not replace prior tags without an explicit governance decision.
