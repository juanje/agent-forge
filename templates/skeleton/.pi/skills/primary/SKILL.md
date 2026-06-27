---
name: {{PRIMARY_SKILL_NAME}}
description: {{PRIMARY_SKILL_DESCRIPTION}} Trigger when {{PRIMARY_SKILL_TRIGGER}}.
---

# {{PRIMARY_SKILL_TITLE}}

## When to use

- "{{EXAMPLE_PHRASE_1}}", "{{EXAMPLE_PHRASE_2}}"
- {{TRIGGER_KEYWORDS}}

## Tools available

| Command | What it does | Key options |
|---------|-------------|-------------|
| `bin/{{TOOL_1}}` | {{DESCRIPTION}} | {{PREFERRED_OPTION}} (preferred); {{FALLBACK_OPTION}} (fallback) |

Do not run `--help`, `ls bin/`, or read tool source — use this table directly.

## Steps

### Step 0: Parse input

Extract {{INPUT_FIELD}} from the user's message:

| User says | Action |
|-----------|--------|
| {{EXAMPLE}} | {{EXTRACTION}} |

### Step 1: {{FIRST_ACTION}}

{{STEP_1_DETAIL}}

### Step 2: {{SECOND_ACTION}}

{{STEP_2_DETAIL}}

### Step 3: {{THIRD_ACTION}}

{{STEP_3_DETAIL}}

### Step 4: Handle tool failures

If a tool fails, treat the error as diagnostic evidence. Do not improvise curl/python workarounds.

### Step 5: Report findings

Report with evidence chain and confidence level.

## Success criteria

- {{SUCCESS_CRITERION_1}}
- {{SUCCESS_CRITERION_2}}

## Gotchas

- {{GOTCHA_1}}
