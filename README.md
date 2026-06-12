# PyXLL Agent Skills

A curated collection of [Agent Skills](https://agentskills.io/home) for working with [PyXLL](https://www.pyxll.com), the Python Excel add-in. These skills help AI agents understand and use PyXLL APIs accurately.

## How They Work

These skills are **not** slash commands or user-invoked actions. Once installed, the agent automatically loads the relevant skill when your prompt matches its use case. See [skill invocation control](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill) for more details.

## Installation

### Claude Code

```bash
/plugin marketplace add pyxll/pyxll-agent-skills
```

### Other AI Clients

#### Vercel Skills CLI

Use the [Vercel Skills CLI](https://github.com/vercel-labs/skills) to install skills from this repository. Supports 30+ AI agents including Cursor, Cline, GitHub Copilot, and others.

```bash
# Preview available skills
npx skills add pyxll/pyxll-agent-skills --list

# Install all skills
npx skills add pyxll/pyxll-agent-skills

# Install a specific skill
npx skills add pyxll/pyxll-agent-skills --skill fetch-pyxll-docs

# Install globally (available in all projects)
npx skills add pyxll/pyxll-agent-skills --global

# Check for updates
npx skills check

# Update installed skills
npx skills update
```

#### Tessl

Install skills using [Tessl](https://tessl.io/), a package manager for agent skills:

```bash
# Install all skills
tessl install pyxll/pyxll-agent-skills

# Install from GitHub directly
tessl install github:pyxll/pyxll-agent-skills
```

Browse the tile on the [Tessl registry](https://tessl.io/registry/pyxll/pyxll-agent-skills).

## Available Skills

| Skill | Description |
|-------|-------------|
| `fetch-pyxll-docs` | Fetch the PyXLL documentation and use it as context when writing, reviewing, or debugging PyXLL code |
| `pywin32-excel-docs` | Reference for the Excel COM API via pywin32 — covers workbooks, worksheets, ranges, formatting, charts, pivot tables, shapes, and constants |

## Contributing

To add a new skill, create a directory under `skills/` with a `SKILL.md` file following the [Agent Skills specification](https://agentskills.io/specification), then add it to `.tessl-plugin/plugin.json`.

## Resources

- [PyXLL Documentation](https://www.pyxll.com/docs/)
- [Agent Skills Documentation](https://agentskills.io/home)

## Community

- **Issues**: Report problems or suggest new skills
- **Pull Requests**: Contribute new skills or improvements

## License

See [LICENSE](LICENSE) for details.
