# Operational recovery (runbook outline)

This document is the **operational** companion to `RELEASE-POLICY.md` (release / rollback / hotfix) and `BRANCH-POLICY.md` (merge paths). It describes **what to do during and after** an incident so recovery is repeatable, not heroic.

## When to use

- Customer-visible outage, data integrity risk, security event, or CI/deploy pipeline broken in a way that blocks safe promotion.
- Any situation where “keep shipping features” would increase blast radius.

## During incident (stabilize)

1. **Assign incident lead** (single DRI) and communication channel (war room / thread).
2. **Pin truth**: note exact `main` SHA, GitHub Actions run ids, and any app semver tag in production.
3. **Stop bleeding**: if deploy is bad, **tag rollback** or redeploy last known-good artifact per `RELEASE-POLICY.md` — *Rollback ladder*.
4. **Freeze optional**: pause non-essential merges to `integration` / `main` until scope is understood (communicate in PR template or status page).

## Evidence and audit

- Preserve logs, failing workflow links, and config snapshots **before** retry loops overwrite evidence.
- If Compliance or Legal is implicated, loop **Compliance + Legal** domain owner per `domain-compliance-legal.md`.

## After incident (recover)

1. **Root cause note** (internal): timeline, trigger, contributing factors — not necessarily public.
2. **Engineering PRs**: forward-fix on `feature/*` → `domain/*` → `integration` → `main` per `BRANCH-POLICY.md`; **hotfix** only when the exception criteria there are met.
3. **Reconcile long-lived branches**: merge or document drift between `main` and affected `domain/*` so the next promotion chain is not “surprise divergence.”
4. **Close the loop**: update specs if authority changed (`AUTHORITY-PROMOTION.md`).

## References

- `docs/governance/RELEASE-POLICY.md` — release train, rollback ladder, hotfix path
- `docs/governance/BRANCH-POLICY.md` — branch hierarchy, merge rules, rollback table
