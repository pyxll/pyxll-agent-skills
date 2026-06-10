# PyXLL Agent Skills — Developer Notes

This repo publishes Claude Code agent skills for working with PyXLL.

## Structure

```
skills/pyxll/          # PyXLL skill category
  fetch-pyxll-docs/    # One directory per skill
    SKILL.md           # Skill definition (required)
    scripts/           # Helper scripts referenced by the skill
```

## Adding a skill

1. Create `skills/pyxll/<skill-name>/SKILL.md` with the required frontmatter (`name`, `description`, `user-invocable`, `metadata.author`)
2. Add an entry to `tile.json` under `"skills"`
3. Update `README.md` to document the new skill

## Plugin manifest

- `tile.json` — top-level plugin metadata and skill path index
- `.claude-plugin/marketplace.json` — Claude Code marketplace entry (enables `/plugin marketplace add pyxll/pyxll-agent-skills`)
