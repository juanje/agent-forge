---
name: review-skills
description: Review SKILL.md procedures for quality, gates, and permission parity. Trigger when reviewing skills or procedures.
---

# Review Skills

## Trigger

User asks to review skills, procedures, or SKILL.md files.

## Steps

1. List all skills in target: `.pi/skills/*/SKILL.md`, `.cursor/skills/*/SKILL.md`

2. Read Evaluation Criteria from `docs/principles/skill-design.md`

3. Per skill assess:
   - Frontmatter description (trigger routing)
   - Numbered steps, tool calls embedded
   - Success criteria
   - Disconfirmation / verify gates (if diagnostic)
   - allowed-tools ↔ permissions.json (read permissions file)

4. Cross-skill: redundant API fetches between skills (status vs diagnose pattern)

5. Note strengths: Gotchas sections, exemplary gates, clean handoff chains — not only failures

6. Compare against `examples/skills/` annotated patterns

7. Report per skill with priority fixes

8. **Cross-check totals:** count pass/fail across all per-skill tables; verify systemic summary matches per-skill details. Flag any inconsistency before finalizing report.

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.

## Success criteria

- Every SKILL.md in target reviewed
- Skill-permission parity checked
- Strengths and good patterns recognized (not only failures)
- Systemic summary cross-checked against per-skill details

## Checklist

- [ ] All SKILL.md files listed
- [ ] Evaluation criteria read from skill-design.md
- [ ] Each skill assessed with pass/fail evidence
- [ ] Cross-skill redundancy checked
- [ ] Strengths noted (Gotchas, gates, handoff chains)
- [ ] Compared against examples/skills/
- [ ] Per-skill report produced
- [ ] Totals cross-checked against per-skill tables

## Gotchas

- **Skills under 5 steps:** Do not require completion checklists (Rule 13). Do not flag absence as a gap.
- **Missing-vs-deliberately-absent:** Intentionally inline procedures (no skills system) may be a design choice — flag as **diverges from framework recommendation** if documented.
- **Harness differences:** Pi uses `.pi/skills/`; Cursor uses `.cursor/skills/`; Claude Code may symlink. Do not penalize path choice.
- **allowed-tools parity:** Cursor slash commands may use frontmatter differently — verify against the harness actually in use.
