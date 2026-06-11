# Cell-Below Setter Macro

## Problem Description

A team is building an internal PyXLL-powered spreadsheet toolkit and needs a small utility macro for data-entry workflows. When a user selects a cell and triggers the macro from the ribbon or a right-click menu, it should stamp the text `"DONE"` into the cell immediately below the currently active cell, leaving the active cell itself unchanged.

The macro does not accept arguments and does not return a value — it is a pure side-effecting action on the workbook.

## Output Specification

Produce two files:

**`set_below.py`** — a Python module containing the macro, ready to be loaded by PyXLL. It should require only `pyxll` and `pywin32`.

**`docs_consulted.md`** — a short record of the documentation you read before writing the code. For each source, note the URL or file path and a one-line summary of what it told you that was relevant. Include every source you actually consulted.
