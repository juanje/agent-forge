# Documentation

Design principles for process-oriented AI agents. Each doc is self-contained — share individually or read as a set.

## Principles

Read [principles/index.md](principles/index.md) for the content map.

| Doc | Read when |
|-----|-----------|
| [identity-and-character](principles/identity-and-character.md) | Writing agent identity, character traits, limits |
| [instruction-delivery](principles/instruction-delivery.md) | Deciding where instructions live (system prompt vs operations vs skills) |
| [progressive-disclosure](principles/progressive-disclosure.md) | Structuring knowledge base navigation and context layers |
| [tool-design](principles/tool-design.md) | Designing agent-facing tools and wrappers |
| [skill-design](principles/skill-design.md) | Writing procedural skills with triggers and gates |
| [memory-architecture](principles/memory-architecture.md) | Structuring file-based memory, capture, consolidation |
| [permissions-as-design](principles/permissions-as-design.md) | Designing guardrails that channel behavior |

## Supporting docs

| Doc | Read when |
|-----|-----------|
| [glossary](glossary.md) | Unsure what "identity", "operations guide", or "permission system" means in your harness |
| [anti-patterns](anti-patterns.md) | Any review — cross-cutting mistakes to check |
| [decision-guide](decision-guide.md) | Choosing harness, memory model, tool freedom, phase progression |

## How review skills use this

Each principle doc has an **Evaluation Criteria** section — a structured checklist. Review skills read that section, check each criterion against the target file, and report pass/fail with references back to the Design Rules.

Improving the docs improves all reviews — criteria are not hardcoded in skills.
