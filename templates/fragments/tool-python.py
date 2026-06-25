# Python Tool Template
#
# Reference: docs/principles/tool-design.md
# Two modes: default (structured summary) and --output (full download).

```python
ALLOWED_DOMAINS = ["api.example.com"]  # {{ALLOWED_DOMAINS}}

def validate_url(url: str) -> None:
    from urllib.parse import urlparse
    host = urlparse(url).hostname
    if host not in ALLOWED_DOMAINS:
        emit_error(
            f"Domain '{host}' not in allowlist",
            hint=f"Allowed: {', '.join(ALLOWED_DOMAINS)}",
        )

@click.command("{{TOOL_CLI_NAME}}")
@click.argument("id")
@click.option("--output", type=click.Path())
def cli(id, output):
    # 1. Validate env / auth
    # 2. validate_url(url) before fetch
    # 3. fetch_json(url, headers=...) from tools/json_io — internal retry, no --timeout
    # 4. --output → save file + emit_json({saved_to, hint})
    # 5. default → emit_json(summary) with truncation metadata:
    #    {"shown": N, "total": M, "truncated": true, "hint": "Use --output for full content"}
    # 6. emit_error(message, hint=) on terminal failure


if __name__ == "__main__":
    cli()
```

Use `tools/json_io.py` for emit_json, emit_error, and fetch_json.

The `bin/` wrapper routes through the installed entry point (`exec uv run tools {{TOOL_CLI_NAME}} "$@"`),
so the `@click.command("{{TOOL_CLI_NAME}}")` name must match what's registered in `cli.py`.
