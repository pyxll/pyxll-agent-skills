# Trade Log Range Navigator

## Problem Description

A quantitative trading desk maintains a daily P&L spreadsheet where trade records are stored on a worksheet called "Trades". Data begins at cell B3 (with column headers in row 3) and extends across 5 columns, with a variable number of data rows below. At the bottom of the data there is a totals row, and one column to the right of the last data column is a summary cell the team calls the "corner total."

The operations team needs a standalone Python script (not a PyXLL add-in — a script run from the command line) that:

1. Opens a workbook at a given file path (hardcode a placeholder path such as `r"C:\data\trades.xlsx"`)
2. Gets the B3 cell as the starting reference point
3. Navigates downward from B3 to find the last occupied cell in column B (the last data row)
4. From that last data cell, computes a range covering all 5 data columns starting from B in the same row down to the last row (i.e., resize from the starting cell to cover 5 columns)
5. Retrieves the address of that full data region as an absolute reference string (e.g., `$B$3:$F$25`) for inclusion in a log message
6. Reads the value of the "corner total" cell, which is 1 row below and 1 column to the right of the last data cell

The script should print the data region address and the corner total value to the console.

## Output Specification

Produce a single Python script file named `trade_log_processor.py`. The script should be complete and runnable (it may reference a placeholder workbook path). Do not require any packages beyond `pywin32` and the Python standard library.
