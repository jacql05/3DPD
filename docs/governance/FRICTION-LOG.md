# Friction log

**Purpose:** Record where delivery **stuck**, where automation **mis-fired**, where rules felt **too heavy**, where **reviewers** (human or CI) were too blunt, where **hooks** annoyed without payoff, and where **promotion** (branch → PR → merge) was **unclean**. Use this to tune governance without losing intent.

**How to add an entry:** Append a dated block under the right heading. Prefer this shape:

- **Problem:** What happened (observable).
- **Impact:** Time lost, merge blocked, wrong signal, etc.
- **Fix / mitigation:** What we changed or should change (doc, workflow, ruleset, habit).

---

## Required checks and branch protection (name mismatch)

### Example: check name mismatch → merge appears blocked

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
- **Fix:** Prefer `gh api --method PATCH repos/{owner}/{repo}/pulls/{number}` with `--input` JSON for reliable PR metadata updates.

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
