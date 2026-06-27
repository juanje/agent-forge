---
name: bootstrap
description: Create a new process-oriented agent from scratch. Trigger when user says create agent, new agent, bootstrap, or describes a domain agent to build.
---

# Bootstrap — Create New Agent

## Trigger

User wants to create a new process-oriented agent (diagnostics, triage, compliance, QE, releases, etc.).

## Prerequisites

Read before generating:
- `docs/principles/index.md`
- `docs/decision-guide.md`
- `templates/skeleton/` structure

## Steps

### 1. Discovery interview (WHY: generating without domain context produces generic agents that fail in production — discovery must come first)

Ask these questions **before generating files**. Batch related questions; do not skip.

| # | Question | Maps to |
|---|----------|---------|
| 1 | What is the agent's **purpose**? (one sentence) | Identity paragraph |
| 2 | What **domain**? (CI/CD, FuSa, QE, releases, security...) | Baseline, KB structure |
| 3 | What are the **primary tasks**? (list 1-3 for Phase 1) | Skills, trigger table |
| 4 | What **external systems** does it call? (APIs, logs, tickets) | bin/ tools, permissions bash |
| 5 | What **data sources** form the KB? (runbooks, wikis, past incidents) | kb/ directories, index.md |
| 6 | What **harness**? (Pi, Claude Code, Cursor, or multiple) | .pi/ vs .cursor/skills placement |
| 7 | Who is the **target user**? (individual, team, cross-team) | Permissions strictness |
| 8 | Where should the agent repo be created? (path) | Output directory |
| 9 | What are 2-3 **example phrases** a user would say to trigger each task? | Trigger table, skill "When to use" sections |

Confirm answers with user before proceeding.

### 2. Harness and archetype decisions

From answers, apply `docs/decision-guide.md`:
- Diagnostic/compliance → restrictive permissions archetype
- Productivity/memory → permissive archetype (document deviation from skeleton template)
- Pi → include `.pi/settings.json` with pi-permission-gate
- Claude Code/Cursor only → ensure `.cursor/skills/` or symlink pattern documented in README

### 3. Copy skeleton

```bash
cp -R templates/skeleton/ <target-path>/
chmod +x <target-path>/bin/*
```

Replace `{{PLACEHOLDERS}}` in all copied files.

### 4. Generate SYSTEM.md

Use `templates/fragments/system-prompt.md` and `docs/principles/identity-and-character.md` Evaluation Criteria.

- Identity paragraph: IS, DOES, IS NOT
- 3+ domain character traits (values, not action rules)
- Procedural trait mandatory
- 3-5 baseline principles
- Limits: read-only KB paths, episodic rules, domain restrictions

**Walk through draft with user** before writing final file.

Reference: `examples/system-prompts/diagnostic-agent.md` or `memory-agent.md` as appropriate.

### 5. Generate AGENTS.md

- "Where to find things" from data sources (step 1 Q5) — every entry: what + when
- Include `kb/index.md` as top-level KB hub (from skeleton template)
- Navigation guidance: single subordinate line ("Read on demand... Read indexes first, then specific files") — not a dominant opening instruction
- Never reference files that don't exist yet — every path in the map must be created during bootstrap
- Do **not** include "Skills in `.pi/skills/`..." lines — Pi knows skill locations; LLMs interpret as ls target
- Procedure trigger table from tasks (step 1 Q3) — use example phrases from Q9, not just capability names
- Default approach
- Post-task capture/commit if applicable

Reference: `templates/fragments/agents-md.md`

### 6. Generate permissions.json (WHY: permissions depend on the skills and KB paths defined in Steps 4-5 — generating them earlier would require rework)

Start from `templates/skeleton/.pi/permissions.json`. Adjust:
- `ls`: allow by default with secret path deny — do **not** deny ls entirely
- `read.paths.deny`: include `.git/*` alongside secrets
- `write.paths.allow` / `edit.paths.allow`: expand for KB lifecycle (history index, lessons, known-issues, tmp/)
- Remove blanket `kb/history/*` from write deny if present — allow index and closed-record writes
- `bash.allow`: add scoped grep (`grep * tmp/*`, `grep * kb/*`); do **not** allow `sed` — prefer `edit` tool
- `bash.allow` for git patterns skills will need
- Pair with skill allowed-tools (even if only primary skill so far)

Reference: `docs/principles/permissions-as-design.md`

### 7. Generate primary skill(s)

For 1-2 highest-priority tasks from discovery:
- Copy `templates/fragments/skill.md` structure
- Include **Step 0: Parse input** with user phrase examples from Q9
- Include **Tools available** table with preferred + fallback modes; explicit "do not --help"
- No Architecture/Design/Context preamble before Steps — start with When to use, Tools, Step 0
- Embed bin/ calls in numbered steps
- Add disconfirmation gate if diagnostic
- Define success criteria

Rename `.pi/skills/primary/` to meaningful skill name.

