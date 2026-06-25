---
name: review-memory
description: Review kb/ structure, four-store model, write rules, consolidation. Trigger when reviewing memory, KB, or capture/consolidate.
---

# Review Memory Architecture

## Trigger

User asks to review kb/, memory, capture, consolidate, or episodic/semantic stores.

## Steps

1. Map target `kb/` directory tree

2. Read Evaluation Criteria from `docs/principles/memory-architecture.md`

3. Assess:
   - Four stores identifiable (or phased plan documented)
   - permissions.json write paths match store model
   - index.md per content directory
   - Episodic write-once pattern in capture skill (if exists)
   - No flat patterns.md anti-pattern
   - stats.md script-only if present

4. Read capture/consolidate skills if present — generator/evaluator separation (WHY: capture and consolidate must be separate skills with different write permissions; a single skill that captures and consolidates violates store boundaries)

5. AGENTS.md maps each store with triggers

6. **Pre-report check:** Verify all four-store criteria assessed and write permissions cross-checked. If capture/consolidate skills exist but were not reviewed, go back to Step 4.

7. Report gaps with Phase 2/3 recommendations from `docs/decision-guide.md`

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.

## Success criteria

- Store model assessed against four-store criteria
- Write permissions cross-checked
- Phase-appropriate recommendations (don't demand Phase 3 on Day 1)

## Checklist

- [ ] kb/ directory tree mapped
- [ ] Evaluation criteria read from memory-architecture.md
- [ ] Four-store model assessed (or phased plan noted)
- [ ] Capture/consolidate skills reviewed (if present)
- [ ] AGENTS.md store mapping verified
- [ ] Pre-report check completed
- [ ] Phase-appropriate gaps reported with decision-guide.md recommendations

## Gotchas

- **Phase 1 agents:** May have no KB structure yet. Score against current phase, not Phase 3 expectations.
- **Missing-vs-deliberately-absent:** Static reference-only agents may skip episodic/history stores by design — flag as **diverges from framework recommendation** if intentional.
- **Flat patterns.md:** A single patterns file without store separation is an anti-pattern unless documented as Phase 1 temporary.
- **stats.md:** Must be script-generated only — never LLM-written computed statistics.
