---
name: populate
description: Post-bootstrap population — import KB, create skills from runbooks, guide iteration. Trigger when user has existing docs, runbooks, repos to import, wants to create skills from procedures, or immediately after bootstrap.
---

# Populate — Fill Agent Skeleton

## Trigger

- User says import knowledge, populate KB, create skill from procedure
- User points to existing repos, wikis, runbooks, SOPs
- Bootstrap just completed — offer populate as next step

## Prerequisites

Target agent repo path must exist (bootstrapped or user-provided).

Read:
- `docs/principles/progressive-disclosure.md`
- `docs/principles/skill-design.md`
- `docs/principles/memory-architecture.md`
- Target agent's `AGENTS.md` and kb/ structure

## Steps

### 1. Assess current state

Read target agent:
- Existing kb/ directories and indexes
- Existing skills and tools
- AGENTS.md map

Report gaps: empty indexes, missing skills for stated tasks, missing tools for external systems.

### 2. Import domain knowledge into KB

**Ask user** for sources:
- Local repo paths
- Wiki URLs or exported markdown
- Runbooks, Confluence exports, past incident threads

For each source:

1. **Classify store** (memory-architecture) (WHY: store classification determines write paths and index placement — importing first and organizing later creates rework and permission mismatches):
   - Stable reference → `kb/<reference>/` (read-only)
   - Recurring patterns → plan for `kb/known-issues/` (Phase 3)
   - Past incidents → `kb/history/` or seed `kb/active/` if open

2. **Extract or summarize** content appropriate to store type

3. **Update index.md** — every new file gets index entry: path, what, when trigger

4. **Update AGENTS.md** map if new top-level kb/ directory

**Large imports:** Recommend parallel subagents in target repo (Cursor Task / Claude subagent) — one per source directory. Parent agent merges index entries.

Reference: `templates/fragments/index-md.md`, `examples/skills/capture-skill.md`

### 3. Create skills from existing procedures

**Ask user** for:
- Runbook / SOP file paths, or
- Verbal description of "how I usually do X"

For each procedure:

1. Identify **trigger phrases** and map to AGENTS.md table
2. Transform to SKILL.md:
   - Frontmatter name + description (routing signal)
   - Numbered steps with embedded bin/ calls
   - Pre-action gates before report/close
   - Disconfirmation gate if diagnostic/hypothesis-based
   - Success criteria
3. Cross-check against `docs/principles/skill-design.md` Evaluation Criteria
4. Add `allowed-tools` in frontmatter; **update permissions.json** (paired-update rule)
5. Place in `.pi/skills/<name>/` or `.cursor/skills/<name>/` per target harness

Reference: `examples/skills/diagnostic-skill.md`, `templates/fragments/skill.md`

### 4. Create missing tools

If procedure references external system without bin/ wrapper:
- Generate from `templates/fragments/tool-wrapper.sh` and `tool-python.py`
- Two modes only: default (structured summary) + --output
- Register in cli.py; update .env.example

Reference: `examples/tools/api-query-tool.md`

### 5. Pre-guidance check

Verify at least one KB import (Step 2) or one skill creation (Step 3) completed successfully. If neither produced output, do not proceed to iteration guidance — report what blocked and recommend resolving before iterating.

### 6. Guide iterative improvement

After population, recommend:

| Order | Action |
|-------|--------|
| 1 | Test primary skill with real task in target harness |
| 2 | Run `full-review` on target agent |
| 3 | Phase 2: add capture skill if agent should persist findings |
| 4 | Phase 3: consolidate when 10+ incidents exist |

Provide concrete commands for target harness (Pi vs Claude Code/Cursor).

Point to `docs/decision-guide.md` Phase progression.

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.
- **Source path not readable:** Skip that source; report which sources were skipped.

## Success criteria

- At least one KB import OR one new skill from procedure completed
- All new kb/ content has index.md entries with what + when
- New skills have success criteria and permissions parity
- User has clear next test step and review recommendation

## Checklist

- [ ] Current agent state assessed (kb/, skills, tools, AGENTS.md)
- [ ] Domain knowledge imported with index.md entries
- [ ] Skills created from procedures with success criteria
- [ ] Missing tools created from templates
- [ ] Pre-guidance check passed (at least one import or skill completed)
- [ ] Iteration guidance given (test → full-review → Phase 2)

## Gotchas

- **Do not dump raw wiki into SYSTEM.md** — KB only.
- **Do not create known-issues/ before episodic capture workflow exists** — respect phase order.
- **Index entries must be operational triggers**, not descriptions.
- **Missing-vs-deliberately-absent:** User may defer skill creation — document as roadmap, not failure.
- **For Pi agents:** Verify allowed-tools ↔ permissions.json after each new skill (paired-update rule).
