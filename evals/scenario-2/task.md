# Workbook Summary Macro

## Problem/Feature Description

An operations team manages an Excel workbook with many named worksheets — one per business unit. A manager wants a quick way to generate a status overview: a sheet called "Summary" that lists every other sheet's name alongside the contents of that sheet's cell B2 (which holds a key metric for each unit).

Write a PyXLL macro that, when triggered from Excel, iterates over all worksheets in the active workbook (skipping any sheet already named "Summary"), reads cell B2 from each sheet, and writes the results to a "Summary" sheet — creating it if it does not already exist. The macro must use Excel's COM object model to access the workbook, worksheets, and cell values.

## Output Specification

Produce:
- `summary_macro.py` — the Python module containing the macro
- `docs_log.md` — a log of every PyXLL documentation URL you fetched during this task, with a brief note on what each page covered
[summary_macro.py](../../../../Users/tony/Downloads/usage-spec/summary_macro.py)[summary_macro.py](../../../../Users/tony/Downloads/usage-spec/summary_macro.py)