# {{AGENT_NAME}} — Operations Guide

## Where to find things

Read on demand when the trigger matches. Do not preload.
Read indexes first, then specific files.

- `kb/reference/index.md` — {{REFERENCE_DESCRIPTION}}. Read when {{REFERENCE_TRIGGER}}.
- `kb/active/index.md` — Open work-in-progress records. Read when resuming an investigation or checking WIP.
- `kb/observations.md` — Candidate learnings scratch pad. Append during work; consolidate later.

## Procedures

Skills in `.pi/skills/` (or `.cursor/skills/` / `.claude/skills` on Claude Code/Cursor).
Loaded on trigger match.

| Trigger | Skill |
|---------|-------|
| {{TRIGGER_1}} | `{{PRIMARY_SKILL_NAME}}` |

Re-invoke on every new intent. Do not improvise when a skill exists.

## Default approach

When no trigger matches, ask clarifying questions about the domain task.
Do not execute destructive or write operations without an explicit skill.

## After completing a task

- Capture findings to kb/active/ if the skill requires it
- Commit changes with a descriptive message
