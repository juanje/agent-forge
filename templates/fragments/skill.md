# SKILL.md Template

> Reference: `docs/principles/skill-design.md`

```markdown
---
name: skill-name
description: [What it does]. Trigger when [phrases/conditions].
---

## When to use

- "[example phrase 1]", "[example phrase 2]"
- [keyword triggers]

## Tools available

| Command | What it does | Key options |
|---------|-------------|-------------|
| `bin/tool-name` | [purpose] | [preferred flag] (preferred); [fallback] (fallback) |

Do not run --help, ls bin/, or read tool source — use this table directly.

## Steps

### Step 0: Parse input

Extract [parameters] from the user's message:

| User says | Action |
|-----------|--------|
| [example] | [extraction rule] |

### Step 1: [First action with bin/tool call embedded]
...

### Step N: [Report format]

## Success criteria
- [Done condition 1]

## Gotchas
- [Domain-specific pitfalls]

## Checklist
> Include for skills with 5+ steps. Compressed step mirror exploits
> recency bias — model sees this summary right before acting.
> Remove this section for short skills (under 5 steps).

Complete each step in order:
- [ ] Step 0: Input parsed
- [ ] Step 1: [compressed description]
- [ ] Step N: [compressed description]
```

**Mandatory patterns:**

- **Step 0 (parse input)** — Every skill starts with explicit input extraction from the user message. Without it, LLMs drift into orientation behavior.
- **Tool signature table inline** — Preferred + fallback modes; explicit negatives ("do not --help"). Prevents discovery loops.
- **No informational preamble** — No Architecture, Design, or Context sections before Steps. All pre-step content must be actionable reference (When to use, Tools available).
- **When to use** — Concrete user phrases replace abstract "Trigger" section. Overlap with description is fine (routing signal).
- **Target ≤6 steps** — Consolidate if more; split into multiple skills if a procedure exceeds ~150 lines.
- **Multi-phase skills** — Specify KB read timing explicitly: defer KB reads to synthesis phase, not at start. Example: "Do not read kb/reference/ during Phase 1–2; read at synthesis (Step N)."

**Quality check:** When to use with example phrases, Step 0 parse table, tool table inline, numbered steps, success criteria, allowed-tools ↔ permissions.json, checklist if 5+ steps.
