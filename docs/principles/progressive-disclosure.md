# Progressive Disclosure

## Core Concept

Don't front-load the entire knowledge base. Use **three layers**: (1) always visible identity + navigation map (~500 lines max), (2) on-demand skills and active context, (3) deep knowledge base via index files. Progressive disclosure **is** the retrieval mechanism — like Wikipedia navigation, not torn-page RAG.

**Layer 1 is the product.** A great entry point with 50 files beats a mediocre one with 1000 files behind it.

When the agent can't browse the filesystem freely (restrictive permissions or large repos), **every directory needs an index file**. Missing indexes break the navigation chain.

## Design Rules

1. **Index entry format** — Each entry: **What** (noun phrase) + **When** (trigger: "Read when...").

2. **Read indexes first** — Operations guide and skills state: read the index before diving into specific files.

3. **Frequency ordering** — List most-common-first in indexes; position = priority.

4. **Hierarchical hubs** — Every knowledge base subdirectory with content has its own index.

5. **No preload** — Operations guide says "do not preload" deep knowledge; load on trigger or skill step.

6. **Functional links** — Cross-reference from multiple contexts (skills, operations, parent indexes).

7. **Lean paths in maps** — Agent-facing references use paths + triggers, not verbose prose.

## Evaluation Criteria

### Operations / navigation map

- [ ] Every listed path has what + when trigger
- [ ] Entries are operational (change what agent reads), not descriptive
- [ ] Indexes listed before leaf files where hierarchy exists
- [ ] "Read indexes first" instruction present

### Knowledge base structure

- [ ] Every directory with content has an index file
- [ ] Child indexes linked from parent indexes
- [ ] No orphan directories (content without index)
- [ ] Read-only vs mutable stores distinguishable in map

### Index files

- [ ] Entries ordered by frequency or importance where known
- [ ] Each entry: path, what, when trigger
- [ ] No "this folder contains..." without a when clause

## Good Examples

```markdown
# Known Issues

Read this index when a failure looks familiar. Then open the matching category.

- `build/index.md` — Compile, dependency, package failures. Read when job log shows build-stage errors.
- `infrastructure/index.md` — Service outages, network issues. Read when multiple unrelated jobs fail simultaneously.
- `testing/index.md` — Test framework issues, false negatives. Read when tests fail but build succeeded.
```

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| `kb/errors/` directory with 20 files, no index | Agent can't browse (permissions deny `ls`); no way to discover what's inside or when to read | Add `kb/errors/index.md` listing each file with what + when trigger |
| Index entry: "Documentation for the build system" | Descriptive, not operational — doesn't tell agent WHEN to open | "Read when a build-stage failure needs architecture context" |
| Operations guide lists 50 individual files the agent might need | Layer 1 bloated; every file competes for attention; agent preloads or ignores all | List 5-6 index files only; leaf files discovered via index navigation |
| `[Error Classification Guide](kb/errors/classification.md)` in agent-facing map | Full markdown link wastes tokens; verbose for a path the agent reads programmatically | `kb/errors/classification.md` — Error type definitions. Read when classifying a failure. |
