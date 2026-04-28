# GitHub branch protection (P0.5)

This checklist aligns the hosted repo with `docs/governance/BRANCH-POLICY.md`. Apply in **GitHub → Settings → Branches → Branch protection rules**.

## `main` (required)

- [ ] **Require a pull request before merging**
  - Required approvals: **≥ 1** (or org default); use **≥ 2** for regulated environments.
- [ ] **Dismiss stale pull request approvals** when new commits are pushed (recommended).
- [ ] **Require status checks to pass** before merging  
  - Add check: **`governance-sanity`** (from workflow `governance-ci.yml`).
- [ ] **Require branches to be up to date before merging** (recommended).
- [ ] **Do not allow bypassing the above settings** (admins included), unless org policy forces an exception.
- [ ] **Restrict who can push to matching branches** to maintainers only (no direct pushes for day-to-day work).

## `integration` (recommended)

Match `main` or **stricter** if `integration` is used as a soak line. If unused, still protect from accidental force-push.

## `domain/*` and `feature/*` (optional)

Many teams leave these unprotected and rely on PRs into `integration` / `main`. Minimum: **block force-push** on `domain/*` if shared.

## CLI reference (optional)

With admin token and `gh` CLI, rules can be scripted via `gh api repos/{owner}/{repo}/branches/main/protection` (see GitHub REST docs). Prefer UI until the team agrees on exact JSON payload.

## CI ↔ pre-commit

Workflow **governance-ci** sets `CI: true` and `GIT_PRE_COMMIT_NONINTERACTIVE: "1"` so any future job that invokes the same hook logic behaves like local **safe mode**. Local developers should prefer a real terminal for full interactive prompts; see `BRANCH-POLICY.md` — *Local pre-commit*.
