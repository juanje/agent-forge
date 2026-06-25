---
name: full-review
description: Comprehensive agent audit — orchestrates all review skills. Trigger when user says full review, review my agent, or audit agent repo.
---

# Full Review — Orchestrated Audit

## Trigger

User wants comprehensive review of an existing agent repository.

## Steps

### 1. Discover target structure

Ask for target path if not provided. Scan:

```
.pi/SYSTEM.md, AGENTS.md, CLAUDE.md
.pi/permissions.json, settings.json
.pi/skills/ or .cursor/skills/
bin/, tools/
kb/
```

Build component inventory table.

### 2. Run reviews via subagents

Launch each review as a **separate subagent** (Cursor Task / Claude Code agent). Do NOT run all reviews inline in the main context (WHY: subagent isolation produces more thorough per-area analysis and prevents context pressure from cutting corners on later reviews).

If the harness does not support subagents, run reviews sequentially with a full context reset between each (read principle doc fresh for each area).

| Order | Review | Target files |
|-------|--------|--------------|
| 1 | review-identity | SYSTEM.md, SOUL.md, CLAUDE.md identity |
| 2 | review-operations | AGENTS.md, CLAUDE.md operations |
| 3 | review-disclosure | kb/**/index.md, AGENTS.md map |
| 4 | review-skills | **/SKILL.md |
| 5 | review-tools | bin/, tools/ |
| 6 | review-memory | kb/ structure, capture/consolidate skills |
| 7 | review-permissions | permissions.json + skill parity |

Also consult `docs/anti-patterns.md` throughout.

### 2b. Cross-reference skills and tools (mandatory)

After completing review-skills and review-tools, cross-check. This step is **mandatory** — delegate to a dedicated subagent if available. Inline cross-reference under context pressure misses real bugs.

**Minimum depth:** verify at least 3 tool calls per skill against actual tool code (argparse/click definitions, output fields, error types).

| Check | How |
|-------|-----|
| **Flag existence** | For each `bin/tool --flag` in a skill step, verify the flag exists in the tool's argparse/click definition or `--help` |
| **Error coverage** | For each error handling block in a skill, verify the tool can actually emit that error type |
| **Output schema match** | For each field a skill parses from tool output (e.g. "extract `verdict` field"), verify the tool produces that field |
| **Mutation safety** | For tools with `--apply` / env-var gates, verify skills include dry-run review before `--apply` |

Report mismatches as: `[skill] calls [tool --flag] but tool does not support [flag]` or `[skill] handles [error] but tool emits [different error format]`.

### 3. Synthesize report

```markdown
## Full Review — [agent path]

### Executive summary
[Overall maturity: Phase 1-4 estimate, top 3 risks]

### Patterns that work well
[Strengths to preserve — character traits, exemplary skills, tool patterns, permission archetype fit]

### Component scores
| Area | Score | Critical issues |
|------|-------|-----------------|
| Identity | N/M (%) | ... |
| Operations | N/M (%) | ... |
| ... | ... | ... |

Scores MUST be numeric: count evaluation criteria from the principle doc for that area (M), count criteria passed (N). Qualitative labels (Good/Mixed) are not sufficient for cross-project comparison.

### Priority roadmap
1. [Fix now — blocks correct behavior]
2. [Fix soon — quality/reliability]
3. [Phase N additions — structural]

### References
- Principle docs cited
- examples/ for remediation patterns
```

### 3b. Write report file (if requested)

If the user asks for a shareable report, or says "save", "write report", or "generate file":

1. Write to `reviews/<agent-name>-YYYY-MM-DD.md` using the synthesized report from Step 3
2. Include executive summary, patterns that work well, component scores, priority roadmap, and references
3. Confirm: "Report saved to reviews/<filename>"

Default behavior: on-screen output only. Reports are ephemeral — share and delete.

### 4. Offer next actions

Present as distinct actionable options (not buried in report):

- Run **populate** if KB thin but structure sound
- Run targeted re-review after fixes applied
- Point to `docs/decision-guide.md` for phase progression
- Suggest specific Phase N additions based on maturity estimate

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.
- **Subagent review fails or returns empty:** Note failure in component table; continue with remaining areas.

## Success criteria

- All 7 review areas assessed (or N/A documented with reason)
- Skills↔tools cross-reference completed (flag existence, error coverage, output schema)
- Executive summary with phased maturity estimate
- Every critical issue has principle doc reference and fix direction

## Checklist

- [ ] Target structure discovered; component inventory built
- [ ] All 7 review subagents launched (or N/A documented)
- [ ] Skills-tools cross-reference completed (Step 2b)
- [ ] Report synthesized with N/M (%) scores, executive summary, patterns that work well, roadmap
- [ ] Report file written (if requested)
- [ ] Next actions offered as distinct options

## Gotchas

- **External repo:** read-only review unless user asks to apply fixes
- **Do not demand Phase 4 components on Phase 1 agents** — note as roadmap items
- **Distinguish harness fault vs content fault** (subject vs meta-evaluator framing)
- **Missing-vs-deliberately-absent:** If evidence shows intentional design choices (comments, README, rejected patterns), include a **Design choices noted** section and flag as **diverges from framework recommendation** — do not penalize in aggregate score
- **Shareable reports:** File output is optional; default is on-screen summary. Reports in `reviews/` are gitignored and ephemeral
