# Customer Data Cleanup Script

## Problem Description

The customer success team manages a CRM export in Excel. The spreadsheet has a "Customers" worksheet with thousands of rows and frequently contains blank cells and duplicates introduced by data-entry errors. Before handing the spreadsheet off to the analytics team, a Python cleanup script needs to run two operations:

**Step 1 — Blank cell fill**: Fill all blank cells within the data range (columns A through E, from row 2 downward to the last occupied row) with the placeholder text `"MISSING"`, then print how many cells were filled.

**Step 2 — Duplicate removal**: Remove rows from the same data range where both the customer ID (column 1) and the email address (column 2) are identical. Rows that differ in at least one of those two fields should be kept. The header row (row 1) should be preserved.

The script runs as a standalone command-line tool (not inside PyXLL).

## Output Specification

Produce a single Python script named `data_cleanup.py`. Use a placeholder workbook path such as `r"C:\crm\customers.xlsx"`. The script should require only `pywin32` and the Python standard library.
