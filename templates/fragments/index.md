# Template Fragments

Annotated component templates. Read one file at a time when generating or improving that component.

| File | Read when |
|------|-----------|
| [agents-md.md](agents-md.md) | Generating AGENTS.md or operations guide |
| [index-md.md](index-md.md) | Creating kb/ directory index.md files |
| [permissions.json](permissions.json) | Generating permissions.json for Pi or as reference for Claude Code settings |
| [skill.md](skill.md) | Creating skills from procedures |
| [system-prompt.md](system-prompt.md) | Generating SYSTEM.md or CLAUDE.md identity section |
| [tool-python.py](tool-python.py) | Creating read-only extraction tools (two modes: extract + --output) |
| [tool-mutation.py](tool-mutation.py) | Creating mutation tools (dry-run default + env-var gate) |
| [tool-wrapper.sh](tool-wrapper.sh) | Creating bin/ shell wrappers |

Do not read all fragments at session start — load on demand when the bootstrap or populate step requires that component.
