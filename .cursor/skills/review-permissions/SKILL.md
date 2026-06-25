---
name: review-permissions
description: Review permissions.json for deny-by-default, path rules, and skill parity. Trigger when reviewing permissions or guardrails.
---

# Review Permissions

## Trigger

User asks to review permissions.json, guardrails, or tool access policy.

## Steps

1. Read target `.pi/permissions.json` (or document Claude Code equivalent)

2. Read Evaluation Criteria from `docs/principles/permissions-as-design.md`

3. Assess deny-by-default, read/write/bash split, path rules

4. Identify archetype: restrictive diagnostic vs permissive memory — **before** scoring deny-by-default (WHY: permissive agents fail restrictive criteria by design; archetype context prevents false FAILs)

5. **Paired-update audit:** For each skill with allowed-tools, verify matching bash allow patterns

6. Check: tools/* bin/* write deny, .env deny, self-protection (Pi gate)

7. settings.json includes pi-permission-gate if Pi agent

8. **Pre-report check:** Verify all permissions-as-design criteria from Step 2 have a pass/fail entry, and every skill's allowed-tools has been paired against bash allow patterns. If any criterion was not assessed, go back and assess it before reporting.

9. Report security gaps and behavior-design gaps separately

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.

## Success criteria

- All permissions-as-design criteria assessed
- Skill-permission parity table produced
- Archetype fit explicitly stated

## Checklist

- [ ] permissions.json (or harness equivalent) read
- [ ] Evaluation criteria read from permissions-as-design.md
- [ ] Deny-by-default assessed
- [ ] Agent archetype identified (restrictive vs permissive)
- [ ] Paired-update audit: skills ↔ bash allow patterns
- [ ] Tool/bin write deny verified
- [ ] Pi permission-gate in settings.json (if Pi agent)
- [ ] Pre-report check completed
- [ ] Report delivered with security vs behavior gaps separated

## Gotchas

- **Archetype identification first:** Identify restrictive vs permissive before scoring deny-by-default — productivity agents with human review may legitimately be permissive.
- **Missing-vs-deliberately-absent:** Advisory-only permissions may be Phase 1 intentional — flag as roadmap item, not critical FAIL, if agent purpose is PoC with human review.
- **Split vs unified config:** Pi uses permissions.json; Claude Code uses settings.json; Cursor uses rules. Evaluate the harness present, not all three.
- **Skill-permission parity:** allowed-tools in skills is advisory unless the harness enforces it — note both declaration and enforcement.
