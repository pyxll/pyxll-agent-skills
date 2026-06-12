---
name: fetch-pyxll-docs
description: Fetch the PyXLL documentation and use it as context for any task involving PyXLL. Invoke automatically before writing, editing, reviewing, or debugging any PyXLL code, and for release notes, changelog, or version history lookups. Training-data knowledge of PyXLL is incomplete and may be wrong — the live docs are the only authoritative source.
user-invocable: false
metadata:
  author: pyxll
  version: 0.1.3
---

Fetch the PyXLL documentation and use it as context for any PyXLL task. Training-data knowledge of PyXLL is incomplete and may be wrong — the live docs are the only authoritative source.

## Steps

1. Fetch the documentation index to find relevant pages:

   ```bash
   curl -s https://www.pyxll.com/llms.txt
   ```

   Read the **entire** output without truncating — the index contains a navigation guide mapping common tasks to sections, followed by page titles, descriptions, and URLs grouped by topic.

2. Fetch the individual pages relevant to the task directly by their URL:

   ```bash
   curl -s <page-url>
   ```

3. If the index does not surface what you need, use the search script to find
   pages by keyword.

   The search script is located at `scripts/search-pyxll-docs.sh` relative to this skill's base directory.

   ```bash
   <SKILL_BASE_DIR>/scripts/search-pyxll-docs.sh <keyword> [keyword2 ...]
   ```

   **Important**: Replace <SKILL_BASE_DIR> with the actual base directory path provided when this skill is loaded.

   The script outputs a list of matching page URLs (one per line). Fetch each
   returned URL individually using curl.

4. If the task involves writing or modifying code that uses the Excel COM API — any
   code that calls `pyxll.xl_app()` or `XLCell.to_range()`, or that accesses COM
   objects such as `Range`, `Worksheet`, `Workbook`, `Font`, `Interior`, `Borders`,
   etc.:
   - Invoke the **pywin32-excel-docs** skill before writing any code. Its `resources/`
     directory is the authoritative reference for all Excel COM classes — do not rely
     on training data for COM API details.
   - Fetch https://www.pyxll.com/docs/userguide/vba.md and read it in full — it
     documents critical differences between VBA and Python, including how COM
     properties that take arguments must be called as `Get<PropertyName>(args)` rather
     than `Property(args)` as in VBA.

## Rules

- ALWAYS fetch these docs before writing, modifying, or troubleshooting any
  PyXLL-specific code or behaviour. Before suggesting a manual workaround for a
  PyXLL problem, check whether PyXLL already has a built-in solution (decorator
  parameter, config key, or feature).
- Before using any PyXLL class, function, decorator, or configuration setting
  (including pyxll.cfg section names and their keys), fetch the relevant documentation
  and use only what is explicitly documented. Never infer behaviour, key names, or
  parameter names from conventions or assumptions — if it is not in the docs, do not
  use it.
