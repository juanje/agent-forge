# Identity and Character

## Core Concept

Process-oriented agents need a coherent **identity** — who they are, how they reason, what they value — not a long list of rules. Character creates an **inference space**: the agent derives behavior in novel situations from values, not from matching the closest rule.

Identity lives in the **highest-reliability channel** available in your harness (system prompt, always-loaded config, or session-start hook). Placement matters more than wording — the same rule buried in a context file that the agent may or may not read fails silently, while the same rule in the system prompt is followed consistently.

Target ratio: **~80% character, ~20% hard limits**. If Limits outgrows Character, behavior is over-specified as rules instead of values.

## Design Rules

1. **Values, not actions** — Write why the agent prioritizes something; it derives what to do. Bad: "Always include error bars." Good: "Conservative in claims — never present data with more confidence than evidence supports."

2. **Include what the agent is NOT** — "You are not a summarizer. When asked to analyze, produce analysis." Prevents default generic assistant behavior.

3. **Ground traits in domain** — Generic "be helpful" is useless. "Verify-first: treat known patterns as hypotheses, not conclusions" applies to diagnostic agents.

4. **Resolve conflicts explicitly** — "When thoroughness conflicts with brevity, favor the reader's time — but flag omitted detail."

5. **Behavioral tendencies, not absolutes** — "Tend toward verify-first" beats "Always verify everything."

6. **Procedural mandate in character** — "I always work through skills — every task, every follow-up." Skills are invisible if the agent improvises with raw tools.

7. **Hard limits for never-violate boundaries** — Write restrictions, scope boundaries, compliance lines. Not derivable from character.

8. **Placement rule** — If removing it changes the agent's **first response to a novel question** → system prompt / identity. If it says **where to look** or **what sequence** → operations guide.

9. **Operational discipline traits** — Every agent needs traits about tool interaction (Tool-trusting, Direct), not just domain expertise. These explain WHY discovery shortcuts and script-based file generation fail — character inference space for novel situations.

10. **Procedure boundary limit** — Standard limit: stay within skill procedure during execution; no git history exploration, tool source reading, or repo-wide grep for data tools already provide. Tangential exploration pollutes context.

## Evaluation Criteria

- [ ] Identity paragraph states what the agent IS, DOES, and IS NOT (one paragraph)
- [ ] At least 3 domain-specific character traits (values/tendencies, not action lists)
- [ ] Procedural trait: skills mandatory when trigger matches
- [ ] Baseline section: 3–5 domain principles always applicable
- [ ] Limits section shorter than Character (80/20 ratio)
- [ ] Limits cover: read-only knowledge paths, write rules, scope boundaries
- [ ] Each limit passes the "never acceptable" test: would violating this EVER be acceptable? If yes → it belongs in Baseline or skills, not Limits
- [ ] No procedural steps disguised as limits (duplicating Character traits or skill steps)
- [ ] No domain knowledge disguised as limits (belongs in Baseline or knowledge base)
- [ ] No operational navigation (KB maps, trigger tables) in identity
- [ ] No tool syntax or global tool inventory in identity
- [ ] Traits use domain language (not generic assistant phrasing)
- [ ] Operational discipline traits present (Tool-trusting, Direct)
- [ ] Procedure boundary limit: no git history, tool source, or repo-wide grep during procedures

## Good Examples

```markdown
# [Agent Name]

You investigate [domain] failures for [system/team]. You identify
root causes with evidence chains. You are not an executor — you do not
[actions outside scope].

## Character

**Evidence-based.** Every claim links to a log line, API response, or KB entry.
You state confidence explicitly when evidence is partial.

**Verify-first.** Known patterns guide investigation; they never replace it.
The stronger the KB match, the harder you seek disconfirming evidence.

**Procedural.** I always work through skills. I never call tools directly
when a skill exists for the task.

## Limits

1. Never write to [read-only knowledge paths] — developer-maintained.
2. Episodic records are write-once; close by moving to history.
3. Procedures are mandatory when a trigger matches.
```

*Principles demonstrated: domain grounding, verify-first, procedural mandate, clear IS-NOT, limits as boundaries.*

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| 30 rules: "Never skip validation," "Always cite sources," "Format as tables," ... | Gaps between rules; conflicts ("be thorough" vs "be concise"); novel situations get no guidance | 3–5 character traits that derive behavior: "Evidence-based — cite sources; state confidence when partial" |
| "Be thorough and concise" | Contradicts itself with no resolution; agent follows whichever appears last in context | "When thoroughness conflicts with brevity, favor the reader's time — but flag what you omitted" |
| KB map ("Read `kb/errors/` for error types, `kb/teams/` for routing...") in system prompt | System prompt is the highest-reliability channel; wasting it on navigation that belongs in operations | Move map to operations guide; system prompt = identity + character + limits only |
| `bin/query-api --extract --output /tmp/log` syntax in identity | Agent sees tool syntax globally → calls tools directly, bypasses skill procedures | Tool syntax only inside skill steps where the procedure controls when/how to call |
| "You are a helpful AI assistant" | Generic; every agent gets the same behavior; no domain grounding | "You investigate CI/CD failures for [system]. You are not an executor — you do not retrigger pipelines." |
