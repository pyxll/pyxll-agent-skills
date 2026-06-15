# Document Structure

## Namespace and root element

The root element is `customUI`. Two namespace versions exist:

| Namespace | Use when |
|-----------|----------|
| `http://schemas.microsoft.com/office/2009/07/customui` | **Required** for context menus; recommended for all new files |
| `http://schemas.microsoft.com/office/2006/01/customui` | Older version — ribbon-only, no context menu support |

Always use the 2009 namespace (the one this XSD covers) unless maintaining legacy files:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<customUI xmlns="http://schemas.microsoft.com/office/2009/07/customui"
          onLoad="my_module.on_ribbon_load">
  <!-- children -->
</customUI>
```

**Root attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `onLoad` | callback | Called when the UI loads. Receives an `IRibbonUI` object used to invalidate controls. |
| `loadImage` | callback | Called to load custom images by ID. Receives the image ID string, returns an `IPictureDisp`. |

## Children of `customUI`

All children are optional. Order must be: `commands`, `ribbon`, `backstage`, `contextMenus`.

### `commands` — Global built-in overrides

Override or disable built-in commands across the entire application:

```xml
<commands>
  <command idMso="FileSave" enabled="false"/>
  <command idMso="FilePrint" onAction="my_module.on_print"/>
</commands>
```

`command` attributes: `idMso` (required), `onAction`, `enabled`, `getEnabled`.

Setting `enabled="false"` on a built-in disables it everywhere (ribbon, menus, keyboard shortcuts).

### `ribbon` — The ribbon toolbar

```xml
<ribbon startFromScratch="false">
  <qat>...</qat>                       <!-- Quick Access Toolbar -->
  <tabs>...</tabs>                     <!-- Custom and modified tabs -->
  <contextualTabs>...</contextualTabs> <!-- Context-sensitive tabs -->
</ribbon>
```

`startFromScratch="true"` removes all built-in tabs and the QAT, leaving only your custom UI.

See [ribbon.md](ribbon.md) for tab/group structure.

### `backstage` — File menu

```xml
<backstage onShow="OnBackstageShow" onHide="OnBackstageHide">
  <tab ...>...</tab>
  <button .../>
</backstage>
```

See [backstage.md](backstage.md) for details.

### `contextMenus` — Right-click menus

```xml
<contextMenus>
  <contextMenu idMso="ContextMenuCell">
    <button id="myButton" label="My Action" onAction="my_module.on_action"/>
  </contextMenu>
</contextMenus>
```

See [context-menus.md](context-menus.md) for details.

## Minimal complete example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<customUI xmlns="http://schemas.microsoft.com/office/2009/07/customui"
          onLoad="my_ribbon.on_ribbon_load"
          loadImage="pyxll.load_image">
  <ribbon>
    <tabs>
      <tab id="myTab" label="My Add-in">
        <group id="myGroup" label="Tools">
          <button id="myButton"
                  label="Run"
                  imageMso="RunMacro"
                  size="large"
                  onAction="my_ribbon.on_run"/>
        </group>
      </tab>
    </tabs>
  </ribbon>
</customUI>
```

## PyXLL integration notes

### Configuring the ribbon XML file

In PyXLL, the ribbon XML file is specified via the `ribbon` key in the `[PYXLL]` section
of `pyxll.cfg`. The path can be relative to the config file or absolute. Multiple files
can be listed (comma or newline separated) and PyXLL merges them automatically — tabs
and groups with the same `id` are merged; elements with unique IDs are appended:

```ini
[PYXLL]
; single file
ribbon = ribbon.xml

; or multiple files — PyXLL merges them
ribbon =
    base_ribbon.xml
    tools_ribbon.xml

modules = my_ribbon_module
```

See [ribbon.md](ribbon.md) for the full merge rules and how to control merge order with
`insertBefore`/`insertAfter`.

The Python modules that contain ribbon callback functions should be listed in `modules`
so they are reloaded when PyXLL reloads.

### Callback function names

All callback attribute values are **Python function name strings** in `module.function`
format. The module must be importable (on the Python path):

```xml
<button id="myBtn" onAction="my_module.on_button_clicked"/>
```

Two built-in PyXLL values are available:
- `pyxll.reload` — triggers a PyXLL reload (useful for a "Reload" button)
- `pyxll.load_image` — image loader for the `loadImage` attribute (recommended over Excel's built-in handler, handles PNG transparency correctly)

### Storing the IRibbonUI object

The `onLoad` callback on `customUI` receives an `IRibbonUI` object. Store it to
invalidate controls later:

```python
ribbon_ui = None

def on_ribbon_load(ribbon):
    global ribbon_ui
    ribbon_ui = ribbon

def refresh_ribbon():
    if ribbon_ui:
        ribbon_ui.Invalidate()           # refresh all controls
        # or: ribbon_ui.InvalidateControl("myControlId")
```

### Using pyxll.load_image

Set `loadImage="pyxll.load_image"` on the `customUI` element to use PyXLL's image
loader, then reference images by filename in control `image` attributes:

```xml
<customUI xmlns="http://schemas.microsoft.com/office/2009/07/customui"
          loadImage="pyxll.load_image">
  <ribbon>
    <tabs>
      <tab id="myTab" label="My Tools">
        <group id="myGroup" label="Tools">
          <button id="reloadBtn"
                  label="Reload PyXLL"
                  image="reload.png"
                  size="large"
                  onAction="pyxll.reload"/>
        </group>
      </tab>
    </tabs>
  </ribbon>
</customUI>
```

Images can be filenames or package resources in the form `module:resource`.
