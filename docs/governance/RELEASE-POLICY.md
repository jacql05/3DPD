# Release Policy

This document defines versioning, **baseline tags**, **release / rollback / hotfix / operational recovery**, and what qualifies as a releasable state for 3DPD. It complements `docs/governance/BRANCH-POLICY.md` and `docs/features/domain-map.md`.

## Baseline tags (fixed ladder)

Repository **authority baselines** use lightweight tags with this fixed naming scheme (do not invent ad-hoc tag names for the same role):

| Tag | Meaning |
| --- | --- |
| `v0.1-docs-baseline` | Documentation skeleton and initial governance placeholders. |
| `v0.2-domain-baseline` | Domain map + per-domain specs (first-level boundaries). |
| `v0.3-governance-baseline` | Executable governance: branch policy, pre-commit safe mode contract, JIT `domain/*` lines. |
| `v0.4-execution-baseline` | First governed **execution path** merged to `main` (domain → `integration` → `main`) with CI green. |
| `v0.5-release-baseline` | **Release & recovery governance** documented in this file + `OPERATIONAL-RECOVERY.md`, with CI gate verifying required sections exist; tag only after merge to `main`. |

**Rules:**

- New baselines **append** to the chain; they do not delete or retag prior baselines without a decision recorded in `AUTHORITY-PROMOTION.md`.
- Application semver (e.g. `v1.0.0` for a shipped app) is **separate** from these `v0.x-*-baseline` tags unless explicitly unified in a future governance amendment.

## v0.5-release-baseline — completion criteria

Tag **`v0.5-release-baseline`** on `main` **only when all** of the following are true:

1. This `RELEASE-POLICY.md` revision is merged to `main` and contains the sections **Release train**, **Rollback ladder**, **Hotfix path**, and **Operational recovery** (headings as below).
2. `docs/governance/OPERATIONAL-RECOVERY.md` exists on `main`.
3. `governance-ci` (required check) passes on the merge commit — including file/heading checks for the above.

## Release train (normal)

**Definition:** A **release train** is the ordered promotion of trusted commits to `main` with green checks, plus (when shipping product) an immutable **artifact** and **release notes**.

| Step | Action |
| --- | --- |
| 1 | Work lands via `feature/*` → `domain/*` → `integration` → `main` per `BRANCH-POLICY.md`. |
| 2 | Ensure `governance-sanity` and `tests` workflows are **green** on the PR that promotes to `main`. |
| 3 | For application semver: tag `vX.Y.Z` from the **exact** `main` SHA that built the artifact; notes MUST cite the baseline tag the release trusts (e.g. at or after `v0.4-execution-baseline`). |
| 4 | Publish artifact (container image, wheel, etc.) from CI or documented pipeline — not from a developer laptop without record. |

## Rollback ladder

| Symptom | First move | Owner |
| --- | --- | --- |
| Bad merge on `integration` or `domain/*` | **Revert** merge commit on that branch; do not rewrite public history. | Domain / integration owner |
| Bad deploy from `main` but repo is fine | **Redeploy** previous artifact or **checkout** previous semver tag in deploy system. | Ops / platform |
| Bad commit already on `main`, no deploy yet | **Revert** on `main` via PR; follow with domain branch reconciliation PR if needed. | Maintainer |
| Production defect needs immediate code fix | **Hotfix** path below | On-call + maintainer |

**Tag rollback:** If the team only needs to **reference** a known-good repo state, use baseline tags (`v0.4-execution-baseline`, etc.) or app semver tags — document which tag was used in the incident log.

## Hotfix path

Hotfix rules are **authoritative** in `BRANCH-POLICY.md` — *Hotfix exception*. Summary:

- Branch `hotfix/<slug>` → PR to `main` only for **urgent** production/legal exposure.
- PR MUST state severity, blast radius, owner, and link/post to reconciliation of `domain/*` within one business day (or sooner per org policy).

## Operational recovery

**Runbook:** `docs/governance/OPERATIONAL-RECOVERY.md` — roles, stabilize, evidence, post-incident engineering and spec updates.

## Audit (v0.4 execution baseline)

**Do not** tag `v0.4-execution-baseline` until the promotion PR from `integration` to `main` is **merged** (not merely open) and status checks are green.

If a **single maintainer** temporarily reduced GitHub **Require approvals** on `main` from **1** to **0** to complete that merge, the audit chain MUST include this exact sentence in the same window (PR description and/or this repository):

> **Single-maintainer exception used for v0.4 bootstrap.**

Restore **Require approvals** to **1** immediately after merge. Full procedure: `BRANCH-POLICY.md` — *Single-maintainer exception*.

## Product releases (semver)

When `apps/` contain shippable artifacts:

- **Semantic versioning** for user-facing or API releases: `MAJOR.MINOR.PATCH` as defined when the first release candidate exists.
- **CHANGELOG** or release notes MUST reference the baseline tag the release was cut from (e.g. built on `main` at or after `v0.4-execution-baseline`).

## Cadence

- **Through `v0.4-execution-baseline`:** documentation, domain, and governed execution first.
- **From `v0.5-release-baseline` onward:** every significant release or recovery change SHOULD update this policy or `OPERATIONAL-RECOVERY.md` when behavior changes — not only code.

## References

- `docs/features/domain-map.md` — version chain summary
- `docs/governance/BRANCH-POLICY.md` — merge paths, hotfix exception, rollback table
- `docs/governance/OPERATIONAL-RECOVERY.md` — incident runbook outline
