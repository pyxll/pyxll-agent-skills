---
name: pywin32-excel-docs
description: Reference for the Microsoft Excel COM API via pywin32. Use this skill whenever writing or reviewing Python code that interacts with Excel using the Excel COM API via win32com, pywin32, or the PyXLL add-in — including code that calls pyxll.xl_app() or XLCell.to_range() — and when working with workbooks, worksheets, ranges, formatting, charts, pivot tables, shapes, and Excel constants.
user-invocable: false
metadata:
  author: pyxll
  version: 0.1.4
---

# Excel COM API Reference Skill

This skill provides an API reference for Microsoft Excel COM objects accessed via `pywin32`.
It is primarily intended for use with the **PyXLL** Excel add-in, but applies equally to any
Python code that drives Excel via COM.

---

## Prerequisite: PyXLL Code

> **BEFORE writing any code that uses a PyXLL decorator, function, or config key
> (`@xl_func`, `@xl_menu`, `@xl_macro`, `xl_app`, `pyxll.cfg`, etc.) — invoke the
> `fetch-pyxll-docs` skill using the Skill tool. Do this before writing any code.**
> PyXLL APIs are not covered by this skill; the live docs are the only authoritative source.

---

## Rules for AI Agents

> **These rules are mandatory. Follow them before writing any Excel COM code.**

1. **Always read the relevant reference file before using any Excel COM class.** Do not rely
   on training-data knowledge of the Excel COM API — method signatures, parameter names, and
   property types must be verified from the `resources/` docs. The API is large and easy to
   misremember.

2. **Before using any class**, look it up in `resources/index.md` to find which file covers
   it, then read its section in that file. At minimum, check: which members are properties vs
   methods vs property accessors, and what the parameter names and types are.

3. **Never guess a method or property name.** If you cannot find a member in the docs, say so
   rather than inventing one. COM errors from wrong names surface only at runtime.

4. **Property accessors (`GetX` / `SetX`) must be called as methods**, not accessed as
   attributes. They appear under "Property Accessors" in the docs. Example:
   `rng.GetOffset(1, 0)` — NOT `rng.Offset`.

5. **Always use `win32com.client.constants.<name>` for enum/constant values.** Never use bare
   integer literals for constants. The constant name (e.g. `xlCenter`) is the authoritative
   identifier; its integer value can change across Excel versions. The integer values in
   `resources/enums_xl.md` are for reference only — use the named constant, not the number.

6. **Use `pyxll.xl_app()` to get the Application object when running inside Excel via PyXLL.**
   Only use `win32com.client.Dispatch("Excel.Application")` in external scripts.

7. **Parameters marked `?` are optional.** Required parameters have no `?` suffix. Do not
   omit required parameters.

8. **Always check `resources/index.md`** to locate any class — it lists every class and
   the file that documents it.

9. **When operating on cells by category** (blanks, formulas, constants, errors, etc.),
   use `SpecialCells(Type)` to select them rather than reading the full range value and
   filtering in Python. Example: `rng.SpecialCells(c.xlCellTypeBlanks)` selects all blank
   cells in one call. Python iteration over range values is slower and bypasses the COM
   object model.


---

## Getting the Application Object

**With PyXLL** (running inside Excel): use `pyxll.xl_app()` to get the `Application` object
for the current running Excel instance:

```python
from pyxll import xl_app
import win32com.client

app = xl_app()          # returns the live Excel Application
c = win32com.client.constants
```

**Without PyXLL** (external script): use `win32com.client.Dispatch`:

```python
import win32com.client

app = win32com.client.Dispatch("Excel.Application")
c = win32com.client.constants
```

Do **not** use `win32com.client.gencache.EnsureDispatch` — use `Dispatch` only.

Everything below `app` in the object hierarchy is identical in both cases.

## API Reference Files

The `resources/` directory contains machine-readable reference docs:

