# Agent workflow

This file defines how agents and humans coordinate work in this repository: **roles**, **steps**, **gates**, and **required artifacts**. It aligns with `BRANCH-POLICY.md`, `TASK-ROUTING.md`, and `REVIEWER-GATEKEEPER.md`.

## L4 roles (first version)

These names describe **accountability**, not chat personas. Each role maps to **branch choice**, **PR authorship**, **CI checks**, and **human approval** (Gatekeeper).

| Role | Responsibility | Typical branch / artifact | Automated gate |
| --- | --- | --- | --- |
| **Planner** | Break work into verifiable slices; name domain + spec + baseline. | Issue or design note linked from PR body | — (human or agent produces PR description) |
| **Builder** | Implement minimal scoped change; open PR toward correct base. | `feature/<domain>/<name>` | `tests`, `governance-sanity` |
| **Tester** | Add/adjust tests; keep CI green. | Same feature branch (may be same actor as Builder) | `tests` |
| **Reviewer** | **Deterministic** policy checks on the PR (this repo: `reviewer-ci`). | GitHub Check `reviewer-deterministic` | `reviewer-ci.yml` |
| **Gatekeeper** | Approve merge per `BRANCH-POLICY` (human); owns risk acceptance. | GitHub **Required approvals** on protected branches | Not automatable |

**Rule:** Reviewer (CI) **recommends / blocks by policy**. Gatekeeper **approves**. No workflow replaces required human review on `main` unless governance explicitly changes.

## Default sequence (feature work)

1. **Planner** confirms: domain slug, spec path under `docs/features/`, baseline tag (e.g. `v0.5-release-baseline`).
2. **Builder** implements on `feature/<domain>/<name>`; **Tester** keeps `pytest` green.
3. Open PR **feature → domain**; CI runs `governance-sanity`, `tests`, `reviewer-deterministic` (when enabled on repo).
4. After domain / integration / `main` promotions, **Gatekeeper** merges per branch protection.

## Out of scope (for this document)

- LLM-as-reviewer prompts or model calls — **not** in v1; see `REVIEWER-GATEKEEPER.md` roadmap.
