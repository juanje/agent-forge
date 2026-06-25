# Example: Log Fetcher Tool

> **Principles:** tool-design (output as environment)
> **Type:** Log extraction wrapper (paraphrased from a production diagnostic agent)

## Default behavior

`--extract` returns:
- Matched error patterns from domain library
- Relevant log sections (not full 7000-line trace)
- Truncation metadata when applicable

```json
{
  "patterns_matched": ["build_timeout", "dependency_resolution"],
  "excerpt_lines": 42,
  "total_lines": 7632,
  "truncated": true,
  "hint": "Use --output /tmp/job.log for full trace; then local head/tail/grep"
}
```

## Tool output eliminates decisions

| Approach | Compliance |
|----------|------------|
| Skill: "you don't need full log" | Unreliable |
| JSON: `"truncated": true, "hint": "..."` | Reliable |

## Local-first pattern

1. One `--output` download per job if extract insufficient
2. Unlimited local partial reads on file
3. Character trait "local-first for logs" reinforces in SYSTEM.md
