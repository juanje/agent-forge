# Decision Guide

Architectural choices for process-oriented agents. Use during bootstrap and when improving existing agents.

## Harness selection

| Choice | When | Tradeoff |
|--------|------|----------|
| **Minimal harness** (Pi, similar) | Shared team agents, model flexibility, audit trail, compliance | Terminal workflow; you build guardrails |
| **IDE-integrated** (Claude Code, Cursor) | Fast individual iteration, rich UX | Less distributable; permissions via hooks/settings |
| **Both** | Migration or dual-user base | Same skills/KB/tools; permission enforcement differs |

Skills, knowledge base, and tool wrappers are **portable** across harnesses. What changes: permission enforcement mechanism and hook/extension system.

## Memory model

| KB size | Approach |
|---------|----------|
| Up to ~1000 entries | File-based + index navigation (no RAG needed) |
| Massive corpus | Consider RAG supplement — not default for process agents |

**Always:** Four-store separation for agents that learn from their work (see memory-architecture).

## Tool freedom spectrum

| Factor | Restrict (wrapped tools only) | Allow (broader access) |
|--------|-------------------------------|------------------------|
| Domain knowledge | Not in model training data | Well-represented |
| Task structure | Known workflow with required steps | Open exploration |
| Failure cost | High (trusted diagnosis) | Low (human reviews output) |

**Diagnostic / compliance agents:** Restrict. **Productivity / exploration agents:** More permissive.

## Phase progression

| Phase | Add when | Components |
|-------|----------|------------|
| **1 — Day 1** | Always | Identity, operations guide, 1 skill, 1 tool, minimal knowledge base, permissions |
| **2 — Week 1-2** | Agent needs to persist findings | Capture skill, episodic history, record template |
| **3 — Week 2-4** | 10+ records accumulated | Consolidation skill, semantic knowledge, stats script |
| **4 — Maturity** | Multiple workflows validated | Secondary skills, verification procedures, health checks |

**Rule:** Do not skip Phase 1 validation. Complexity is earned through usage.

## Identity placement

| Content | Identity / system prompt | Operations guide | Skill |
|---------|-------------------------|------------------|-------|
| Character traits | Yes | No | No |
| KB map with triggers | No | Yes | No |
| Procedure steps | No | No | Yes |
| Tool flag explanations | No | No | Yes (in steps) |
| Hard limits | Yes | No | No |

## Post-bootstrap next steps

1. Run **populate** — import knowledge base content, convert runbooks to skills
2. Test with a real task in target harness
3. Run **full-review** on generated agent
4. Meta-evaluate session (the agent can't reliably diagnose its own harness gaps)
5. Iterate: test → fix → test