| File | Contents |
|------|----------|
| [resources/index.md](resources/index.md) | Overview, object hierarchy, quick reference table |
| [resources/application.md](resources/application.md) | `Application`, `_Application`, `WorksheetFunction`, and app-level helpers |
| [resources/workbook.md](resources/workbook.md) | `Workbook`, `Workbooks`, connections, scenarios, protection |
| [resources/worksheet.md](resources/worksheet.md) | `Worksheet`, `Worksheets`, `PageSetup`, `AutoFilter`, `Sort` |
| [resources/range.md](resources/range.md) | `Range`, `Areas`, `Name`, `Names`, `Hyperlink`, `Comment`, `Validation` |
| [resources/formatting.md](resources/formatting.md) | `Font`, `Interior`, `Border`, `Borders`, `Style`, conditional formatting |
| [resources/charts.md](resources/charts.md) | `Chart`, `ChartObject`, `Axis`, `Series`, `Legend`, plot elements |
| [resources/pivot.md](resources/pivot.md) | `PivotTable`, `PivotField`, `PivotItem`, `PivotCache`, slicers |
| [resources/shapes.md](resources/shapes.md) | `Shape`, `Shapes`, fill/line/shadow formats, OLE objects, sparklines |
| [resources/tables.md](resources/tables.md) | `ListObject`, `ListColumn`, `ListRow`, query tables, connections |
| [resources/model.md](resources/model.md) | Data Model: `Model`, relationships, measures, tables |
| [resources/window.md](resources/window.md) | `Window`, `Pane`, protected view windows |
| [resources/addins.md](resources/addins.md) | Add-ins, dialogs, legacy menus/toolbars |
| [resources/enums_xl.md](resources/enums_xl.md) | All `Xl*` enumeration constants with integer values |

## Key Conventions

- **Properties** — accessed as attributes: `ws.Name`, `rng.Value`, `rng.Font.Bold`
- **Methods** — called normally: `rng.Clear()`, `ws.Copy()`, `app.Calculate()`
- **Property Accessors** — parameterized properties that *must* be called as methods:
  `rng.GetOffset(1, 0)`, `rng.GetAddress(False, False)`, `rng.GetResize(3, 2)`
- **Optional params** — marked with `?` in the reference: `Find(What, After?, LookIn?...)`
- **`Any` type** — means the COM type wasn't resolved; usually `str`, `int`, `bool`, or `float`
- **Constants** — use `win32com.client.constants.<name>` at runtime, e.g. `win32com.client.constants.xlOpenXMLWorkbook`. Integer values are listed in [resources/enums_xl.md](resources/enums_xl.md).

## Object Hierarchy

```
Application
  ├─ Workbooks -> Workbook
  │    ├─ Worksheets -> Worksheet
  │    │    ├─ Range  (also .Cells, .Rows, .Columns)
  │    │    │    ├─ .Font, .Interior, .Borders
  │    │    │    ├─ .FormatConditions
  │    │    │    └─ .Hyperlinks, .Comment, .Validation
  │    │    ├─ Shapes -> Shape
  │    │    ├─ ListObjects -> ListObject
  │    │    ├─ PageSetup
  │    │    └─ AutoFilter
  │    ├─ Charts -> Chart
  │    │    ├─ Axes -> Axis, SeriesCollection -> Series
  │    │    └─ ChartArea, PlotArea, Legend
  │    ├─ Names (named ranges)
  │    └─ PivotCaches -> PivotCache
  └─ Windows -> Window -> Panes -> Pane
```

## Common Patterns

```python
from pyxll import xl_app          # PyXLL: use xl_app() inside Excel
import win32com.client

app = xl_app()                     # or: win32com.client.Dispatch("Excel.Application")
c = win32com.client.constants

wb = app.ActiveWorkbook            # or: app.Workbooks.Open(r"C:\path\to\file.xlsx")
ws = wb.Worksheets("Sheet1")

# Read/write cells
rng = ws.Range("A1:B10")
rng.Value = [[1, 2], [3, 4]]

# Formatting
rng.Font.Bold = True
rng.Interior.Color = 0xFFFF00     # yellow
rng.Borders.LineStyle = c.xlContinuous

# Enum constants via win32com.client.constants
wb.SaveAs(r"C:\out.xlsx", FileFormat=c.xlOpenXMLWorkbook)
ws.Cells.HorizontalAlignment = c.xlCenter
```
