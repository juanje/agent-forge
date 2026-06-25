# Anti-Patterns

Cross-cutting mistakes observed in production agent development. Review skills consult this during any audit.

## Instruction and identity

| Anti-pattern | Why it fails | Fix | Principle |
|--------------|--------------|-----|-----------|
| Long rule lists in system prompt | Gaps, conflicts, brittleness | 80% character + 20% limits | identity-and-character |
| KB map in identity / system prompt | Wastes highest-reliability channel | Move to operations guide | instruction-delivery |
| "Read config first" without hook/auto-load | ~70% compliance | Use hooks or auto-injection | instruction-delivery |
| Critical rules buried deep in context | Smaller models ignore | Promote to Character in identity | instruction-delivery |
| Duplicate instructions across identity + operations | Double tokens / conflicts | Single responsibility per file | instruction-delivery |
| Extended thinking on procedural agents | Self-narration, slower, same quality | Use low thinking for procedural tasks | — |
| Instructions in HTML comments | Stripped by some harnesses; ignored by models | Visible markdown; comments only in templates, removed before ship | instruction-delivery |

## Tools and procedures

| Anti-pattern | Why it fails | Fix | Principle |
|--------------|--------------|-----|-----------|
| Tool syntax in identity / system prompt | Bypasses skills | Tools only in skill steps | skill-design |
| Global tool inventory in config | Agent improvises | Skills teach tools in context | skill-design |
| `--tail`/`--limit`/`--timeout` flags exposed | Agent parameter-sweeps | Two modes: extract / download; bake defaults | tool-design |
| Raw stack traces to agent | Agent invents workarounds | Structured error with pivot suggestion | tool-design |
| Skill says "don't read file" + file available | Thoroughness instinct wins | Skip signal in tool output | tool-design |

## Memory

| Anti-pattern | Why it fails | Fix | Principle |
|--------------|--------------|-----|-----------|
| Flat patterns file rewritten incrementally | Drift compounds in single file | Hierarchical knowledge with category indexes | memory-architecture |
| LLM-computed statistics | Plausible but wrong numbers | Script-derived stats | memory-architecture |
| Trust knowledge match blindly | Wrong diagnosis trusted | Disconfirmation gate in skill | skill-design |
| Empty knowledge schema first | Inertia, no gravity | Bootstrap with real content | memory-architecture |
| Edit closed records in history | Breaks immutability contract | Move to history + append only | memory-architecture |

## Permissions

| Anti-pattern | Why it fails | Fix | Principle |
|--------------|--------------|-----|-----------|
| Skill declares tool access, no enforcement | Advisory only; no real guardrail | Enforce in permission system | permissions-as-design |
| Writable tool source | Proxy escape risk | Deny writes to tool paths | permissions-as-design |
| Broad command denies | Breaks harmless operations | Specific denies per command | permissions-as-design |

## Evaluation and adoption

| Anti-pattern | Why it fails | Fix | Principle |
|--------------|--------------|-----|-----------|
| Agent self-diagnoses its own harness | Post-hoc rationalization | Separate meta-evaluator | — |
| Single-fix validation | Misses cascade effects | Fix-cascade scoring across sessions | — |
| More rules when model ignores procedure | Structural issue, not comprehension | Permissions + tool output design | instruction-delivery |
| Shared agents before local skills | High coordination cost | Skills-first adoption | skill-design |
| RAG for ~200 entries | Disconnected chunks vs full-context files | File-based navigation | progressive-disclosure |
| Shared identity in runtime package | Coupling + update risk across agents | Template copy at bootstrap; each agent owns identity | identity-and-character |
