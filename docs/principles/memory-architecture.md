# Memory Architecture

## Core Concept

For knowledge bases in the hundreds to low thousands of entries, file-based memory with progressive disclosure outperforms vector RAG. The reason: RAG retrieval returns disconnected chunks that the model must piece together without context. File-based navigation works like Wikipedia — the agent follows links from indexes to full documents, accumulating context as it reads rather than assembling fragments. No vector database or embedding infrastructure needed; markdown files, index files with triggers, and a clear directory structure form the complete retrieval system.

Separate knowledge by **who writes** and **drift risk** — the #1 failure mode is the agent rewriting its own knowledge, with small errors compounding over time.

## Four Stores

| Store | Purpose | Who writes | Mutability |
|-------|---------|------------|------------|
| 1 — Read-only reference | Domain documentation | Developer | No agent writes |
| 2a — Episodic active | What's happening now | Agent | Write-once; no edit after initial write |
| 2b — Episodic history | What happened (closed) | Agent | Immutable after close |
| 3 — Semantic | Patterns and lessons learned | Agent | Consolidation skill only (not mid-task) |
| 4 — Computed | Statistics and metrics | Script | Never LLM-computed |

Plus an observations scratch pad for candidate learnings (append during work, promote during consolidation).

## Design Rules

1. **Episodic write-once** — Never rewrite active records; append follow-up sections. Close by moving to history (immutable).

2. **Hierarchical semantic knowledge** — Category indexes + specific files; enrich generics when patterns recur, never delete specifics.

3. **Consolidation order** — (1) compute stats via script, (2) incidents → known patterns, (3) stats → lessons. Always script-first for deterministic data.

4. **Actionability filter for lessons** — "Does this change what the agent does next?" Interesting-but-inert statistics go to Store 4, not lessons.

5. **Verify-first framing** — Known patterns guide investigation; they don't replace it. A wrong pattern match costs time, not correctness.

6. **Trust levels** — Developer-introduced patterns (direct action, trusted) vs agent-learned patterns (verify-first hypothesis, earned trust through evidence).

7. **Enforce via permissions** — Path-based write rules in the permission system, not just instructions in prose. The agent should be mechanically unable to write to read-only stores.

8. **Every store directory has an index** — Progressive disclosure into each store. Without indexes, the agent can't navigate.

## Evaluation Criteria

- [ ] Four stores identifiable in directory structure (or documented plan for later phases)
- [ ] Read-only paths denied in permission system write rules
- [ ] Active store writable; history store not writable by agent
- [ ] Semantic paths writable only where consolidation skill needs
- [ ] Observations scratch pad appendable if used
- [ ] Index file in every content directory
- [ ] Episodic template or skill defines write-once + close-to-history workflow
- [ ] No flat patterns file rewritten incrementally (use hierarchy instead)
- [ ] Statistics computed by script, not by LLM
- [ ] Operations guide maps each store with triggers

## Good Examples

Closing an episodic record (move, don't edit):
```bash
git mv kb/active/2026-06-18_timeout-issue.md kb/history/incidents/
```

Append follow-up (not rewrite):
```markdown
## Diagnosis (2026-06-10)
Root cause: service timeout. Resolution: unknown.

## Follow-up (2026-06-12)
Resolution: infra team fixed broker. Service green since Jun 11.
```

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| Agent edits a closed incident record to "fix a typo" | Breaks immutability contract; other records may reference the original text; drift accumulates | Permission system denies write on history paths; corrections go as new follow-up entries |
| Single `patterns.md` file where agent appends every new pattern | File grows to 500 lines; agent rewrites while adding; small errors compound over months | Hierarchical directory: category indexes + individual pattern files; enrich generic, never merge specifics |
| Agent writes "65% of failures are timeout-related" to lessons | LLM-computed statistics are plausible but often wrong; future sessions trust the number | Script computes stats deterministically from structured data; apply actionability filter ("does this change what I do?") |
| Knowledge base has perfect directory structure but zero content files | Empty schema creates no gravity; agent has nothing to match against; skills that read KB find nothing | Bootstrap with real reference docs first — even 5 real documents beat 50 empty directories |
| Known-issue matches → agent reports it immediately without checking current evidence | The issue may have been resolved; symptoms may look similar but differ; false match = wrong diagnosis | Verify-first framing: known patterns are hypotheses, not conclusions; disconfirmation gate in diagnostic skills |
