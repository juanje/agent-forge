"""Example tool — replace with domain API integration."""

from __future__ import annotations

import json
import os
from urllib.parse import urlparse

import click

from tools.json_io import emit_error, emit_json, fetch_json

ALLOWED_DOMAINS = ["api.example.com"]  # {{ALLOWED_DOMAINS}}
DEFAULT_EXTRACT_LIMIT = 50


def validate_url(url: str) -> None:
    host = urlparse(url).hostname
    if host not in ALLOWED_DOMAINS:
        emit_error(
            f"Domain '{host}' not in allowlist",
            hint=f"Allowed: {', '.join(ALLOWED_DOMAINS)}",
        )


@click.command("example-tool")
@click.argument("resource_id")
@click.option("--output", type=click.Path(), help="Download full response to file.")
def cli(resource_id: str, output: str | None) -> None:
    """Fetch data for RESOURCE_ID. Default: structured summary. --output FILE: full download."""
    base_url = os.environ.get("API_BASE_URL")
    token = os.environ.get("API_TOKEN")
    if not base_url or not token:
        emit_error(
            "Missing API_BASE_URL or API_TOKEN in environment",
            hint="Copy .env.example to .env and set credentials",
        )

    url = f"{base_url.rstrip('/')}/resources/{resource_id}"
    validate_url(url)
    data = fetch_json(url, headers={"Authorization": f"Bearer {token}"})

    if output:
        with open(output, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)
        emit_json(
            {
                "saved_to": output,
                "hint": "Use local shell tools on the file for partial reads",
            }
        )
        return

    items = data.get("items", [])
    if not isinstance(items, list):
        items = []
    shown = items[:DEFAULT_EXTRACT_LIMIT]
    summary: dict[str, object] = {
        "resource_id": resource_id,
        "status": data.get("status", "unknown"),
        "items": shown,
        "shown": len(shown),
        "total": len(items),
        "truncated": len(items) > len(shown),
    }
    if summary["truncated"]:
        summary["hint"] = (
            f"Showing {len(shown)} of {len(items)}. Use --output for full content."
        )
    emit_json(summary)


if __name__ == "__main__":
    cli()
