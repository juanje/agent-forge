# Tool Design

## Core Concept

Agent-facing tools are not human CLIs. LLMs can't handle raw authentication, don't validate domains, struggle with unstructured error output, and will retry failed requests with creative workarounds instead of backing off. Good agent tools handle all of this internally: they authenticate, validate, retry with backoff, and return structured JSON with actionable error messages.

The key design insight: **tool output shapes agent behavior more reliably than written instructions.** A truncation header that says "Showing 100 of 7632 lines — use `--output` for full content" guides the agent's next action more effectively than a skill step saying "check if the output is truncated." Design tools to eliminate decisions, not inform them.

**Two modes only** for remote or log data: (1) smart extraction as the default (show the relevant subset with metadata), and (2) raw download to a local file for full content. Avoid middle-ground flags like `--tail`, `--head`, `--limit`, or `--full`. When given partial-read options, agents spend multiple turns sweeping parameter values (`--tail 50`, then `--tail 200`, then `--tail 500`) instead of analyzing the data they already have.

## Design Rules

1. **Opinionated defaults** — Show a useful subset with metadata: `[Showing last 100 of 7632 lines. Use --output for full content.]`

2. **Errors as diagnostic evidence** — `"Fetch failed after 3 attempts — server unavailable. Retrying will not help."` Not raw stack traces or exception dumps.

3. **Graceful degradation** — Return successful data + `warnings` field for partial failures. Don't fail completely when one sub-request out of five breaks.

4. **Auto-detect mode** — Context determines extraction vs download; no redundant flags the agent has to choose between.

5. **Retry internally** — 3+ attempts with backoff; never expose `--timeout` to agent. Bake sensible defaults as constants.

6. **Consistent interface** — Same two-mode pattern across similar tools in the same repo.

7. **Thin wrapper pattern** — Shell script delegates to the real implementation. Keeps the executable simple and permissions clear.

8. **Structured output** — JSON for agent consumption. Centralize output/error helpers in a shared module so all tools produce the same schema.

9. **Output tells next action** — Truncation headers, skip signals with reason, inline metadata that eliminates speculation.

10. **Defense in depth** — Domain allowlist in tool code even when permissions restrict raw HTTP access. Belt and suspenders.

11. **Deny writes to tool source** — Agent should not be able to modify its own tools. Prevents proxy escape via modified allowlisted scripts.

12. **Mutation safety: dry-run default + env-var gate** — Tools that write to external systems (APIs, ticket systems, databases) default to dry-run mode. Require explicit `--apply` flag AND an environment variable gate for destructive operations. Two independent confirmations: env var proves intentional setup, flag proves intentional execution. Read-only tools don't need this.

13. **Shared module for common logic** — Tools in the same repo that share patterns (HTTP client, auth, ID resolution, output formatting) must share a module. Copy-pasted helpers grow inconsistencies and block centralized improvements. Extract early.

## Evaluation Criteria

### Wrappers

- [ ] One-line comment describing purpose
- [ ] Delegates to implementation (no business logic in wrapper)
- [ ] Executable permissions set

### Tool implementations

- [ ] Structured output (JSON or equivalent) for agent consumption
- [ ] Errors use structured format with actionable message (no bare stack traces)
- [ ] Remote data: extraction mode default; download for full content
- [ ] No `--tail`/`--head`/`--limit`/`--timeout` exposed to agent
- [ ] Internal retry (3x+) for transient failures
- [ ] Truncation/summary headers when output is partial
- [ ] Domain validation for HTTP tools (allowlisted hosts)
- [ ] Consistent interface structure across tools in same repo

### Mutation tools

- [ ] Dry-run default (no writes without explicit flag)
- [ ] Environment variable gate for destructive operations
- [ ] Dry-run output shows what WOULD happen (agent can review before executing)

### Shared module

- [ ] Common HTTP client, auth, ID resolution in shared module (not copy-pasted)
- [ ] Output and error helpers centralized
- [ ] Retry logic consistent across all tools (one implementation)

### Skill integration

- [ ] Tool flags documented in skills (WHY order matters), not in identity/system prompt
- [ ] Skills teach the efficiency order: pattern match → extract → download → local analysis

## Good Examples

Thin wrapper:
```bash
#!/usr/bin/env bash
# bin/query-api — Query domain API; structured JSON output
exec uv run tools query-api "$@"
```

Structured error:
```python
def emit_error(message: str, hint: str | None = None) -> None:
    payload = {"error": message}
    if hint:
        payload["hint"] = hint
    print(json.dumps(payload))
    sys.exit(1)
```

Truncation metadata:
```json
{"truncated": true, "shown_lines": 100, "total_lines": 7632, "hint": "Use --output /tmp/full.log for complete content"}
```

Mutation safety (dry-run + env gate):
```bash
# Without env var — aborts
$ bin/apply-changes
Error: MY_AGENT_APPLY not set. Set to '1' to enable.

# With env var, without --apply — dry-run
$ MY_AGENT_APPLY=1 bin/apply-changes --target 12345
[DRY RUN] Would apply 47 changes to target 12345. Use --apply to execute.

# Full execution
$ MY_AGENT_APPLY=1 bin/apply-changes --target 12345 --apply
Applied 47 changes to target 12345.
```

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| `--tail 100` flag on a log-fetching tool | Agent experiments: `--tail 50`, `--tail 200`, `--tail 500` — wasting 4 calls to find the right number | Default shows last 100 + header saying "7632 total, use --output for full"; agent decides once |
| `requests.exceptions.ConnectionError: HTTPSConnectionPool(host=...)` printed to stdout | Agent sees raw Python exception → tries `curl` or `wget` workaround | `{"error": "Fetch failed after 3 attempts — server unavailable", "hint": "Retrying will not help."}` |
| Skill step: `curl -H "Authorization: Bearer $TOKEN" https://api.example.com/data` | Token handling, SSL, retry, error formatting all on the agent; one wrong header = leaked credential | Wrapper handles auth from env, validates domain, retries, returns JSON |
| Tool with `--extract`, `--summary`, `--brief`, `--full`, `--raw`, `--json` flags | Agent explores combinations; 6 flags = 64 possible states | Two modes only: default extraction + `--output /tmp/file` for full download |
| Tool A writes result to global variable; Tool B reads it | Each tool call is a new process; no shared state | Return state in JSON output; next tool call gets it as input |
| `bin/deploy --target prod` runs immediately with no confirmation | One wrong invocation = production change | `--apply` flag + `AGENT_DEPLOY=1` env var; without both, tool shows what WOULD happen |
| `_http_get()` function copy-pasted in 12 files, retry count drifting (3 vs 5 vs 8) | Bug fix requires editing 12 files; inconsistencies grow silently | `from tools.shared import http_get` — one implementation, one place to fix |
