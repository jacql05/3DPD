# Friction log

**Purpose:** Record where delivery **stuck**, where automation **mis-fired**, where rules felt **too heavy**, where **reviewers** (human or CI) were too blunt, where **hooks** annoyed without payoff, and where **promotion** (branch → PR → merge) was **unclean**. Use this to tune governance without losing intent.

**How to add an entry:** Append a dated block under the right heading. Start each example with a dated heading, e.g. `### YYYY-MM-DD — Short title`. Prefer this shape under that heading:

- **Problem:** What happened (observable).
- **Impact:** Time lost, merge blocked, wrong signal, etc.
- **Fix / mitigation:** What we changed or should change (doc, workflow, ruleset, habit).

---

## Required checks and branch protection (name mismatch)

### 2026-04-29 — Check name mismatch → merge appears blocked

- **Problem:** Branch protection or rulesets referenced a **status check name** that did not match what GitHub Actions actually reported (e.g. workflow filename vs **job** `name`, or shorthand vs full check string). Symptom: required check stuck **pending / expected** while CI was already green under a *different* label.
- **Impact:** PR merge blocked until the ruleset was corrected; looked like “CI failed” when the real issue was **label alignment**.
- **Fix:** In rulesets / branch protection, require checks using the **exact** names shown on the PR **Checks** tab. For this repo (as of the friction event):

  | Workflow file        | Job `name` (GitHub check)   |
  | -------------------- | --------------------------- |
  | `tests.yml`          | **pytest**                  |
  | `reviewer-ci.yml`    | **reviewer-deterministic**  |
  | `governance-ci.yml`  | **governance-sanity**       |

  Treat “`tests` / `pytest`”, “`reviewer-ci` / `reviewer-deterministic`”, “`governance-ci` / `governance-sanity`” as **workflow vs job** pairs: protection must target the **job** name as displayed.

---

## Unresolved review threads (not “approvals”)

- **Problem:** GitHub blocked merge with **“A conversation must be resolved before this pull request can be merged”** while approvals were satisfied. Open threads were **Copilot** or inline review comments left unresolved.
- **Impact:** Maintainer time spent on the wrong knob (e.g. lowering required approvals) when the real blocker was **Resolve conversation**.
- **Fix:** Before changing approval count: on **Files changed**, resolve or substantively reply-then-resolve stale threads. Optionally resolve via API when threads are outdated but still open.

---

## Reviewer-deterministic (CI) limits

- **Problem:** `reviewer-ci` is **grep-level** by design: it cannot judge whether a `docs/features/*.md` reference is the *right* spec for the change.
- **Impact:** False sense of security if bodies are boilerplate; rare false negatives if formatting breaks the regex.
- **Fix:** Keep bodies honest; Gatekeeper enforces meaning. Extend CI only with **still-deterministic** rules (documented in `REVIEWER-GATEKEEPER.md`).

---

## Draft PRs vs checks

- **Problem:** `reviewer-deterministic` skips **draft** PRs; leaving a promotion PR in draft meant reviewer did not run when expected.
- **Impact:** Surprise after marking ready; or missing signal while iterating.
- **Fix:** Mark **Ready for review** when the PR should gate merge; document in PR template if needed.

---

## Promotion chain hygiene (integration vs `main`)

- **Problem:** `integration` and `main` both **added** the same paths (e.g. payout intake) on different histories → **add/add** conflicts on `integration` → `main` PR even when the *net* diff was small.
- **Impact:** “Dirty” merge UI; risk of dropping doc-cleanup or duplicating logic if resolved wrong.
- **Fix:** Merge **`main` into `integration`** (or rebase policy-permitted) **before** the promotion PR; resolve conflicts once on `integration` so the PR to `main` is **mergeable** and **narrow**. Prefer **squash** on feature/domain PRs to keep train readable.

---

## Local hooks and pre-commit noise

- **Problem:** Interactive or broad “high-risk path” prompts in local hooks can fire on **docs-only** or **test-only** touches when patterns are wide; cross-layer warnings on small changes add noise.
- **Impact:** Friction for trivial commits; habit to `--no-verify` (undesired).
- **Fix:** Narrow `CONFIRM` patterns; keep hook semantics documented (`PRE-COMMIT-LOCAL-HOOK.md`); use `CI=true` / non-interactive vars in automation as already aligned with `governance-ci`.

---

## Tooling / API quirks

- **Problem:** `gh pr edit` failed with GraphQL noise (e.g. classic Projects) while REST `PATCH` on the pull request succeeded.
- **Impact:** Could not update title/body from CLI until switching API.
- **Fix:** Prefer `gh api --method PATCH repos/{owner}/{repo}/pulls/{pull_number}` with `--input` JSON for reliable PR metadata updates.

---

## Case log (Stabilization Window — dated, recurrence-focused)

Use this subsection to count toward **Reviewer v2 Launch Gate — Condition B** (`reviewer-v2-launch.md`). Prefer **repeat** incidents; one-offs go under topic sections above.

### 2026-04-29 — Required check name did not match Actions job label

