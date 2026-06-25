# Example: Diagnostic Skill

> **Principles:** skill-design, memory-architecture (verify-first)
> **Type:** Core diagnostic procedure (paraphrased from a production CI/CD agent)

## Key structural elements

### Disconfirmation gate (Step 4 pattern)

```markdown
4. **Disconfirmation gate:** If a known-issue matches, list what evidence
   would contradict this hypothesis. Search for that evidence before reporting
   the known issue as root cause.
```

*Prevents reporting resolved issues as current failures.*

### Depth obligation

```markdown
3. For each failed job, run `bin/fetch-log --extract <job>`.
   A KB match does NOT exempt you from reading job-level evidence.
```

*KB match ≠ shallow investigation.*

### Efficiency order (WHY in skill)

```markdown
Order: pattern match in extract output → full --extract → --output then local grep.
Smart extraction covers ~80% of cases; download is fallback.
```

*Tool-design principle 6 — WHY in skill, not flag list.*

## Success criteria (good)

```markdown
## Success criteria

- Root cause stated with evidence chain (log line, API field, or artifact)
- Confidence level explicit when evidence is partial
- Escalation path if outside agent scope (read escalation-routing.md)
```

## Anti-pattern avoided

- Status skill and diagnose skill both fetching same pipeline metadata → eliminated redundant API calls (0% overlap post-fix)
