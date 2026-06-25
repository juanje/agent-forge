"""Click CLI group — register subcommands here."""

import click

from tools import example_tool


@click.group()
def main() -> None:
    """Agent tools — JSON output for LLM consumption."""


main.add_command(example_tool.cli, name="example-tool")
