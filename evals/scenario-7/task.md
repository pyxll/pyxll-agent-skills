# Range Data Validation Script

## Problem Description

A data-entry spreadsheet needs to restrict what users can type into a specific range of cells. The operations team wants a Python script that opens an existing workbook and applies input validation to the range B2:B20 on the first worksheet, configured so that only whole numbers between 1 and 100 are accepted. Any out-of-range entry should show a warning alert but still allow the user to proceed.

The script runs as a standalone command-line tool (not inside PyXLL).

## Output Specification

Produce two files:

**`add_validation.py`** — the Python script. Use a placeholder workbook path such as `r"C:\data\entry.xlsx"`. Require only `pywin32` and the Python standard library.

**`files_read.md`** — a plain list of every file from the pywin32-excel-docs `resources/` directory that you opened and read while writing this script. One file path per line, exactly as it appears in the resources directory (e.g. `resources/index.md`). Include every file you actually read, in the order you read them.
