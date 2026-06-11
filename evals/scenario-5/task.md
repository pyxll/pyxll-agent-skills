# PyXLL Add-In Utilities Module

## Problem Description

A small team of analysts uses PyXLL to run Python functions directly inside Excel. They want to add two utilities to their PyXLL add-in module:

**Utility 1 — Active Sheet Name function**: A worksheet function (callable from a cell formula like `=ActiveSheetName()`) that returns the name of the currently active worksheet. It takes no arguments and should update automatically when recalculated.

**Utility 2 — Load CSV menu action**: A menu item under a custom ribbon or right-click menu that, when triggered, opens a file-open dialog for the user to pick a CSV file, reads it using Python's `csv` module, and writes its contents (row by row) into the active worksheet starting at cell A1. The menu action does not need to return a value.

Both utilities need access to the live Excel Application object to read or write worksheet data.

## Output Specification

Produce a single Python module file named `workbook_helpers.py` containing both functions decorated appropriately for PyXLL. The file should be self-contained, requiring only `pyxll`, `win32com`, and the Python standard library.
