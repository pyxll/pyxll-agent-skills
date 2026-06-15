# Attributes Reference

## ID attributes

Every control needs exactly one of `id`, `idMso`, or `idQ`.

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | ST_UniqueID | Custom unique ID. Must be unique across the entire customUI XML file. Max 1024 chars. |
| `idMso` | ST_ID | Built-in control ID. Use to reference or modify an existing Office control. |
| `idQ` | ST_QID | Qualified ID in the form `prefix:name` where `prefix` maps to your namespace. Allows multiple add-ins to reference the same custom control. |
| `tag` | ST_String | Arbitrary string data attached to the control. Accessible in callbacks. Max 1024 chars. |

**Qualified IDs example:**

```xml
<customUI xmlns="http://schemas.microsoft.com/office/2009/07/customui"
          xmlns:myaddin="MyAddInNamespace">
  <ribbon>
    <tabs>
      <tab idQ="myaddin:MyTab" label="Shared Tab">
        ...
      </tab>
    </tabs>
  </ribbon>
</customUI>
```

Another add-in can then add controls to `myaddin:MyTab` by referencing `idQ="myaddin:MyTab"`.

## Position attributes

Controls positioning within their parent container. These are mutually exclusive — use only one.

| Attribute | Description |
|-----------|-------------|
| `insertAfterMso` | Place after a built-in control with this `idMso` |
| `insertBeforeMso` | Place before a built-in control with this `idMso` |
| `insertAfterQ` | Place after a control with this qualified ID |
| `insertBeforeQ` | Place before a control with this qualified ID |

## Label attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `label` | ST_String (max 1024) | Static label text |
| `getLabel` | callback | Dynamic label: `def cb(control) -> str` |

## Image attributes

Only one of `image`, `imageMso`, or `getImage` may be specified.

| Attribute | Type | Description |
|-----------|------|-------------|
| `image` | ST_Uri (max 1024) | Path to a custom image resource |
| `imageMso` | ST_ID | ID of a built-in Office icon (e.g. `"RunMacro"`, `"FileSave"`) |
| `getImage` | callback | Dynamic: `def cb(control) -> IPictureDisp` |
| `showImage` | boolean | Whether to display the image (default true) |
| `getShowImage` | callback | Dynamic: `def cb(control) -> bool` |

**Common `imageMso` values:**
`RunMacro`, `FileSave`, `FileOpen`, `FilePrint`, `Undo`, `Redo`, `Cut`, `Copy`, `Paste`,
`Bold`, `Italic`, `Underline`, `FormatCells`, `OptionsDialog`, `Refresh`, `Close`,
`Help`, `HappyFace`, `SadFace`, `SelectAll`, `Find`, `Replace`, `Sort`, `Filter`

**Custom images with PyXLL:** Set `loadImage="pyxll.load_image"` on the `customUI` root
element, then use `image="filename.png"` on controls. `pyxll.load_image` handles PNG
transparency correctly. For package resources use `image="module:resource_name"`.
Without `pyxll.load_image`, Excel's built-in image handler is used and PNG transparency
may not render correctly.

## Tooltip attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `screentip` | ST_String (max 1024) | Short tooltip title shown on hover |
| `getScreentip` | callback | Dynamic screentip |
| `supertip` | ST_String (max 1024) | Long tooltip body shown on hover |
| `getSupertip` | callback | Dynamic supertip |

## Keytip attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `keytip` | ST_Keytip (1–3 chars, no whitespace) | Alt-key navigation shortcut |
| `getKeytip` | callback | Dynamic keytip |

## Visibility and enabled state

| Attribute | Type | Description |
|-----------|------|-------------|
| `visible` | boolean | Whether the control is shown |
| `getVisible` | callback | Dynamic: `def cb(control) -> bool` |
| `enabled` | boolean | Whether the control is interactive |
| `getEnabled` | callback | Dynamic: `def cb(control) -> bool` |

## Show label

