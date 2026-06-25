# Instruction Delivery

## Core Concept

Effectiveness depends on **delivery mechanism**, not just content quality. Important content in an unreliable channel = silent failure. Match content type to the channel with the right reliability for that content.

**Instruction budget:** Frontier models follow ~150–200 instructions consistently. Coding harnesses consume ~50 before your content loads. Each added instruction degrades **all** instructions uniformly — not just the new one.

## Design Rules

1. **System prompt / identity** — Character, domain baseline, hard limits. Always present; survives context compaction. Highest reliability.

2. **Injected context (hooks, session start)** — Mandatory init, current state, safety criteria. ~100% compliance vs ~70% for "read this file first."

3. **Operations guide** — Knowledge base map with triggers, procedure table, default approach, post-task steps. On-demand; agent consults when needed.

4. **Skills / procedures** — Step-by-step workflows. Loaded on trigger. Medium reliability (depends on trigger matching).

5. **Referenced files** — Supplementary knowledge base. Low reliability unless a skill step directs the read.

6. **Tool output** — Highest reliability **for that turn**. Pre-digested decisions, skip signals, truncation headers.

7. **Actionable format** — Every instruction answers: what to do, when, and why. "Read when user asks about X" not "contains information about X."

8. **Lean agent references** — `path — description. Read when trigger.` Full markdown links only for human-facing URLs.

9. **One entry point where possible** — Some harnesses load multiple config files; avoid duplicate or conflicting instructions across them.

10. **No instructions in HTML comments** — Two failure modes: (1) some harnesses strip `<!-- -->` from auto-injected files. (2) Models ignore or deprioritize comment content even when preserved. Use visible markdown for all agent-facing guidance.

## Evaluation Criteria

### Identity / system prompt

- [ ] Identity and character only (no KB maps, no trigger tables)
- [ ] Turn-critical behavioral rules in Character, not buried in operations file
- [ ] Under ~500 lines for Layer 1 total (identity + operations map if always loaded)

### Operations guide

- [ ] "Where to find things" uses trigger-based entries (what + when)
- [ ] Procedure trigger table maps intents to skills
- [ ] "Re-invoke on every new intent" stated
- [ ] Default approach when no trigger matches
- [ ] Post-task capture/commit steps where applicable
- [ ] Operational lines change agent behavior (not descriptive filler)

### Cross-file

- [ ] No duplicate instructions across identity and operations
- [ ] Skills referenced in operations exist in skills directory
- [ ] Critical init uses hooks or auto-loading where harness supports it

## Good Examples

```markdown
## Where to find things

Read on demand when trigger matches. Read indexes first, then specific files.

- `kb/known-issues/index.md` — Recurring failure patterns. Read when a failure looks familiar.
- `kb/active/index.md` — Open investigations. Read when resuming work or checking WIP.

## Procedures

| Trigger | Skill |
|---------|-------|
| Failure investigation, URL/ID provided | `diagnose` |
| Status overview, "is it healthy?" | `check-status` |

Re-invoke on every new intent. Do not improvise when a skill exists.
```

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| `kb/errors/` listed in operations guide as "contains error documentation" | Agent doesn't know WHEN to read it; descriptive, not operational | `kb/errors/index.md` — Error classification reference. **Read when** a job fails and you need to classify the error type. |
| "Always verify before reporting" in both identity AND operations guide | Duplicated across channels wastes tokens; if they diverge, agent gets conflicting signals | Keep in identity (Character trait) only; remove from operations guide |
| Single 200-line config file with character traits + KB map + procedure table + examples | Everything in one file = everything at medium priority; identity traits compete with navigation for attention | Split: identity file (~40 lines, highest-reliability) + operations file (map + procedures, on-demand) |
| "You should check the knowledge base if you think it might help" | Vague; agent decides whether to read = unreliable | Trigger table maps intent → skill; skill step 3 says "Read `kb/errors/index.md`" — mandatory, not suggested |
