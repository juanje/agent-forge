# Example: API Query Tool

> **Principles:** tool-design
> **Type:** API query wrapper (paraphrased from a production diagnostic agent)

## Wrapper

```bash
#!/usr/bin/env bash
# bin/query-api — Query external API; structured JSON for agent
exec uv run tools query-api "$@"
```

## Two modes

| Mode | Flag | Output |
|------|------|--------|
| Smart extraction | default / `--extract` | Focused JSON (status, failed items, IDs) |
| Raw download | `--output /tmp/response.json` | Full response saved; JSON confirms path + hint |

## Removed flags (anti-patterns)

- ~~`--tail 100`~~ → default truncation header in extract mode
- ~~`--limit 500`~~ → agent invented values; removed
- ~~`--timeout 60`~~ → internal retry only

## Error output

```json
{
  "error": "Fetch failed after 3 attempts — API unavailable",
  "hint": "Retrying will not help until service recovers."
}
```

## Defense in depth

`validate_url()` allowlists known API domains — even if raw HTTP access were possible, the tool rejects unknown hosts.