| Attribute | Type | Description |
|-----------|------|-------------|
| `showLabel` | boolean | Whether to show the label text on the control |
| `getShowLabel` | callback | Dynamic: `def cb(control) -> bool` |

## Size attribute (buttons and galleries in groups)

| Attribute | Values | Description |
|-----------|--------|-------------|
| `size` | `"normal"` or `"large"` | Large = tall button with image above label |
| `getSize` | callback | Dynamic size: `def cb(control) -> str` |

## Callback values in PyXLL

In PyXLL, all callback attribute values are **Python function name strings** in
`module.function` format. The module must be importable from the Python path:

```xml
<button id="myBtn" onAction="my_module.on_click"/>
<customUI loadImage="pyxll.load_image" onLoad="my_module.on_load"/>
```

The `control` parameter passed to most callbacks is an `IRibbonControl` object with:
- `control.Id` — the control's `id` attribute value
- `control.Tag` — the control's `tag` attribute value
- `control.Context` — the active window

The `onLoad` callback on `customUI` is the exception — it receives an `IRibbonUI` object
(not `IRibbonControl`). Store it to invalidate control state:

```python
_ribbon = None

def on_load(ribbon_ui):          # ribbon_ui is IRibbonUI
    global _ribbon
    _ribbon = ribbon_ui

def refresh():
    if _ribbon:
        _ribbon.Invalidate()
        # or: _ribbon.InvalidateControl("myControlId")
        # or: _ribbon.ActivateTab("myTabId")
```

## Action callbacks

| Attribute | Used by | Callback signature |
|-----------|---------|-------------------|
| `onAction` | button, toggleButton, checkBox, dropDown, gallery, comboBox | See below |
| `onChange` | editBox, comboBox | `def cb(control, text): ...` |
| `getPressed` | toggleButton, checkBox | `def cb(control) -> bool` |

**`onAction` signatures by control type:**

```python
# button, menu item:
def on_click(control):
    ...

# toggleButton, checkBox:
def on_toggle(control, pressed):   # pressed is True/False
    ...

# dropDown, gallery (when item selected):
def on_select(control, selectedId, selectedIndex):
    ...
```

## Description attribute

| Attribute | Type | Description |
|-----------|------|-------------|
| `description` | ST_LongString (max 4096) | Extended description shown in `itemSize="large"` menus |
| `getDescription` | callback | Dynamic: `def cb(control) -> str` |

## Dynamic dropdown attributes

Used by `dropDown`, `gallery`, `comboBox` for dynamic item lists:

| Attribute | Description |
|-----------|-------------|
| `showItemImage` | boolean — show image next to each item |
| `showItemLabel` | boolean — show label next to each item (dropDown/gallery) |
| `sizeString` | Sample string used to calculate control width |
| `getItemCount` | `def cb(control) -> int` — number of items |
| `getItemLabel` | `def cb(control, index) -> str` |
| `getItemImage` | `def cb(control, index) -> IPictureDisp` |
| `getItemID` | `def cb(control, index) -> str` |
| `getItemScreentip` | `def cb(control, index) -> str` |
| `getItemSupertip` | `def cb(control, index) -> str` |
| `getSelectedItemID` | `def cb(control) -> str` (dropDown only) |
| `getSelectedItemIndex` | `def cb(control) -> int` (dropDown/gallery only) |

## Dynamic menu content

| Attribute | Used by | Description |
|-----------|---------|-------------|
| `getContent` | dynamicMenu | **Required.** `def cb(control) -> str` — returns XML string |
| `invalidateContentOnDrop` | dynamicMenu, comboBox, gallery | Re-fetch content every time the dropdown opens |

## String length limits

| Type | Min | Max | Used for |
|------|-----|-----|----------|
| `ST_String` | 1 | 1024 | label, screentip, supertip, keytip, tag, sizeString, image path |
| `ST_LongString` | 1 | 4096 | description, altText, helperText |
| `ST_Keytip` | 1 | 3 | keytip (no whitespace) |
| `ST_StringLength` | 1 | 1024 | maxLength on editBox |
