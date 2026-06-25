---
name: review-disclosure
description: Review index.md files and progressive disclosure navigation. Trigger when reviewing KB indexes, navigation chain, or progressive disclosure.
---

# Review Progressive Disclosure

## Trigger

User asks to review index.md, progressive disclosure, KB navigation, or "can't find files" agent behavior.

## Steps

1. Discover all `index.md` under target agent `kb/` and operations maps in AGENTS.md

2. Read Evaluation Criteria from `docs/principles/progressive-disclosure.md`

3. For each index.md:
   - Entries have what + when
   - Frequency ordering where applicable
   - Child indexes linked from parent

4. Check for orphan directories (content files without index parent)

5. Verify AGENTS.md lists indexes before deep leaf paths

6. If permissions deny ls/grep/find: flag any directory missing index as **critical** (WHY: without exploration tools, the agent has no way to discover content in unindexed directories — indexes are the only navigation path)

7. **Pre-report check:** Verify every content directory with 3+ files has been assessed for index presence. Check `.gitignore` — gitignored directories are not orphans. (WHY: gitignored directories like output/ or reviews/ are often flagged as orphans but are deliberately excluded from navigation.)

8. Report with per-file fixes; reference `templates/fragments/index-md.md`

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.

## Success criteria

- Every kb/ content directory assessed for index presence
- All index entries checked for trigger quality
- Critical gaps flagged (missing index + denied ls)

## Checklist

- [ ] All index.md files under kb/ discovered
- [ ] Evaluation criteria read from progressive-disclosure.md
- [ ] Each index assessed (what + when, child links)
- [ ] Orphan directories identified (excluding gitignored paths)
- [ ] AGENTS.md lists indexes before deep leaf paths
- [ ] Critical gaps flagged (missing index + denied ls/grep/find)
- [ ] Pre-report check completed
- [ ] Report with per-file fixes

## Gotchas

- **Single flat directory:** One or two files do not need index.md. Flag missing indexes only when 3+ content files exist in a directory.
- **Missing-vs-deliberately-absent:** Small Phase 1 agents may defer KB indexes — recommend Phase 2, do not treat as blocking if structure is intentional.
- **Gitignored directories:** Check `.gitignore` before flagging orphan directories — ephemeral output dirs (e.g. `reviews/`) are not navigation gaps.
- **Permissions deny ls:** If grep/find/ls are denied, missing index.md is **critical** — agent cannot navigate without indexes.
- **Operational triggers:** Index entries must say when to read, not just describe content.
