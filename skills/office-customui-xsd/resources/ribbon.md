# Ribbon Structure

## Overview

```
ribbon
  ├─ qat                        Quick Access Toolbar
  │    ├─ sharedControls        Controls for all windows
  │    └─ documentControls      Controls for current document
  ├─ tabs
  │    └─ tab (1–100)
  │         └─ group (0–100)
  │              ├─ [controls]  See controls.md
  │              └─ dialogBoxLauncher (optional)
  └─ contextualTabs
       └─ tabSet (1–100, idMso required)
            └─ tab (0–50)
                 └─ group ...
```

## `tab` element

Tabs appear in the ribbon at the top of the Excel window.

**Attributes:**

| Attribute | Description |
|-----------|-------------|
| `id` | Unique custom ID (use for new tabs) |
| `idMso` | Built-in tab ID (use to modify an existing tab) |
| `idQ` | Qualified ID for cross-add-in coordination |
| `label` / `getLabel` | Tab label text |
| `visible` / `getVisible` | Show/hide the tab |
| `keytip` / `getKeytip` | Alt-key shortcut (1–3 chars) |
| `insertAfterMso` / `insertBeforeMso` | Position relative to built-in tab |
| `insertAfterQ` / `insertBeforeQ` | Position relative to qualified ID |

One of `id`, `idMso`, or `idQ` must be specified.

**Common built-in tab idMso values:**
- `TabHome`, `TabInsert`, `TabPageLayoutExcel`, `TabFormulas`, `TabData`
- `TabReview`, `TabView`, `TabDeveloper`, `TabAddIns`

```xml
<!-- New custom tab -->
<tab id="myTab" label="My Tools" insertAfterMso="TabHome">
  ...
</tab>

<!-- Modify existing tab (add a group to Home tab) -->
<tab idMso="TabHome">
  <group id="myGroup" label="My Group">...</group>
</tab>
```

## `group` element

Groups are the labelled sections within a tab. Controls live inside groups.

**Attributes:**

| Attribute | Description |
|-----------|-------------|
| `id` / `idMso` / `idQ` | Identifier |
| `label` / `getLabel` | Group label shown below controls |
| `image` / `imageMso` / `getImage` | Icon for collapsed group |
| `screentip` / `getScreentip` | Tooltip title |
| `supertip` / `getSupertip` | Tooltip body |
| `keytip` / `getKeytip` | Alt-key shortcut |
| `visible` / `getVisible` | Show/hide |
| `insertAfterMso` / `insertBeforeMso` | Position within tab |
| `insertAfterQ` / `insertBeforeQ` | Position relative to qualified ID |
| `autoScale` | boolean — auto-scale contents when tab is narrow |
| `centerVertically` | boolean — vertically center contents |

A group may optionally end with a `dialogBoxLauncher`:

```xml
<group id="myGroup" label="Formatting">
  <button id="btn1" label="Bold" .../>
  <dialogBoxLauncher>
    <button id="dlgBtn" label="Format Options" onAction="ShowDialog"/>
  </dialogBoxLauncher>
</group>
```

## Contextual tabs

Contextual tabs appear only when specific content is selected (e.g. a chart or table).
They are grouped into `tabSet` elements identified by `idMso`.

```xml
<contextualTabs>
  <tabSet idMso="TabSetChartTools" visible="true" getVisible="GetChartTabVisible">
    <tab idMso="TabChartToolsDesign">
      <group id="myChartGroup" label="My Chart Tools">
        ...
      </group>
    </tab>
  </tabSet>
</contextualTabs>
```

`tabSet` attributes: `idMso` (required), `visible`, `getVisible`.

## Quick Access Toolbar (QAT)

```xml
<qat>
  <sharedControls>
    <!-- available to all documents -->
    <button id="myQatBtn" label="Quick Run" onAction="my_module.quick_run" imageMso="RunMacro"/>
    <separator id="sep1"/>
    <control idMso="FileSave"/>   <!-- clone built-in -->
  </sharedControls>
  <documentControls>
    <!-- attached to current document only -->
    <button id="docBtn" label="Doc Action" onAction="my_module.doc_action"/>
  </documentControls>
</qat>
```

QAT allows: `control` (clone), `button`, `separator`.

`control` in QAT supports: `id`, `idQ`, `idMso`, plus `description`, `size`.

## `separator` element

A vertical bar between controls. Used in groups and `buttonGroup`:

```xml
<separator id="sep1"/>
```

Attributes: `id`, `idQ`, `tag`, `visible`, `getVisible`, `insertAfterMso`, `insertBeforeMso`,
`insertAfterQ`, `insertBeforeQ`.

## PyXLL: merging multiple ribbon files

### Specifying multiple files

The `ribbon` key in `[PYXLL]` accepts a single file or a list of files (comma-separated
or one per line). All listed files are loaded and merged into one ribbon:

```ini
[PYXLL]
; comma-separated
ribbon = base_ribbon.xml, tools_ribbon.xml, reporting_ribbon.xml

; or newline-separated
ribbon =
    base_ribbon.xml
    tools_ribbon.xml
    reporting_ribbon.xml
```

Paths may be absolute or relative to the `pyxll.cfg` file. Ribbon files may also be
discovered automatically via Python entry points (e.g. from installed packages), in
which case they are merged in alongside any files listed in the config.

### Merge rules

PyXLL merges all loaded ribbon files by the following rules:

| Situation | Result |
|-----------|--------|
| Two `tab` elements share the same `id` | Merged into one tab; their `group` children are combined |
| Two `group` elements (in the same merged tab) share the same `id` | Merged into one group; their control children are combined |
| A `tab` or `group` has a unique `id` | Appended in file-load order |

**Use unique IDs for every element you own.** If an ID unintentionally matches one from
another file or add-in, their contents will be silently merged.

### Controlling merge order: `insertBefore` and `insertAfter`

To control where an element appears relative to elements from other files, PyXLL
recognises two attributes that are **not part of the XML schema** — PyXLL strips them
before sending the final XML to Excel:

| Attribute | Description |
|-----------|-------------|
| `insertBefore` | Place this element before the sibling whose `id` matches this value |
| `insertAfter` | Place this element after the sibling whose `id` matches this value |

Rules:
- Can be set on `tab`, `group`, or any child element of a `group`
- Only one of `insertBefore` or `insertAfter` may be set on a given element (not both)
- Values are custom `id` strings — **not** `idMso` values

```xml
<!-- file_a.xml: defines a tab with two groups -->
<tab id="MyTab" label="My Tools">
  <group id="AnalysisGroup" label="Analysis">...</group>
  <group id="ToolsGroup"    label="Tools">...</group>
</tab>

<!-- file_b.xml: adds a group between the two groups from file_a.xml -->
<tab id="MyTab">
  <group id="ReportingGroup" label="Reporting" insertBefore="ToolsGroup">
    ...
  </group>
</tab>
```

Result: the merged `MyTab` contains `AnalysisGroup`, then `ReportingGroup`, then
`ToolsGroup`.

**Important distinction:** `insertBefore`/`insertAfter` (PyXLL merge attributes) are
different from the schema's `insertBeforeMso`/`insertAfterMso` (which position elements
relative to built-in Office controls and are valid XML schema attributes).
