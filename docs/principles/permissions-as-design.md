# Permissions as Design

## Core Concept

Permissions serve **dual purpose**: security (secrets, destructive ops, self-modification) and **behavior design** — restrict tools that invite improvisation; channel the agent toward designed paths (skills, wrapped tools, structured navigation).

Think of permissions as **constraints that shape capability**, not just walls that block it. An agent that can't use `grep` navigates via indexes instead — a better pattern, enforced mechanically.

Different harnesses implement permissions differently (config files, settings UI, hook scripts, rule files), but the principles are the same.

## Design Rules

1. **Deny-by-default** — Start from "nothing allowed" and explicitly permit what the agent needs. Safer than allowlisting retroactively.

2. **Restrict raw system access** (restrictive agents) — Deny direct `curl`, `wget`, `python`, `pip`, `rm`, `sudo`. Force all external access through wrapped tools that handle auth, validation, and structured output.

3. **Consider hiding exploration tools** (restrictive agents) — Denying `grep`/`find`/`ls` forces the agent to navigate via indexes and skill steps. More structured, prevents ad-hoc browsing.

4. **Path-based write rules** — Enforce the four-store boundaries mechanically. The agent should be unable to write to read-only stores regardless of what instructions say.

5. **Protect secrets in read rules** — `.env`, credentials, SSH keys denied even if read is generally allowed.

6. **Self-protection** — Agent cannot modify its own permission config, tools, or wrapper scripts.

7. **Deny writes to tool source** — Prevents proxy escape: agent modifies an allowed tool to do something the permission system would otherwise block.

8. **Skill-permission parity** — Tool access declared in skill metadata must match what the permission system actually allows. Keep both in sync; verify during reviews.

9. **Defense in depth** — Domain allowlist inside HTTP tools as a second layer, even when bash is restricted.

10. **Audit trail** — Log permission decisions (allow/deny with tool, input, reason) for compliance and debugging.

## Agent Archetypes

| Aspect | Diagnostic (restrictive) | Productivity (permissive) |
|--------|--------------------------|---------------------------|
| Write default | Deny except knowledge paths | Allow workspace |
| System commands | Wrapped tools only | Scoped allowlist |
| Exploration tools | Hidden (forces index navigation) | Allowed (identity handles navigation) |
| Focus | Knowledge integrity, no improvisation | Secrets, self-protection |

Choose the archetype that matches your agent's failure cost. Diagnostic agents where wrong answers are trusted need restrictive permissions. Productivity agents where humans review output can be more permissive.

## Evaluation Criteria

- [ ] Deny-by-default policy (or documented intentional permissive variant with rationale)
- [ ] Raw system access restricted; wrapped tools allowed
- [ ] Write paths match four-store knowledge model
- [ ] Read-only knowledge paths in write deny
- [ ] Active knowledge writable; history not writable by agent
- [ ] Secrets (.env, credentials) denied in read rules
- [ ] Tool/wrapper source in write deny
- [ ] Skill-permission parity verified
- [ ] Harness-appropriate implementation (config file, settings, rules, hooks — depends on runtime)

## Good Examples

Restrictive agent permission policy (conceptual — adapt syntax to your harness):

```
Default: deny all

Read: allow (except .env, credentials, SSH keys)
Write: deny (except active knowledge, scratch, tmp)
System commands: deny (except wrapped tools, scoped git operations)
Exploration: deny grep/find/ls (force index navigation)
```

## Bad Examples → Fix

| Bad | Why it fails | Fix |
|-----|-------------|-----|
| Skill says "move record to history" but permission system blocks the file move | Agent tries, gets denied, wastes a turn, may try a workaround (copy+delete) | Paired-update: when adding capability to a skill, add the matching permission rule at the same time |
| Deny `cat *` to protect sensitive files | Also blocks reading ordinary knowledge base files; agent can't follow its own procedures | Specific denies: `cat .env*`, `cat ~/.ssh/*` — not wildcard on all files |
| Skill metadata lists "can use git, curl, python" but no enforcement in permission system | Metadata is advisory only; agent can call anything the harness allows | Enforce in permission config; metadata documents intent but config enforces it |
| Agent can edit `tools/query.py` (its own tool source) | Agent modifies a tool to bypass restrictions or add unauthorized capabilities (proxy escape) | Deny write on all tool/wrapper paths in permission system |
| Permissive "allow everything" policy on a diagnostic agent whose output is trusted | Wrong diagnosis accepted without human review; agent improvises with raw tools, hits APIs without validation | Use restrictive archetype: wrapped tools only, scoped writes, hidden exploration tools |
