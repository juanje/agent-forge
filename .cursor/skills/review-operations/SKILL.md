---
name: review-operations
description: Review AGENTS.md or CLAUDE.md operations — navigation map, trigger table, defaults. Trigger when reviewing operations guide or AGENTS.md.
---

# Review Operations

## Trigger

User asks to review AGENTS.md, operations guide, navigation map, or trigger table.

## Steps

1. Locate operations file: `AGENTS.md` and/or `CLAUDE.md` (exclude pure identity if split)

2. Read Evaluation Criteria from:
   - `docs/principles/instruction-delivery.md`
   - `docs/principles/progressive-disclosure.md` (map quality)

3. Verify:
   - "Where to find things" entries have what + when
   - Procedure trigger table complete vs actual skills in repo
   - "Re-invoke on every new intent" present
   - Default approach defined
   - No identity content duplicated from SYSTEM.md (WHY: duplicated identity wastes context and drifts — one source of truth)
   - Operational lines only (not descriptive filler)

4. Cross-check: list skills in `.pi/skills/` or `.cursor/skills/` — every skill should appear in trigger table or have documented reason not to

5. **Pre-report check:** Verify every instruction-delivery criterion has a pass/fail entry and every skill in the directory appears in the trigger table assessment. (WHY: operations reviews often miss 1-2 criteria under context pressure; this gate catches gaps before report generation.)

6. Report pass/fail per criterion with fixes

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.

## Success criteria

- All instruction-delivery AGENTS.md criteria assessed
- Trigger table ↔ skills directory consistency verified
- Priority fixes ordered by impact on skill routing

## Checklist

- [ ] Operations file located (AGENTS.md / CLAUDE.md)
- [ ] Evaluation criteria read from instruction-delivery.md + progressive-disclosure.md
- [ ] All verification items checked (what+when, trigger table, re-invoke, default approach, no duplication)
- [ ] Skills directory cross-checked against trigger table
- [ ] Pre-report check completed
- [ ] Report with pass/fail per criterion

## Gotchas

- **Phase 1 minimalism:** A minimal operations section is valid for Phase 1 agents. Do not demand full trigger tables on single-skill agents.
- **Missing-vs-deliberately-absent:** If evidence shows intentional omission, flag as **diverges from framework recommendation** rather than FAIL.
- **Split vs unified config:** Some agents use CLAUDE.md only; others split SYSTEM.md + AGENTS.md. Evaluate against the agent's chosen structure, not a fixed layout.
- **Descriptive filler:** "This project helps with..." paragraphs waste context. Operations files should be routing and triggers only.
