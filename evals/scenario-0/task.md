# Implement Excel Functions for a Financial Analytics Add-in

## Problem/Feature Description

A financial analytics team uses a PyXLL-based Excel add-in to expose Python calculations directly in their spreadsheets. They need to add two new worksheet functions to their existing add-in:

1. A function called `portfolio_vol` that accepts a 2D range of returns (rows = observations, columns = assets) and a 1D range of weights, and returns the portfolio volatility as a single float.
2. A function called `compound_return` that accepts an annual rate (float) and a number of compounding periods (integer), and returns the compound return factor.

The team uses Python 3.10+ and numpy for numeric work. PyXLL is already installed and configured — the only deliverable is a new Python module to be loaded by the add-in.

## Output Specification

Produce:
- `analytics.py` — the Python module containing both functions, ready to be loaded by PyXLL
- `docs_consulted.md` — a markdown file listing every PyXLL documentation URL you fetched, with a one-line note on what each page contributed to your implementation decisions
