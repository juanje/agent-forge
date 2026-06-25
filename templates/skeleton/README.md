# {{AGENT_NAME}}

{{ONE_LINE_DESCRIPTION}}

## Quick start

```bash
cp .env.example .env   # set API credentials
chmod +x bin/*
uv sync

# Start a session with your preferred harness
# See docs/glossary.md for harness-specific instructions
```

## Structure

- Identity file — Who the agent is (system prompt)
- `AGENTS.md` — Operations map and procedure triggers
- Skills directory — Procedures loaded on trigger match
- `bin/` + `tools/` — Agent-facing CLI tools (JSON output)
- `kb/` — File-based knowledge (four-store architecture)

## Phase roadmap

| Phase | Add |
|-------|-----|
| 1 (now) | Primary skill + tool + reference KB |
| 2 | capture skill, kb/history/ |
| 3 | consolidate skill, known-issues/, compute-stats |
| 4 | Secondary skills, verify-close |

See Agent Forge `docs/decision-guide.md` for details.