### 8. Generate tool stubs (WHY: tools wrap external system calls; the skill steps from Step 7 determine which tools are needed and how they should be called)

For each external system (step 1 Q4):
- `bin/<name>` from `templates/fragments/tool-wrapper.sh` — replace `{{TOOL_CLI_NAME}}` with the Click subcommand name (e.g. `service-health`)
- `tools/<name>.py` from `templates/fragments/tool-python.py` pattern — include `if __name__ == "__main__": cli()` guard
- Register in `tools/cli.py`
- Update `.env.example` with required variables

**PoC interface discipline:**
- Minimal interface for Phase 1 — what the skill calls is the interface; avoid extra flags the skill won't use
- Health checks: treat 401/403 as "up" (service reachable, auth may be missing in PoC)
- Detect placeholder/unconfigured URLs and report clearly instead of failing opaquely
- Auth tokens optional unless the endpoint requires them for the PoC scenario

### 9. Create KB structure

- `kb/index.md` as top-level hub (from skeleton template)
- `kb/<reference>/index.md` per data source category
- `kb/active/index.md` (from skeleton)
- Initial entries in reference index pointing to planned content (or stubs)

Reference: `templates/fragments/index-md.md`

### 10. Generate README

From skeleton README template with domain-specific quick start and Phase 2-4 roadmap from `docs/decision-guide.md`.

### 11. Validate (WHY: packaging and import issues are invisible until runtime — catching them here prevents a broken first session that wastes user trust)

Run these checks in the target directory. Fix any failures before proceeding.

```bash
cd <target-path>
uv sync                           # dependencies resolve and package installs
uv run tools --help               # entry point loads all subcommands
uv run ruff check tools/          # no lint errors in generated code
uv run ruff format --check tools/ # formatting consistent
```

Then smoke-test each wrapper:
```bash
for f in bin/*; do "$f" --help > /dev/null 2>&1 || echo "FAIL: $f"; done
```

If any tool fails `--help`, the import chain is broken — fix before reporting.

**Structural checks:**
- Verify every file path referenced in AGENTS.md exists on disk
- Verify each `bin/<name>` wrapper's CLI name matches a key in `pyproject.toml` `[project.scripts]`
- Verify `[build-system]` section exists in `pyproject.toml`

### 12. Report

Summarize:
- Files created and path
- Mapping: discovery answer → component
- Recommended next step: **populate** skill for KB import
- Recommended validation: test with real task, then **full-review**

## Error handling

- **Target file not found:** Report N/A for this area; do not skip remaining areas.
- **Permissions config absent:** Document as finding, not a blocker.
- **Harness ambiguous:** Document both; evaluate against primary.
- **Target directory already exists:** STOP and confirm with user before overwriting.

## Success criteria

- Phase 1 skeleton exists at target path with no unresolved `{{PLACEHOLDERS}}`
- SYSTEM.md passes identity-and-character Evaluation Criteria (spot check)
- At least one skill + one tool + kb/reference/index.md
- User confirmed identity draft
- `uv sync` succeeds and `uv run tools --help` shows all subcommands
- `ruff check tools/` passes with no errors
- All `bin/*` wrappers execute `--help` without error

## Checklist

- [ ] Discovery interview completed (9 questions)
- [ ] Harness and archetype decisions applied
- [ ] Skeleton copied to target path
- [ ] SYSTEM.md drafted and user-confirmed
- [ ] AGENTS.md generated with trigger table
- [ ] permissions.json generated with paired skill rules
- [ ] Primary skill(s) generated
- [ ] Tool stubs generated for external systems
- [ ] KB structure with index.md entries
- [ ] README generated
- [ ] Validation passed: `uv sync` + `agent-tools --help` + `ruff check` + `bin/*` smoke
- [ ] Report delivered with next steps

## Gotchas

- **Do not generate without discovery interview** — generic agents fail in production.
- **Do not put KB maps in SYSTEM.md** — progressive disclosure belongs in AGENTS.md and kb/index.md.
- **Remove HTML comments from templates** after customization — invisible to LLM.
- **Missing-vs-deliberately-absent:** If user rejects skills or permissions complexity, document as Phase 2 roadmap — do not force Phase 3 components on Day 1.
- **Pi vs Cursor:** Copy skills to `.cursor/skills/` or `.pi/skills/` per harness; document migration path in README.
- **Name from the user's perspective, not the document's.** When bootstrapping from a spec/design document, do not copy section headings as skill names or triggers. Ask: "what would the user say to invoke this?" Names like `check-services` beat `pre-flight`; triggers like "what failed?" beat "post-run analysis." If a skill has >5 steps, consider decomposing into atomic skills + orchestrator.
- **`{{TOOL_CLI_NAME}}` must match the Click subcommand name** registered in `cli.py` — e.g. if `main.add_command(foo.cli, name="service-health")`, then `{{TOOL_CLI_NAME}}` is `service-health`.
