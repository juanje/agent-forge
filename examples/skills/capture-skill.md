# Example: Capture Skill

> **Principles:** skill-design, memory-architecture (episodic write-once)
> **Type:** Episodic capture procedure (paraphrased from a production diagnostic agent)

## Structure

```markdown
---
name: capture-findings
description: Write investigation findings to episodic memory. Trigger after
  diagnose-failure completes or when user asks to save findings.
allowed-tools: Bash(git:*)
---

## Steps

1. Create `kb/active/YYYY-MM-DD_short-description.md` from template
2. Write diagnosis section — write-once; do not edit later
3. `git add` + `git commit` with descriptive message
4. Update kb/active/index.md with new entry (what + when trigger)

## Success criteria

- File exists in kb/active/ with dated filename
- Index entry added
- Committed to git
```

## Episodic rules

- **Write-once** — later updates = append new `## Follow-up` section, not rewrite
- **Close** — `git mv kb/active/... kb/history/incidents/` (permissions must allow this pattern)

## permissions.json pairing

```json
"allow": ["git mv kb/active/* kb/history/*"]
```

*Paired-update rule — skill allowed-tools must match permissions.*
