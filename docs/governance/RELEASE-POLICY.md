# Release Policy

This document defines versioning, **baseline tags**, release cadence, and what qualifies as a releasable state for 3DPD. It complements `docs/governance/BRANCH-POLICY.md` and `docs/features/domain-map.md`.

## Baseline tags (fixed ladder)

Repository **authority baselines** use lightweight tags with this fixed naming scheme (do not invent ad-hoc tag names for the same role):

| Tag | Meaning |
| --- | --- |
| `v0.1-docs-baseline` | Documentation skeleton and initial governance placeholders. |
| `v0.2-domain-baseline` | Domain map + per-domain specs (first-level boundaries). |
| `v0.3-governance-baseline` | Executable governance: branch policy, pre-commit safe mode contract, JIT `domain/*` lines. |
| `v0.4-execution-baseline` | First integrated application / execution plane agreed for production path (TBD when reached). |
| `v0.5-release-baseline` | First repeatable release train (CI, artifacts, rollback naming) (TBD when reached). |

**Rules:**

- New baselines **append** to the chain; they do not delete or retag prior baselines without a decision recorded in `AUTHORITY-PROMOTION.md`.
- Application semver (e.g. `v1.0.0` for a shipped app) is **separate** from these `v0.x-*-baseline` tags unless explicitly unified in a future governance amendment.

## Product releases (future)

When `apps/` contain shippable artifacts:

- **Semantic versioning** for user-facing or API releases: `MAJOR.MINOR.PATCH` as defined when the first release candidate exists.
- **CHANGELOG** or release notes MUST reference the baseline tag the release was cut from (e.g. built on `main` at or after `v0.3-governance-baseline`).

## Cadence

Until `v0.4-execution-baseline` exists, cadence is **documentation and governance first**: merge via PR, tag baselines deliberately, avoid drive-by tags on `main`.

## Rollback

Prefer **tag rollback** to a known baseline or semver tag, then forward-fix. See `BRANCH-POLICY.md` rollback table for merge vs hotfix vs revert.

## References

- `docs/features/domain-map.md` — version chain summary
- `docs/governance/BRANCH-POLICY.md` — merge paths and hotfix rules
