# Shared Ribbon for a Multi-Team PyXLL Add-in

## Problem Description

FinTech Analytics Ltd is building a PyXLL Excel add-in shared by two teams. Each team
owns its own ribbon XML file to avoid version-control conflicts:

- The **Data Science team** defines an "Analytics" tab containing two groups: one for
  data preparation tools and one for running models. Each group should contain at least
  one button. Callbacks live in the `ds_tools` Python module.

- The **Reporting team** wants to add a "Reporting" group to the same Analytics tab —
  but it must appear **between** the two Data Science groups, not appended at the end.
  Callbacks live in `report_tools`.

Both XML files are loaded by PyXLL at startup and merged automatically. The final
ribbon must show all three groups in the correct order: Prepare → Reporting → Models.

## Output Specification

Produce three files:

- `data_ribbon.xml` — Data Science team's ribbon file (Analytics tab with two groups,
  each containing at least one button with a callback)
- `report_ribbon.xml` — Reporting team's ribbon file (adds the Reporting group to the
  Analytics tab, positioned between the two Data Science groups)
- `pyxll.cfg` — configuration snippet (just the `[PYXLL]` section) showing how PyXLL
  is configured to load both ribbon files
