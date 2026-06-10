---
name: fetch-pyxll-docs
description: Fetch the PyXLL documentation and use it as context for any task involving PyXLL. Invoke automatically before writing, editing, reviewing, or debugging any PyXLL code, and for release notes, changelog, or version history lookups. Training-data knowledge of PyXLL is incomplete and may be wrong — the live docs are the only authoritative source.
user-invocable: false
metadata:
  author: pyxll
  version: 0.1.0
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

   The script is in the `scripts/` folder next to this file. Find this file's
   location and run:

   ```bash
   /path/to/this/skills/fetch-pyxll-docs/scripts/search-pyxll-docs.sh <keyword> [keyword2 ...]
   ```

   The script outputs a list of matching page URLs (one per line). Fetch each
   returned URL individually using curl.

## Rules

- ALWAYS fetch these docs before writing, modifying, or troubleshooting any
  PyXLL-specific code or behaviour. Before suggesting a manual workaround for a
  PyXLL problem, check whether PyXLL already has a built-in solution (decorator
  parameter, config key, or feature).
- Do NOT rely on training-data knowledge alone for PyXLL APIs — the docs are authoritative.
- Before writing any code that calls the Excel COM API (Range, Worksheet, Workbook, etc.),
  fetch https://www.pyxll.com/docs/userguide/vba.md and read it in full. It documents
  critical differences between VBA and Python — including how COM properties that take
  arguments must be called as `Get<PropertyName>(args)` in Python rather than
  `Property(args)` as in VBA.
- Before using any PyXLL class, function, decorator, or configuration setting
  (including pyxll.cfg section names and their keys), fetch the relevant documentation
  and use only what is explicitly documented. Never infer behaviour, key names, or
  parameter names from conventions or assumptions — if it is not in the docs, do not
  use it.
