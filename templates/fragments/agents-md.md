# AGENTS.md Template

> Reference: `docs/principles/instruction-delivery.md`, `progressive-disclosure.md`

```markdown
## Where to find things

Read on demand when trigger matches. Read indexes first.

- `kb/<dir>/index.md` — [what]. Read when [trigger].

## Procedures

| Trigger | Skill |
|---------|-------|
| [intent] | `skill-name` |

Re-invoke on every new intent.

## Default approach
[fallback]

## After [task]
- [capture]
- [commit]
```

Every map entry must answer: **what** + **when**.
