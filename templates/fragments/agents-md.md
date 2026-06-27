# AGENTS.md Template

> Reference: `docs/principles/instruction-delivery.md`, `progressive-disclosure.md`

```markdown
## Where to find things

Read on demand when the trigger matches. Do not preload. Read indexes first, then specific files.

- `kb/index.md` — [KB map]. Read when navigating KB or unsure where content lives.
- `kb/<dir>/index.md` — [what]. Read when [trigger].

## Procedures

| Trigger | Skill |
|---------|-------|
| "[example phrase 1]", "[example phrase 2]" | `skill-name` |
| [intent keywords] | `skill-name` |

Re-invoke on every new intent.

## Default approach
[fallback]

## After [task]
- [capture]
- [commit]
```

**Navigation:** Single subordinate line under "Where to find things" — not an opening instruction that dominates the section. Do not duplicate "Read indexes first" as a standalone paragraph before the map.

**Trigger table:** Include 2-3 concrete user example phrases per skill (ask during bootstrap discovery). Capability names alone are weak routing signals.

**File references:** Never reference files that don't exist yet. Every path in the map must be created during bootstrap.

**Do not include:** "Skills in `.pi/skills/`..." lines — Pi already knows skill locations; LLMs interpret this as an ls target.

Every map entry must answer: **what** + **when**.
