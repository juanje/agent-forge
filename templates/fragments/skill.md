# SKILL.md Template

> Reference: `docs/principles/skill-design.md`

```markdown
---
name: skill-name
description: [What it does]. Trigger when [phrases/conditions].
---

## Trigger
[When to invoke — overlap with description for routing]

## Steps
1. [Action with bin/tool call embedded]
2. [Disconfirmation gate if diagnostic]
N. [Report format]

## Success criteria
- [Done condition 1]

## Gotchas
- [Domain-specific pitfalls]

## Checklist
> Include for skills with 5+ steps. Compressed step mirror exploits
> recency bias — model sees this summary right before acting.
> Remove this section for short skills (under 5 steps).

Complete each step in order:
- [ ] Step 1: [compressed description]
- [ ] Step N: [compressed description]
```

**Quality check:** trigger, numbered steps, tool calls in steps, success criteria, allowed-tools ↔ permissions.json, checklist if 5+ steps.
