# Context Menus

> **PyXLL callback format:** All callback values (`onAction`, `getEnabled`, etc.) must be
> **`module.function` strings** — e.g. `onAction="context_menus.on_action"`. Examples
> below use abbreviated names for readability; use your actual `module.function` path.

## Structure

```xml
<contextMenus>
  <contextMenu idMso="ContextMenuCell">
    <button id="myBtn" label="My Action" imageMso="RunMacro" onAction="OnMyAction"/>
    <menuSeparator id="sep1"/>
    <menu id="mySubMenu" label="More Options">
      <button id="opt1" label="Option 1" onAction="OnOpt1"/>
    </menu>
  </contextMenu>
</contextMenus>
```

## `contextMenu` element

Each `contextMenu` targets a specific built-in context menu via `idMso`. You add controls
to it; you cannot remove existing built-in items.

**Attribute:** `idMso` (required) — identifies which context menu to extend.

**Common `idMso` values for Excel context menus:**

| idMso | When shown |
|-------|-----------|
| `ContextMenuCell` | Right-click on a cell |
| `ContextMenuColumn` | Right-click on a column header |
| `ContextMenuRow` | Right-click on a row header |
| `ContextMenuSheet` | Right-click on a sheet tab |
| `ContextMenuPivotRead` | Right-click in a pivot table |
| `ContextMenuChartArea` | Right-click on chart area |
| `ContextMenuSeries` | Right-click on a chart series |
| `ContextMenuShape` | Right-click on a shape |
| `ContextMenuTextEdit` | Right-click while editing text |

## Allowed controls in context menus

Context menus support a restricted set of controls (no `editBox`, `comboBox`, `dropDown`,
`box`, `buttonGroup`, or `labelControl`):

| Element | Notes |
|---------|-------|
| `button` | Standard action button |
| `checkBox` | Toggle state |
| `toggleButton` | Toggle with image |
| `gallery` | Grid picker |
| `splitButton` | Button + dropdown |
| `menu` | Submenu |
| `dynamicMenu` | Dynamically generated submenu |
| `control` | Clone a built-in (by `idMso` or `idQ` only) |
| `menuSeparator` | Horizontal dividing line — **no `title` attribute** |

**Important:** `menuSeparator` in context menus does NOT support a `title` attribute
(unlike `menuSeparator` in ribbon menus which does). It only supports `id`, `idQ`, `tag`,
and positioning attributes.

## Positioning controls

Use `insertAfterMso` / `insertBeforeMso` to place your controls relative to existing
items, or just append them (they appear at the bottom by default):

```xml
<contextMenu idMso="ContextMenuCell">
  <!-- Insert at top, before the built-in Cut -->
  <button id="myTop"
          label="My Action"
          insertBeforeMso="Cut"
          onAction="OnMyAction"/>

  <!-- Append at bottom with a separator -->
  <menuSeparator id="mySep"/>
  <button id="myBottom" label="My Bottom Action" onAction="OnMyBottom"/>
</contextMenu>
```

## Example: cell context menu with submenu

```xml
<contextMenus>
  <contextMenu idMso="ContextMenuCell">
    <menuSeparator id="mySep"/>
    <menu id="myToolsMenu" label="My Tools" imageMso="ToolsMenu">
      <button id="tool1"
              label="Analyse Cell"
              imageMso="RunMacro"
              onAction="OnAnalyseCell"/>
      <button id="tool2"
              label="Format Cell Custom"
              imageMso="FormatCells"
              onAction="OnFormatCellCustom"/>
    </menu>
  </contextMenu>
</contextMenus>
```

## Callbacks in context menus

All standard callbacks work in context menus. The `control` parameter passed to callbacks
is the ribbon control object, which you can use to get the control's `Id`, `Tag`, etc.

```python
def OnAnalyseCell(control):
    # do work using xl_app() to get context
    pass

def GetEnabled(control):
    # dynamically enable/disable based on current selection
    return True
```
