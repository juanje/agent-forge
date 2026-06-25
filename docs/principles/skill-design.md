# Skill Design

## Core Concept

**Skills are procedures, not tool documentation.** When agents see tool syntax in a global reference (system prompt, README, tool appendix), they call tools directly and skip the procedure — bypassing verification, capture, and guardrails. Tools should only appear inside skill steps, where the procedure controls when and why each tool is called.

Every skill needs three components: a **trigger** that tells the agent when to invoke it, **numbered steps** that define the exact sequence, and **success criteria** that tell the agent when it's done. Without a clear trigger, the agent doesn't know when to use the skill. Without numbered steps, it improvises the order. Without success criteria, it either stops too early or over-investigates. The quality bar for skill content is strict: every line should change what the agent does — if removing a line doesn't change behavior, it's filler that wastes context budget.

## Design Rules

1. **Trigger in description** — Skill description is the routing signal (~80% of routing quality). Make triggers explicit and specific.

2. **Trigger table in operations guide** — Maps user intents to skills; re-invoke on every new intent.

3. **No global tool inventory** — Tool syntax lives in skill steps only. The agent learns tools through procedures, not through a reference list.

4. **Operational prose** — "Run exactly ONE row from lookup table" beats flat menus (especially for smaller models).

5. **Negative constraints near action** — "Do NOT poll status" at the step that polls, not in a separate rules section.

6. **Pre-action gates** — Imperative checkpoints before terminal actions (report, capture, close).

7. **Disconfirmation gate** (diagnostic skills) — "What evidence would contradict this hypothesis? Check before reporting."

8. **Depth obligation** — KB match ≠ shallow investigation; mandate evidence depth in steps.

9. **Success criteria** — Explicit done conditions (root cause + evidence, or new pattern documented).

10. **Separate capture from consolidate** — Different skills with different write permissions and different purposes.

11. **Skill-permission parity** — Tool access declared in skills must match what the permission system actually allows. Keep both in sync.

12. **Target size** — ~100–150 lines per skill; split if larger (though complex core skills may justify exceeding this).

13. **Completion checklist for complex skills** — Skills with 5+ steps add a checklist section at the end: a compressed mirror of all steps as checkbox items. Models exhibit recency bias — a short checklist after many lines of procedure re-activates step awareness before the agent reports. Not needed for skills under 5 steps.

## Evaluation Criteria

- [ ] Description with clear trigger phrases (routing signal)
- [ ] Trigger section or description covers when to invoke
- [ ] Numbered steps with explicit order
- [ ] Tool calls embedded in steps (not separate tool reference appendix)
- [ ] Error handling steps (what to do when tool fails)
- [ ] Success criteria section
- [ ] Diagnostic skills: disconfirmation or verify step where applicable
- [ ] Pre-action gate before final report/capture/close
- [ ] WHY for non-obvious step order (efficiency, safety)
- [ ] No duplicate fetches across skills (e.g., status skill re-fetching what diagnosis skill will fetch)
- [ ] Skill-permission parity verified
- [ ] Skills with 5+ steps: completion checklist at end (compressed step mirror)
- [ ] Gotchas section for domain-specific pitfalls (tool restrictions, endpoint naming, format traps)

## Good Examples

### Skill with steps, gates, and checklist

```markdown
---
name: diagnose
description: Investigate a failure. Trigger when user provides an ID, URL, or asks why something failed.
---

## Steps

1. Fetch metadata via the appropriate query tool
2. Identify failed components; if none failed, report success and stop
3. For each failure, extract relevant logs
4. **Disconfirmation gate:** If known-issue matches, seek evidence that would contradict it before classifying
5. Classify each failure
6. Verify outcome independently (don't trust status field alone)
7. Compose report: summary, root cause, evidence chain, confidence
8. Capture findings

## Success criteria

- Root cause identified with cited evidence, OR
- New pattern documented for consolidation

## Checklist

Complete each step in order:
- [ ] Step 1: Metadata fetched
- [ ] Step 2: Failed components identified
- [ ] Step 3: Logs extracted
- [ ] Step 4: Known-issue hypothesis + disconfirmation
- [ ] Step 5: Failures classified
- [ ] Step 6: Outcome verified
- [ ] Step 7: Report composed
- [ ] Step 8: Findings captured
```

*The checklist mirrors the steps in compressed form. Recency bias works in your favor — the model sees this summary right before acting.*

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| Skill has a "Tool Reference" appendix listing all flags of 4 tools | Agent reads flags out of context, calls tools directly bypassing the procedure steps | Embed each tool call in its procedure step with WHY that flag matters: "Step 3: `bin/query --extract` (extraction covers 80% of cases; download only if extract is insufficient)" |
| Skill ends with step 8 but no "## Success criteria" | Agent doesn't know when it's done; may over-investigate or stop too early | "Root cause identified with cited evidence, OR new pattern documented for follow-up" |
| "Step 4: Check known issues for matches" — then proceeds to report | If a known issue matches, agent reports without verifying it still applies; resolved issues get re-reported | "Step 4: If match found, seek evidence that would **contradict** this match before classifying" |
| 400-line skill covering status check + diagnosis + capture + consolidation | Too many concerns; agent loses track; context pressure causes late steps to be skipped | Split into focused skills: `check-status` → `diagnose` → `capture` → `consolidate` |
| Skill metadata says "can use git mv" but permission system blocks it | Agent tries, gets denied, wastes a turn, may improvise a workaround | Paired-update: add matching permission rule when adding tool access to skill |
| 8-step diagnostic skill; agent consistently skips steps 5-7 | After 300 lines of procedure, model's attention is on most recent content (recency bias) | Add compressed checklist at end: `- [ ] Step 5: Classify` ... — re-activates awareness of skipped steps |
