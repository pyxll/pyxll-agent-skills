# Backstage (File Menu)

The Backstage is the full-screen view opened by clicking the "File" tab. You can add custom
tabs and fast-command buttons to it.

## Structure

```
backstage
  ├─ tab (0–255, CT_BackstageTab)
  │    ├─ firstColumn (CT_BackstageGroups)
  │    │    ├─ taskFormGroup  (or)
  │    │    ├─ group (CT_BackstageGroup)
  │    │    └─ taskGroup
  │    └─ secondColumn (CT_SimpleGroups)
  │         ├─ group
  │         └─ taskGroup
  └─ button (0–255, CT_BackstageFastCommandButton)
```

## `backstage` element

```xml
<backstage onShow="OnBackstageShow" onHide="OnBackstageHide">
  <tab id="myTab" label="My Tab" keytip="MT">
    ...
  </tab>
  <button id="myFastCmd"
          label="Quick Export"
          imageMso="FileExportToExcel"
          onAction="OnQuickExport"
          isDefinitive="true"/>
</backstage>
```

| Attribute | Description |
|-----------|-------------|
| `onShow` | Callback when Backstage opens |
| `onHide` | Callback when Backstage closes |

## `tab` element (BackstageTab)

A full tab page in the Backstage.

```xml
<tab id="myBackstageTab"
     label="My Settings"
     keytip="MS"
     insertAfterMso="TabInfo"
     columnWidthPercent="40">
  <firstColumn>
    <group id="myGroup" label="Options">
      ...
    </group>
  </firstColumn>
  <secondColumn>
    <group id="myGroup2" label="Preview">
      ...
    </group>
  </secondColumn>
</tab>
```

| Attribute | Description |
|-----------|-------------|
| `columnWidthPercent` | Percentage width of the first column (1–99) |
| `firstColumnMinWidth` / `firstColumnMaxWidth` | Pixel constraints for first column |
| `secondColumnMinWidth` / `secondColumnMaxWidth` | Pixel constraints for second column |
| `title` / `getTitle` | Optional large title shown in the tab |

## `button` (fast command)

A button in the left navigation pane of the Backstage (like "New", "Open", "Save As").

```xml
<button id="myFastCmd"
        label="Export Data"
        imageMso="DataExportExcel"
        onAction="OnExportData"
        isDefinitive="true"
        insertAfterMso="FileSave"/>
```

`isDefinitive="true"` closes the Backstage when the button is clicked.

## `group` (BackstageGroup)

Groups in the Backstage have a different structure from ribbon groups.

```xml
<group id="myBsGroup"
       label="Export Settings"
       style="normal"
       showLabel="true"
       helperText="Configure export options below.">
  <primaryItem>
    <button id="exportBtn"
            label="Export Now"
            imageMso="DataExportExcel"
            onAction="OnExport"
            isDefinitive="true"/>
  </primaryItem>
  <topItems>
    <editBox id="filename" label="File name:" getText="GetFilename" onChange="OnFilenameChanged"/>
    <dropDown id="format" label="Format:" onAction="OnFormatChanged" getSelectedItemIndex="GetFormatIndex">
      <item id="csv"  label="CSV"/>
      <item id="xlsx" label="Excel"/>
    </dropDown>
  </topItems>
  <bottomItems>
    <checkBox id="includeHeader" label="Include header row" getPressed="GetIncludeHeader" onAction="OnHeaderToggle"/>
  </bottomItems>
</group>
```

| Attribute | Values | Description |
|-----------|--------|-------------|
| `style` / `getStyle` | `"normal"`, `"warning"`, `"error"` | Visual style of the group |
| `helperText` / `getHelperText` | string | Descriptive text shown above controls |
| `showLabel` / `getShowLabel` | boolean | Whether to show the group label |

**Structure of `group`:**
- `primaryItem` (optional, 0–1): a `button` or `menu` as the primary action
- `topItems` (optional): controls shown above the primary item area
- `bottomItems` (optional): controls shown below the primary item area

## Controls available in Backstage groups

The `topItems` and `bottomItems` (and `groupBox`, `layoutContainer` children) accept:

| Element | Description |
|---------|-------------|
| `button` | Action button with `style` (normal/borderless/large) and `expand` |
| `checkBox` | Checkbox with `expand`, `description`, `screentip` |
| `editBox` | Text input with `alignLabel`, `expand` |
| `dropDown` | Dropdown with `alignLabel`, `expand`, optional `item` children |
| `radioGroup` | Group of radio buttons (`radioButton` children) |
| `comboBox` | Editable dropdown with `item` children |
| `hyperlink` | Clickable link with `target`/`getTarget`, `expand` |
| `labelControl` | Read-only text with `noWrap`, `expand` |
| `groupBox` | Labelled box container for further controls |
| `layoutContainer` | Layout helper with `align`, `expand`, `layoutChildren` |
| `imageControl` | Displays an image with `altText`/`getAltText` |

### `expand` attribute

Most Backstage controls support `expand`:

| Value | Description |
|-------|-------------|
| `"horizontal"` | Fill available horizontal space |
| `"vertical"` | Fill available vertical space |
| `"both"` | Fill both directions |
| `"neither"` | Use natural size (default) |

### `alignLabel` attribute

Controls label alignment on Backstage controls:
`"topLeft"`, `"top"`, `"topRight"`, `"left"`, `"center"`, `"right"`,
`"bottomLeft"`, `"bottom"`, `"bottomRight"`

## `taskGroup` / `taskFormGroup`

`taskGroup` shows a list of tasks (like the "New" tab showing templates).

```xml
<taskGroup id="myTaskGroup" label="Templates" allowedTaskSizes="largeMediumSmall">
  <category id="cat1" label="Built-in">
    <task id="task1"
          label="Blank Workbook"
          imageMso="FileNew"
          onAction="OnNewBlank"
          description="Create a blank workbook"/>
  </category>
</taskGroup>
```

`allowedTaskSizes` values: `"largeMediumSmall"`, `"largeMedium"`, `"large"`,
`"mediumSmall"`, `"medium"`, `"small"`.

`taskFormGroup` is similar but each task contains Backstage `group` elements (a form layout).
