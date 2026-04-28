# Reviewer and Gatekeeper (L4)

**Reviewer** = automated, **deterministic** checks (CI). **Gatekeeper** = human approval on protected branches. This split keeps policy **executable** without pretending software replaces accountability.

## What runs today (`reviewer-ci`)

Workflow: `.github/workflows/reviewer-ci.yml` — job **`reviewer-deterministic`**.

| Check | Meaning |
| --- | --- |
| No `feature/*` → `main` | Violates merge ladder; fails the job. |
| PR body contains `Domain:`, `Spec:`, `Baseline:` | Minimum governance labels (case-insensitive). |
| Body references `docs/features/…/*.md` | CI greps the whole description; put the spec path on the `Spec:` line for human Gatekeepers. |

**No LLM** in v1. Optional AI-assisted review can be added later only if output is structured and auditable.

## When checks are skipped

For `pull_request` events where the **head** branch starts with:

- `docs/` — documentation-only work; **body contract not enforced** by `reviewer-ci` (still use clear titles; Gatekeeper applies). Add `Baseline:` when changing authority docs.
- `hotfix/` — emergency path; body contract **not enforced** here (hotfix PR must still satisfy `BRANCH-POLICY.md` manually).

Fork PRs from outside this repo are skipped (`head.repo` must match) to avoid missing secrets/context.

## Gatekeeper (human)

- **GitHub**: Required approvals on `main` (and optionally `integration` / `domain/*`) per org settings.
- **Single-maintainer exceptions** must follow `BRANCH-POLICY.md` / `RELEASE-POLICY.md` audit language.

## Roadmap (not implemented yet)

- Structured LLM output consumed by a **second** deterministic step (two-stage Reviewer).
- CODEOWNERS mapping domain → reviewer pool.
- Required status: add **`reviewer-deterministic`** to branch protection after this workflow has run clean on `main` for a soak period.

## References

- `AGENT-WORKFLOW.md` — L4 role definitions
- `TASK-ROUTING.md` — branch / PR routing
- `BRANCH-POLICY.md` — merge ladder and hotfix rules
