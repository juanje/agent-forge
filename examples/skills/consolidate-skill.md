# Example: Consolidate Skill

> **Principles:** memory-architecture, skill-design (generator/evaluator separation)
> **Type:** Learning cycle procedure (paraphrased from a production diagnostic agent)

## Ordered consolidation (never skip step 1)

```markdown
## Steps

1. Run `bin/compute-stats` → updates kb/history/stats.md (deterministic)
2. Read new incidents in kb/history/ not yet reflected in known-issues/
3. For 2+ incidents sharing mechanism → enrich category index.md generic pattern
4. Create specific files for novel patterns; link from category index
5. Apply actionability filter for lessons/ — only if it changes next investigation
6. `git commit` consolidation batch
```

## Actionability filter

| Goes to lessons/ | Goes to stats.md only |
|------------------|----------------------|
| "When build_stage errors, check tooling versions first" | "Downstream fails 65% more than upstream" |

## Separation from capture

- **capture-findings** — generator, write kb/active/
- **consolidate** — evaluator/promoter, write kb/known-issues/, kb/lessons/
- Different write permissions in permissions.json
