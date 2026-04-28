# Branch Policy

This document is authoritative for branch naming, merge paths, review expectations, and rollback posture for the 3DPD repository. It implements the domain model in `docs/features/domain-map.md` and must stay consistent with `docs/governance/AUTHORITY-PROMOTION.md` when changed.

## Branch hierarchy

```text
main                 # protected; releasable truth; tagged baselines
integration          # optional integration line; pre-release soak
domain/<slug>        # long-lived per domain; aligns to docs/features/domain-<slug>.md
feature/<slug>/<name> # short-lived; must map to exactly one domain slug
hotfix/<slug>        # emergency production fixes; exceptional path only
```

**Naming:** `<slug>` MUST match a row in `docs/features/domain-map.md`. Feature branches use `feature/<domain-slug>/<feature-name>` (kebab-case `feature-name`).

## Merge rules (required)

Allowed merge flow:

```text
feature/<domain-slug>/...  →  domain/<domain-slug>
domain/<slug>            →  integration
integration              →  main
```

**Forbidden (without explicit governance exception documented in the PR):**

```text
feature/*  →  main
domain/*   →  main   # except hotfix policy below
```

**Hotfix exception:** `hotfix/*` MAY open a PR directly to `main` only when all of the following hold:

1. Production or legal exposure requires immediate repair.
2. PR description states severity, blast radius, and owner.
3. Within one business day (or sooner if release policy says so), `main` is either merged back into affected `domain/*` branches or a follow-up PR records the reconciliation plan.

**Docs-only policy:** Governance or domain-spec corrections that do not change runtime code MAY use `docs/*` branches with PR to `main` when they only touch `docs/**` and are classified as authority updates per `AUTHORITY-PROMOTION.md`. They MUST NOT introduce application code paths under `apps/` in the same PR.

## Review and approval

Rules are **defaults** until overridden in writing by org governance (e.g. CODEOWNERS on GitHub).

| PR type | Target branch | Who may approve |
| --- | --- | --- |
| Feature | `domain/<slug>` | Domain owner (see domain spec **Owner → Accountable**) plus one additional reviewer with commit rights. |
| Domain integration | `integration` | At least one maintainer plus domain owner for any domain touched by the batch. |
| Release / promotion | `main` | Maintainer(s) per org list; compliance or legal reviewer when PR touches `docs/compliance/**`, payments, or identity verification semantics. |
| Hotfix | `main` | Two approvers where org policy requires dual control; otherwise one maintainer plus post-merge audit note. |
| Docs / authority only | `main` | As defined in `AUTHORITY-PROMOTION.md` (typically accountable role for that doc). |

**Enforcement:** Teams SHOULD use branch protection on `main` (required reviews, required status checks). `integration` SHOULD match `main`’s rules or stricter if it is used.

## Rollback rules

| Situation | Preferred action |
| --- | --- |
| Bad merge on `integration` or `domain/*` | **Revert** the merge commit on that branch; do not rewrite public history. |
| Production defect on a tagged release | **Hotfix** branch → `main`; tag new patch version per `RELEASE-POLICY.md`. |
| Need to restore a known-good system state | **Tag rollback**: deploy or reference the previous release tag (e.g. `v0.2-domain-baseline` or app semver), then forward-fix; document in incident log. |
| Authority / spec was wrong, code was right | Fix **docs** through `AUTHORITY-PROMOTION.md`; avoid “silent” spec edits. |

**Never** force-push to `main` to “fix” history unless executive + compliance exception exists and mirrors are coordinated.

## Feature admission (iron rule)

A feature MUST NOT enter development until it can answer:

1. **Which domain?** — Maps to exactly one `domain/<slug>` and `docs/features/domain-<slug>.md`.
2. **Which spec?** — Cites the relevant sections of that domain spec (or linked feature spec under authority).
3. **Which baseline?** — States the tag or `main` commit it is built on (e.g. `v0.2-domain-baseline` or later).

If any answer is missing, the work item stays in design / routing until `TASK-ROUTING.md` and domain owners close the gap.

## Local pre-commit (non-interactive safe mode)

Global or repo hooks MUST NOT require a TTY for routine commits, or agents and CI will train contributors to use `--no-verify`, which **voids** the gate system.

**Contract for this org’s hook:**

- If the hook cannot prompt (non-interactive / no usable TTY), it runs in **safe mode**: print diff and impact summary, then apply automatic rules below—**no** interactive `yes` / `CONFIRM` prompts.
- **Commits to `main` in safe mode** are blocked unless `GIT_PRE_COMMIT_ALLOW_MAIN=1` is set intentionally for documented automation.
- **High-risk paths** (`docs/SSOT/`, `apps/worker/`, `apps/api/`, `scripts/` as defined in the global hook — **not** ordinary `tests/`-only commits): blocked in safe mode unless `GIT_PRE_COMMIT_ACK_HIGH_RISK=1`. See `docs/governance/PRE-COMMIT-LOCAL-HOOK.md` for hook version alignment.
- **SSOT changes:** blocked in safe mode unless `GIT_PRE_COMMIT_ACK_SSOT=1` and commit message includes required justification lines per SSOT policy.
- **Large diffs** (hook threshold): blocked in safe mode unless `GIT_PRE_COMMIT_ACK_LARGE=1`.

To **force** interactive prompts when stdin is not a TTY (e.g. advanced terminal tooling), set `GIT_PRE_COMMIT_FORCE_INTERACTIVE=1` only in environments where `/dev/tty` works.

Contributors SHOULD run `git commit` from a normal terminal when possible so full interactive checks apply. They MUST NOT habitually use `--no-verify` except when bypass is explicitly approved for a one-off emergency, with a follow-up ticket to restore gates.

## References

- `docs/features/domain-map.md` — slugs and evolution rule
- `docs/governance/RELEASE-POLICY.md` — tags, release train, rollback ladder, hotfix path
- `docs/governance/OPERATIONAL-RECOVERY.md` — incident runbook outline
- `docs/governance/AUTHORITY-PROMOTION.md` — promoting or changing authoritative docs
