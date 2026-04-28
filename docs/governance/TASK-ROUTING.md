# Task routing

This file defines how tasks are classified and routed to **branches**, **PR targets**, **CI**, and **approval (Gatekeeper)**. Pair with `AGENT-WORKFLOW.md` and `BRANCH-POLICY.md`.

## Routing table (summary)

| Task type | Branch to use | PR target | CI (always) | Gatekeeper |
| --- | --- | --- | --- | --- |
| Domain feature | `feature/<slug>/<name>` | `domain/<slug>` | `governance-sanity`, `tests`, `reviewer-deterministic` | Domain owner + reviewer (per `BRANCH-POLICY`) |
| Domain batch / sync | `domain/<slug>` | `integration` | same | Maintainer + domain owner for touched domains |
| Release train step | `integration` | `main` | same | Maintainer(s); stricter on `main` |
| Governance / docs only | `docs/<topic>` | `main` | `governance-sanity`, `tests` (if applicable) | Per `AUTHORITY-PROMOTION.md`; **reviewer-deterministic** skipped for `docs/*` heads (see `REVIEWER-GATEKEEPER.md`) |
| Emergency fix | `hotfix/<slug>` | `main` (exception) | `governance-sanity`, `tests`, `reviewer-deterministic` where applicable | Hotfix policy in `BRANCH-POLICY.md` |

## PR body contract (enforced by Reviewer / CI)

For heads **not** starting with `docs/` or `hotfix/`, the PR description **must** include (case-insensitive labels):

- `Domain:` …
- `Spec:` … (must reference a path under `docs/features/` ending in `.md`)
- `Baseline:` … (tag or explicit `main` + SHA per policy)

`reviewer-ci` implements the **deterministic** subset; Gatekeeper still enforces meaning.

## Forbidden shortcut

- **`feature/*` → `main`**: never route here; use domain + integration per `BRANCH-POLICY.md`.
