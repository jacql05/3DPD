# Local pre-commit hook (reference)

This repository’s **authoritative** contract for non-interactive behavior is in `BRANCH-POLICY.md` — *Local pre-commit (non-interactive safe mode)*.

## Where the hook lives

The global hook used on this machine is typically:

```text
~/.githooks/pre-commit
```

It is **not** committed inside 3DPD; changes are operator-local. This document records **policy alignment** between 3DPD and that hook so audits know what “green local gates” mean.

## Change log (operator)

| Hook version | Note |
| --- | --- |
| v1.6 | **tests/** paths no longer trigger the interactive “HIGH-RISK / type CONFIRM” gate. Ordinary pytest/unit files should not force `git commit --no-verify`. SSOT, `apps/worker/`, `apps/api/`, and `scripts/` still trigger the gate. |
| v1.5 | Non-interactive safe mode (`CI`, `GIT_PRE_COMMIT_NONINTERACTIVE`, non-TTY stdin). |

## When you still need env ACK (safe mode)

See `BRANCH-POLICY.md`: `GIT_PRE_COMMIT_ACK_HIGH_RISK`, `GIT_PRE_COMMIT_ACK_SSOT`, `GIT_PRE_COMMIT_ACK_LARGE`, `GIT_PRE_COMMIT_ALLOW_MAIN` (main only).

## Rationale

`tests/` churn is high-volume and low-blast-radius compared to SSOT or worker deploy paths. Treating every test edit as “critical confirm” trains contributors to bypass hooks entirely, which **voids** governance.