- **Problem:** Branch protection required a label that did not match the **job** name GitHub reported (e.g. workflow file vs `pytest` / `governance-sanity` / `reviewer-deterministic`).
- **Impact:** Merge blocked with check “expected” while another green check existed; looked like CI failure.
- **Fix:** Documented exact job names in `GITHUB-BRANCH-PROTECTION.md` and `FRICTION-LOG.md`; align rulesets to PR Checks tab strings.

### 2026-04-29 — Unresolved Copilot / review threads blocked merge (not approvals)

- **Problem:** GitHub showed **“A conversation must be resolved”** while approval rules were already satisfied.
- **Impact:** Time spent on approval count instead of resolving threads; merge still blocked.
- **Fix:** Resolve threads on **Files changed** first; use `resolveReviewThread` GraphQL when threads are stale but open.

### 2026-04-28 — `integration` vs `main` add/add conflicts on shared payout paths

- **Problem:** Same files introduced on divergent histories → merge conflict on promotion PR (`integration` → `main`).
- **Impact:** Risk of dropping doc cleanup or duplicating logic; noisy merge UI.
- **Fix:** Merge `main` into `integration` before promotion; resolve once on `integration`; keep net diff domain-scoped.

### 2026-04-28 — Copilot flagged PR scope vs promotion intent (payments-tax train)

- **Problem:** Promotion PR diff history touched multiple domains while title claimed a narrow payments-tax promotion.
- **Impact:** Reviewer ambiguity; repeated scope discussion on same promotion class.
- **Fix:** Narrow diff via merge hygiene; update PR title/body to match files actually changed; track for future **scope drift** rule.

### 2026-04-29 — `gh pr edit` failed; REST `PATCH` on pull request worked

- **Problem:** `gh pr edit` returned GraphQL error path involving classic Projects.
- **Impact:** Could not update PR title/body from CLI with the obvious command.
- **Fix:** Use `gh api --method PATCH repos/{owner}/{repo}/pulls/{pull_number}` with JSON body file.

### 2026-04-29 — Draft PR skipped `reviewer-deterministic` until marked ready

- **Problem:** Workflow skips draft PRs; checks did not run when authors expected.
- **Impact:** False sense that reviewer passed; late surprise after “Ready for review”.
- **Fix:** Mark ready when merge-bound; document in PR checklist.

### 2026-04-28 — Maintainer tuned approvals (1→0) before checking conversations

- **Problem:** Merge still blocked by unresolved conversations after temporary approval relaxation.
- **Impact:** Wrong lever pulled; policy exception used without removing the real blocker.
- **Fix:** Document order: **resolve conversations →** then approvals if still required.

### 2026-04-28 — `reviewer-ci` PR body contract vs `docs/*` head exemption

- **Problem:** Confusion whether governance PRs to `main` must carry `Domain/Spec/Baseline` in body.
- **Impact:** Risk of failing a docs-only PR or omitting contract on feature PRs.
- **Fix:** Recorded skip rules in `REVIEWER-GATEKEEPER.md` (`docs/*`, `hotfix/*`).

### 2026-04-29 — Multiple stripe-related keys duplicated the same error string

- **Problem:** Loop appended the same stripe rejection message once per matching key.
- **Impact:** Noisy, unstable error list for validators and tests.
- **Fix:** Single flag / single append for stripe class; regression test for multiple keys.

### 2026-04-28 — `feature/*` → `main` intent vs reviewer deterministic gate

- **Problem:** Direct feature→main violates ladder; must be caught before merge.
- **Impact:** Would bypass domain/integration soak.
- **Fix:** `reviewer-ci` fails when `base_ref == main` and `head_ref` matches `feature/*`.

### 2026-04-29 — FRICTION-LOG template said “dated” but first example lacked date in heading

- **Problem:** “Append dated block” guidance did not match the first example heading format.
- **Impact:** Copilot / human confusion about required format for Condition B counting.
- **Fix:** Renamed example to `### YYYY-MM-DD — …` and documented pattern in “How to add an entry”.

### 2026-04-29 — Launch Gate doc added before friction count reached 10+

- **Problem:** `reviewer-v2-launch.md` requires **10+** friction cases; log had fewer discrete dated rows.
- **Impact:** Condition B formally unmet; risk of starting v2 too early.
- **Fix:** This case log section expands dated entries; keep appending as incidents recur.

---

## Where rules felt “too heavy”

*(Append examples here: e.g. required two reviewers on a single-maintainer org, strict base-branch rules without documented exception path.)*

---

## Where promotion was “not clean”

*(Append examples here: e.g. mixed-domain diff in one PR title, or `feature/*` → `main` attempts.)*

---

## References

- `BRANCH-POLICY.md` — merge ladder  
- `REVIEWER-GATEKEEPER.md` — Reviewer vs Gatekeeper, skip rules  
- `GITHUB-BRANCH-PROTECTION.md` — check names and protection alignment  
- `reviewer-v2-launch.md` — when L4 Reviewer v2 is allowed (launch gate)  
