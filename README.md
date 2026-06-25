# Agent Forge

Documentation and meta-agent toolkit for creating, bootstrapping, and evaluating
**stateful AI agents with persistent memory and process-oriented design**.

The documentation captures design principles for agents that follow procedures, maintain
structured memory, and use controlled tools in a specific domain (diagnostics, triage,
compliance, release health, test analysis). The meta-agent applies those principles:
it bootstraps new agents from scratch and reviews existing ones against the documented
criteria.

These agents are different from general coding assistants. Their value comes from
**identity** (who they are), **procedures** (how they work), **memory** (what they've
learned), and **guardrails** (what they can't do) — not from open-ended tool access.

> **Who is this for?** Engineers who want to build a domain-specific agent and need a
> structured path: from discovery interview to a working skeleton, populated knowledge
> base, and validated design.

---

## What you get

Open this repo in [Cursor](https://cursor.com) or [Claude Code](https://claude.ai/code). The repo itself is a configured agent with
ten skills:


| Skill                   | What it does                                                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bootstrap**           | Runs a structured interview about your domain → generates a working agent skeleton: identity, first skill, first tool, knowledge base, permissions |
| **Populate**            | Imports existing docs and runbooks into the agent's knowledge base (KB); converts procedures into skills                                           |
| **Full review**         | Comprehensive audit — orchestrates all seven review skills in sequence                                                                             |
| **Review: identity**    | Audits `SYSTEM.md` / `CLAUDE.md` for character quality and hard limits                                                                             |
| **Review: operations**  | Audits the operations guide — navigation map, trigger table, defaults                                                                              |
| **Review: skills**      | Audits `SKILL.md` procedures for quality, gates, and permission parity                                                                             |
| **Review: tools**       | Audits `bin/` wrappers and `tools/` CLIs for agent-facing API design                                                                               |
| **Review: memory**      | Audits `kb/` structure, four-store model, write rules, and consolidation                                                                           |
| **Review: permissions** | Audits `permissions.json` for deny-by-default, path rules, and skill parity                                                                        |
| **Review: disclosure**  | Audits `index.md` files and progressive disclosure navigation                                                                                      |


## Quick start

```bash
git clone <repo-url>
# Open the folder in Cursor or Claude Code — no install required
```

Then type a prompt:

```
# Build a new agent from scratch
"Bootstrap a new agent for [your domain]"
# e.g. defect triage, release validation, incident diagnosis

# Review an agent you already have
"Full review of /path/to/my-agent"

# Import existing runbooks or docs into an agent's knowledge base
"Populate the KB from /path/to/runbooks"
```

---

## Design principles

Seven areas, each documented with rationale, design rules, evaluation criteria, and
examples:


| Principle                                                           | What it covers                                               |
| ------------------------------------------------------------------- | ------------------------------------------------------------ |
| [Identity and character](docs/principles/identity-and-character.md) | Who the agent is, how it reasons — values over rules         |
| [Instruction delivery](docs/principles/instruction-delivery.md)     | Where to put instructions so the model actually follows them |
| [Progressive disclosure](docs/principles/progressive-disclosure.md) | Three-layer context model — don't front-load everything      |
| [Tool design](docs/principles/tool-design.md)                       | Agent-facing tools that eliminate decisions, not inform them |
| [Skill design](docs/principles/skill-design.md)                     | Procedures with triggers, gates, and success criteria        |
| [Memory architecture](docs/principles/memory-architecture.md)       | Four-store model — separate by who writes and drift risk     |
| [Permissions as design](docs/principles/permissions-as-design.md)   | Guardrails that channel behavior, not just enforce security  |


Plus [anti-patterns](docs/anti-patterns.md), a [decision guide](docs/decision-guide.md),
and a [glossary](docs/glossary.md) that maps these terms to specific files in Cursor,
Claude Code, and [Pi](https://pi.dev/).

The principles are framework-agnostic — they apply whether you build on Claude Code,
Cursor, Pi, or another agent framework. They come from building and evaluating real
agents in production.

---

## Repository layout

```
agent-forge/
├── CLAUDE.md              # Forge agent identity and skill trigger table
├── .cursor/skills/        # Bootstrap, populate, and review skills
├── .claude/skills/        # Symlink → .cursor/skills (works in Claude Code too)
├── docs/
│   ├── principles/        # Seven principle docs
│   ├── anti-patterns.md
│   ├── decision-guide.md
│   └── glossary.md
├── templates/
│   ├── skeleton/          # Copy-ready Phase 1 agent structure
│   └── fragments/         # Per-component annotated templates
└── examples/              # Annotated extracts from production agents
```

## How the docs work

Each principle doc follows the same structure:

1. **Core Concept** — the WHY (shareable as standalone reference)
2. **Design Rules** — numbered, with rationale
3. **Evaluation Criteria** — checklist that review skills use
4. **Good Examples** — annotated patterns
5. **Bad Examples → Fix** — anti-patterns with corrections

Review skills read the Evaluation Criteria section and check each criterion against the target agent. Improving the docs improves all reviews automatically.