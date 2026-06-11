# Excel Table Builder Script

## Problem Description

The reporting team wants a Python automation script that creates and populates a structured Excel Table (the native Excel table feature, not just a range of cells) in a new workbook. They want the table to be properly configured and contain some sample data so it can be used as a template for future reports.

The script should:

1. Create a new workbook and select the first worksheet
2. Write column headers into cells A1:D1 (`Region`, `Product`, `Units`, `Revenue`)
3. Write one sample data row into A2:D2 (e.g. `East`, `Widget`, `100`, `5000`)
4. Convert the range A1:D2 into a formal Excel Table (ListObject) and name it `SalesData`
5. Add a second data row to the table programmatically (not by writing to a range directly — use the table's own row-insertion mechanism)
6. Access the table's data area (excluding the header) and apply bold formatting to it

The script runs as a standalone command-line tool.

## Output Specification

Produce a single Python script named `table_builder.py`. The script should save the workbook to a placeholder path such as `r"C:\reports\sales_template.xlsx"`. Require only `pywin32` and the Python standard library.
