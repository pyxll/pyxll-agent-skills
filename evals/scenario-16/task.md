# Branded Ribbon with Custom PNG Icons

## Problem Description

Meridian Wealth Management wants their PyXLL Excel add-in to display their corporate
branding in the ribbon. Their design team has produced two custom button icons as PNG
files with alpha-channel transparency. The icons are shipped as resources inside their
Python package `mw_addin`:

- `run_analysis.png` — icon for the "Run Analysis" button
- `export_report.png` — icon for the "Export Report" button

A third button ("Refresh Data") should use a standard built-in Office icon rather
than a custom one.

The PNGs must render with correct transparency — earlier attempts using the default
image loading produced black backgrounds instead of transparent ones.

All callbacks live in the `mw_addin.ribbon` module.

## Output Specification

Produce `mw_ribbon.xml` — a complete customUI XML file with a ribbon tab containing
the three buttons described above, with images configured correctly for each.
