# L4 Reviewer v2 — Launch gate

**Reviewer v2** is not started by declaring “begin work.” It starts only when this **Launch Gate** says so. Until then: **no** `reviewer-v2` implementation work; collect **evidence**, define **deterministic** rules, then code.

---

## 1. Allowed vs forbidden

| Situation | Verdict |
| --- | --- |
| All **Launch conditions** (A **and** B **and** C) are satisfied **and** a **Trigger Evidence** pack is filed under Section 2 | **Allowed** to implement v2 automation behind new checks/workflows. |
| Any condition missing, or evidence is anecdotal / one-off | **Forbidden** to add LLM-backed merge gates or new “smart” required checks. |
| Someone wants to “try the model” without a written deterministic shell | **Forbidden** — that is not v2, it is **unsafe**. |

---

## 2. Launch conditions (must **all** be true)

### Condition A — 5+ stable promotion chains

**Definition:** At least **five** distinct domains (or equivalent product slices) have completed the full ladder **more than once or under sustained use**, not a single lucky merge:

```text
feature/* → domain/* → integration → main
```

**Stable** means: repeated promotions, governance CI + tests + deterministic reviewer green, no chronic revert/repair cycles for the same breakage.

**Current inventory (example baseline for this repo):** three completed trains (e.g. identity-verification, compliance-legal, payments-tax) → **does not yet satisfy** Condition A. **Do not** start v2 until the count and stability bar are met.

---

### Condition B — 10+ real friction cases in `FRICTION-LOG.md`

**Definition:** At least **ten** entries that document **real** merge or delivery pain:

- actually blocked a merge, or  
- burned maintainer time in a measurable way, or  
- produced a **false signal** (green CI / wrong check / wrong approval story).

Subjective annoyance (“feels slow”) **does not** count unless tied to an observable outcome.

**Where:** `docs/governance/FRICTION-LOG.md` (append dated blocks per that file’s template).

**Current state:** treat as **below 10** until the log explicitly contains ten qualifying entries. Condition B is **not** met until then.

---

### Condition C — Repeated failure pattern (≥ 3 occurrences)

**Definition:** The **same** failure class has happened **three or more times** (e.g. check name mismatch, PR scope drift vs title/body, unresolved review threads blocking merge). **One-off** incidents do **not** qualify for automation priority.

**Why:** v2 adds **process surface area**; it must pay rent by preventing recurrence, not by encoding luck.

---

## 3. How to officially launch (order is mandatory)

```text
evidence → rule → deterministic condition → then implementation
```

**Never** reverse this (e.g. writing `reviewer-v2.py` first is the common failure mode).

### Section 3.1 — Trigger evidence (required document section)

When conditions A–C are met, add a subsection to this file (or to the PR that introduces v2) titled **Trigger evidence**, using **Problem / Impact / Evidence** (links to PRs, ruleset screenshots, commit SHAs). Example shape:

```markdown
### Trigger evidence — PR scope drift

- **Problem:** PR title/body claimed a narrow domain; diff included unrelated app paths.
- **Evidence:** PR #17, PR #21, PR #22, PR #24 (replace with real list when filing).
- **Impact:** Reviewer and Gatekeeper ambiguity; merge delay; repeated Copilot/human scope challenges.
```

Evidence must be **specific** (URLs, numbers, dates). “We felt confused” is insufficient.

---

### Section 3.2 — Why a deterministic rule is possible

For each candidate v2 rule, document:

- **Rule:** One sentence, testable without a model.  
- **Because:** What **path-, diff-, or text-based** signal makes it deterministic?

Example:

```markdown
- **Rule:** PR title `Domain:` token must match at least one changed path prefix (e.g. `payments-tax` ↔ `apps/payments_*` / agreed map).
- **Because:** File paths and PR body labels are **deterministic** inputs; a lookup table is finite and auditable.
```

If the only justification is “the LLM can judge if it feels right,” **stop** — that is **not** v2 and must not ship as a gate.

---

### Section 3.3 — Why LLM may assist only (iron law)

| LLM **may** | LLM **must never** |
| --- | --- |
| Summarize risk, surface links, suggest **non-binding** notes for humans | **Merge** decision |
| Draft text for a human to paste after edit | **Replace** required approval or Gatekeeper |
| Classify **only** when output is structured and every branch maps to a **deterministic** follow-up step | **Override** branch protection or rulesets |

**Binding gates** stay **deterministic** (grep, path rules, schema). Anything that feels like “the model said OK to merge” is **out of scope** for v2.

---

## 4. First v2 rule candidates (priority — spec only until gate opens)

These are **design priorities**, not shipped checks, until the Launch Gate is satisfied.

### Rule #1 — PR scope drift detection (**highest**)

Detect mismatch between declared scope (title/body `Domain:` / linked spec) and **changed paths** (e.g. compliance paths under a payments-only claim). Outcome can start as **annotation** or **non-required** check, then tighten after false-positive rate is known.

### Rule #2 — Domain ↔ changed path mismatch

If body contains `Domain: payments-tax` but diff touches `apps/compliance_*` (per agreed path map), emit **warning** (or fail only after human sign-off in `FRICTION-LOG`).

### Rule #3 — Spec drift hint (soft signal)

If code under `apps/payments_*` changes but no `docs/features/*.md` in the same PR, **remind** only — **not** a hard fail by default; Gatekeeper may still require a doc follow-up PR.

---

## 5. Explicit non-goals (until gate opens)

- Do **not** implement `reviewer-v2.py` (or equivalent) **before** evidence + deterministic rule text exists in repo docs.  
- Do **not** attach an LLM to **required** status checks.  
- Do **not** lower approval counts to “unstick” v2 experiments; resolve conversations and fix rulesets first (see `FRICTION-LOG.md`).

---

## 6. One-line summary

Starting Reviewer v2 is **not** “start coding.” It is **proving it deserves to exist** — with chains, friction volume, repeated patterns, and **deterministic** rule contracts.

---

## References

- `FRICTION-LOG.md` — friction volume (Condition B)  
- `REVIEWER-GATEKEEPER.md` — Reviewer vs Gatekeeper, v1 scope  
- `BRANCH-POLICY.md` — promotion ladder (Condition A)  
- `TASK-ROUTING.md` — PR body contract  
