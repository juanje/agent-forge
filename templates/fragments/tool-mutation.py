# Mutation Tool Template
#
# Reference: docs/principles/tool-design.md Design Rule #12
# Dry-run default + env-var gate for tools that write to external systems.

```python
import os

import click

from tools.json_io import emit_error, emit_json

ENV_GATE = "{{AGENT_NAME}}_APPLY"


@click.command()
@click.argument("target_id")
@click.option("--apply", is_flag=True, help="Execute changes (default: dry-run).")
def cli(target_id: str, apply: bool) -> None:
    # 1. Check env gate
    if not os.environ.get(ENV_GATE):
        emit_error(
            f"{ENV_GATE} not set",
            hint=f"Set {ENV_GATE}=1 to enable mutations.",
        )

    # 2. Compute changes (same code path for dry-run and apply)
    changes = compute_changes(target_id)

    # 3. Dry-run: show what WOULD happen
    if not apply:
        emit_json({
            "dry_run": True,
            "changes": changes,
            "hint": f"Use --apply to execute {len(changes)} changes.",
        })
        return

    # 4. Apply: execute and report
    results = execute_changes(changes)
    emit_json({"applied": len(results), "results": results})
```
