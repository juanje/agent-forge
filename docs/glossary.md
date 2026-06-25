# Glossary

Generic terms used in the principle docs and how they map to specific harnesses.

## Core components

| Term | What it is | Pi | Claude Code | Cursor |
|------|-----------|-----|-------------|--------|
| **Identity** | Who the agent is — character traits, domain baseline, hard limits. Lives in the highest-reliability channel (system prompt). | `.pi/SYSTEM.md` | Top of `CLAUDE.md` or dedicated identity section | Top of `AGENTS.md` or `.cursor/rules/` |
| **Operations guide** | Where to find things, procedure triggers, default approach. Loaded on demand. | `AGENTS.md` (also reads `CLAUDE.md`) | `CLAUDE.md` (operations sections) | `AGENTS.md` (also reads `CLAUDE.md`) |
| **Skill / procedure** | Step-by-step workflow with trigger, numbered steps, success criteria. Loaded when trigger matches. | `.pi/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` | `.cursor/skills/<name>/SKILL.md` or `.cursor/commands/<name>.md` |
| **Knowledge base (KB)** | File-based domain knowledge organized in stores. Navigated via indexes. | `kb/` directory tree | Any directory tree with `index.md` | Any directory tree with `index.md` |
| **Permission system** | Deny-by-default rules that control what the agent can read, write, and execute. | `.pi/permissions.json` + `pi-permission-gate` | `.claude/settings.json` `permissions` | `.cursor/rules/` rule files |
| **Tool / wrapper** | Shell script or thin launcher that delegates to the real implementation. Agent calls the wrapper; wrapper handles auth, retry, JSON output. | `bin/<name>` → `tools/<name>.py` | `bin/<name>` or direct script | `bin/<name>` or direct script |
| **Hook / session start** | Code that runs automatically at session start to inject context. ~100% compliance vs ~70% for "read this file first." | Extensions in `.pi/extensions/` | `.claude/hooks/` scripts | `.cursor/hooks/` scripts |

## Memory stores

| Term | What it is | Typical path |
|------|-----------|-------------|
| **Read-only reference** | Developer-maintained domain docs. Agent reads but never writes. | `kb/<domain>/` |
| **Episodic active** | Current work-in-progress records. Agent writes once, appends follow-ups. | `kb/active/` |
| **Episodic history** | Closed records. Immutable after close (moved from active). | `kb/history/` |
| **Semantic knowledge** | Patterns and lessons learned. Written only during consolidation, not mid-task. | `kb/known-issues/`, `kb/lessons/` |
| **Computed** | Statistics derived by scripts. Never LLM-computed. | `kb/history/stats.md` or similar |

## Other terms

| Term | Meaning |
|------|---------|
| **Progressive disclosure** | Three-layer context model: (1) always visible identity + navigation, (2) on-demand skills + active context, (3) deep KB via index navigation. |
| **Disconfirmation gate** | Skill step that forces the agent to seek evidence AGAINST its current hypothesis before reporting. Prevents premature known-issue matching. |
| **Skill-permission parity** | Tool access declared in skills must match what the permission system actually allows. Both must be updated together. |
| **Completion checklist** | Compressed mirror of skill steps at the end of complex skills (5+). Exploits recency bias to re-activate step awareness. |
| **Character trait** | A behavioral value in identity that the agent uses to derive behavior in novel situations. "Verify-first" is a trait; "always run validation step 3" is a rule. |
| **Four-store model** | Memory architecture separating knowledge by who writes and drift risk: read-only, episodic, semantic, computed. |
