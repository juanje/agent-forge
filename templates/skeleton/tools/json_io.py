"""Shared JSON output helpers for agent-facing tools."""

from __future__ import annotations

import json
import sys
import time
from typing import Any

import httpx


def emit_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, indent=2, default=str))


def emit_error(message: str, hint: str | None = None, **extra: Any) -> None:
    payload: dict[str, Any] = {"error": message}
    if hint:
        payload["hint"] = hint
    payload.update(extra)
    print(json.dumps(payload, indent=2))
    sys.exit(1)


def fetch_json(
    url: str,
    headers: dict[str, str] | None = None,
    *,
    retries: int = 3,
    timeout: float = 30.0,
) -> dict[str, Any]:
    """Fetch JSON with internal retry — never expose --timeout to the agent."""
    last_error: str | None = None
    for attempt in range(1, retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers or {})
                response.raise_for_status()
                data = response.json()
                if isinstance(data, dict):
                    return data
                return {"data": data}
        except httpx.HTTPError as exc:
            last_error = str(exc)
            if attempt == retries:
                emit_error(
                    f"Fetch failed after {retries} attempts — {last_error}",
                    hint="Retrying will not help until the service is available.",
                )
            if attempt < retries:
                time.sleep(2 ** (attempt - 1))  # 1s, 2s, 4s...
    emit_error("Unexpected fetch failure")
