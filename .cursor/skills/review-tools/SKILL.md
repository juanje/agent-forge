---
name: review-tools
description: Review bin/ wrappers and tools/ Python CLIs for agent-facing API design. Trigger when reviewing tools, bin/, or CLI wrappers.
---

# Review Tools

## Trigger

User asks to review tools, bin/, wrappers, or CLI design.

## Steps

1. **Detect harness** — check which runtime the target agent uses (WHY: wrong harness assumption produces false P0 findings):
   - `.pi/permissions.json` + `.pi/settings.json` → Pi agent; evaluate permissions against Pi policy
   - `.claude/settings.json` → Claude Code; evaluate deny rules there
   - `.cursor/rules/` → Cursor; evaluate rule files for tool restrictions
   - Multiple present → note dual-harness; evaluate the primary and flag gaps in secondary
   - None → flag as critical (no tool write protection)

2. List `bin/*` and corresponding `tools/*.py` (or `scripts/`)

3. Read Evaluation Criteria from `docs/principles/tool-design.md`

4. Per tool assess against all criteria sections in the doc (Wrappers, Tool implementations, Mutation tools, Shared module, Skill integration)

5. Check tool write protection (harness-appropriate from Step 1):
   - Pi: permissions.json denies write to tools/ and bin/
   - Claude Code: .claude/settings.json deny rules
   - Cursor: .cursor/rules/ covering tool immutability

6. Compare `examples/tools/` patterns

7. **Pre-report check:** Verify every bin/ tool has been assessed against all tool-design.md criteria sections. If harness was detected as Pi but only Claude Code was evaluated (or vice versa), reassess.

8. Report with before/after for flag/interface issues

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.
- **No bin/ or tools/ found:** Report N/A with recommendation (bootstrapper, memory-only agents), not as critical error.

## Success criteria

- Harness detected and stated in report
- Every bin/ tool reviewed against all doc criteria sections
- Tool write protection verified (harness-appropriate)
- Shared module usage assessed (not copy-pasted logic across tools)

## Checklist

- [ ] Harness detected and stated
- [ ] bin/ and tools/ listed
- [ ] Evaluation criteria read from tool-design.md
- [ ] Each tool assessed against all doc sections
- [ ] Tool write protection verified (harness-appropriate)
- [ ] Compared against examples/tools/
- [ ] Pre-report check completed
- [ ] Report with before/after for flag/interface issues

## Gotchas

- **No tools is valid:** Bootstrappers, memory agents, and meta-agents may have no bin/ or tools/. Flag N/A, not critical.
- **Missing-vs-deliberately-absent:** Shell commands used directly without wrappers may be intentional for low-risk generators — note risk, do not auto-FAIL.
- **Harness detection:** Check `.pi/permissions.json` before assuming Claude Code. Wrong harness assumption produces false P0 findings.
- **Hidden --timeout:** Internal retry constants are correct; exposing --timeout to the agent is the anti-pattern.
