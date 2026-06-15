# Custom Cell Formatter for Financial Data

## Problem Description

A financial analytics team uses a PyXLL-based Excel add-in to display portfolio data. They want a custom cell formatter that applies background colour highlighting based on the cell's numeric value:

- Values greater than 1000: green background
- Negative values: red background
- All other values: no background colour (cleared)

The formatter should integrate with PyXLL's cell formatting system and apply the colouring directly through the Excel object model.

## Output Specification

Produce:
- `formatter.py` — the custom formatter class, ready to be registered with PyXLL
- `docs_log.md` — every documentation source you consulted (PyXLL docs URLs, skill reference files, etc.), with a one-line note on what each source contributed
