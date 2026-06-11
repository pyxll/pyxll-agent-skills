# Monthly Report Formatter

## Problem Description

The finance team produces a monthly summary report as an Excel workbook and needs consistent, professional formatting applied automatically before it is distributed to stakeholders. The report has a fixed layout: row 1 is a title merged across all columns, rows 2–3 contain column headers, and rows 4 onward contain data.

A Python script needs to open an existing workbook, apply the following formatting, and save it:

1. Center the horizontal alignment of the header rows (rows 2–3)
2. Apply a continuous border around the outside of the entire data range (rows 4 to the last data row)
3. Set the header rows' background fill to a medium blue color using an RGB hex value (`0x4472C4`)
4. Set the header text to bold and white (`0xFFFFFF`)
5. Save the workbook in the modern Excel format (not the legacy `.xls` binary format)

The team uses the script on multiple machines running different Excel versions, and they have had bugs in the past when integer constants were hard-coded and produced unexpected behaviour after an Office update. Write the script so it is robust to version differences.

## Output Specification

Produce a standalone Python script named `format_report.py`. Use a placeholder workbook path such as `r"C:\reports\monthly.xlsx"`. The script should require only `pywin32` and the Python standard library.
