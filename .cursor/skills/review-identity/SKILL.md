---
name: review-identity
description: Review agent SYSTEM.md, CLAUDE.md identity, or SOUL.md for character and limits quality. Trigger when reviewing identity, system prompt, or character traits.
---

# Review Identity

## Trigger

User asks to review SYSTEM.md, identity, character traits, or system prompt section.

## Steps

1. Locate identity file in target repo:
   - Pi: `.pi/SYSTEM.md`
   - Memory-agent style: `identity/SOUL.md` or symlinked SYSTEM.md under a dedicated identity/ directory
   - Unified: `CLAUDE.md` identity sections

2. Read Evaluation Criteria from:
   - `docs/principles/identity-and-character.md`
   - `docs/principles/instruction-delivery.md` (system prompt placement rules)

3. Evaluate each criterion — **pass / fail / partial** with quoted evidence

4. Read `docs/anti-patterns.md` instruction rows for additional checks (WHY: anti-patterns catch cross-cutting issues that individual criteria miss; reading them after initial assessment avoids bias toward anti-pattern hunting over criteria evaluation)

5. For each failure: provide specific fix with before/after snippet

6. Reference `examples/system-prompts/` for positive patterns

7. **Pre-report check:** Verify all identity-and-character criteria from Step 2 have a pass/fail/partial entry. If any criterion was not assessed, go back and assess it before reporting.

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.

## Report format

```markdown
## Identity Review — [agent name]

### Summary
[1-2 sentences overall assessment]

### Criteria
| Criterion | Status | Evidence / Fix |
|-----------|--------|--------------|
| ... | pass/fail | ... |

### Priority fixes
1. [Highest impact]
```

## Success criteria

- All identity-and-character Evaluation Criteria assessed
- Every fail has actionable fix referencing principle doc
- 80/20 character vs limits ratio checked

## Checklist

- [ ] Identity file located (SYSTEM.md / CLAUDE.md / SOUL.md)
- [ ] Evaluation criteria read from identity-and-character.md + instruction-delivery.md
- [ ] Each criterion assessed with pass/fail/partial + evidence
- [ ] Anti-patterns checked
- [ ] Each failure has before/after fix
- [ ] Examples referenced for positive patterns
- [ ] Pre-report check completed

## Gotchas

- **Identity statement vs character traits:** "You are..." is not the same as domain character traits. Missing traits is a gap; choosing values-over-rules is a design choice — flag as **diverges from framework recommendation**, not FAIL.
- **Missing-vs-deliberately-absent:** If comments, README notes, or design docs show the author intentionally omitted a pattern, flag as **diverges from framework recommendation** rather than FAIL.
- **Operational rules disguised as limits:** "ALWAYS fix X before Y" is procedure, not a limit. Move to baseline or skill steps.
- **Domain knowledge in identity:** Product lineage, issue tracker projects, toolchain details belong in reference/KB — not in SYSTEM.md or CLAUDE.md identity sections.
