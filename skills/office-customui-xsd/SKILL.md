---
name: office-customui-xsd
description: Reference for the Office CustomUI XML schema used to define Excel ribbon toolbars and context menus. Use this skill whenever writing, editing, reviewing, or debugging customUI XML — including ribbon tabs, groups, buttons, dropdowns, galleries, menus, context menus, the QAT, or the Backstage. Also use when working with PyXLL ribbon configuration. Training-data knowledge of the schema is incomplete and can produce invalid XML — the schema and these docs are the authoritative source.
user-invocable: false
metadata:
  author: pyxll
  version: 0.1.4
---

# Office CustomUI XML Reference Skill

## How to use this skill

1. **Read `resources/index.md`** — find which reference file covers your task, and
   check the allowed-controls table before placing any control (not all controls are
   valid in all locations).
2. **Read the relevant doc(s):**
   - `resources/document-structure.md` — root element, namespace, overall XML skeleton
   - `resources/ribbon.md` — tabs, groups, QAT, contextual tabs, PyXLL merge rules
   - `resources/controls.md` — all controls for ribbon groups and menus
   - `resources/context-menus.md` — context menu structure and allowed controls
   - `resources/attributes.md` — complete attribute reference (label, image, callbacks, etc.)
   - `resources/backstage.md` — File menu (Backstage) customisation
3. **If you cannot find what you need** in the markdown docs, read the raw XSD:
   `resources/office-customui-2009-07.xsd`. Never guess — invalid attributes are
   silently ignored and invalid nesting causes load errors.
4. **Validate the XML before deploying.** Run it through `xmllint` using the bundled XSD.
   The XSD is at `<SKILL_BASE_DIR>/resources/office-customui-2009-07.xsd` — replace
   `<SKILL_BASE_DIR>` with the actual base directory path provided when this skill is loaded.
   ```bash
   xmllint --noout --schema <SKILL_BASE_DIR>/resources/office-customui-2009-07.xsd ribbon.xml
   ```
   Or with Python's lxml: `etree.XMLSchema(etree.parse('<SKILL_BASE_DIR>/resources/office-customui-2009-07.xsd')).assertValid(etree.parse('ribbon.xml'))`

   **PyXLL caveat:** `insertBefore`/`insertAfter` are PyXLL-only merge attributes not in
   the schema, so they produce expected validation errors. Strip them before validating,
   or treat those specific attribute errors as false positives.

---

## Rules for AI Agents

> **These rules are mandatory. Follow them before writing any customUI XML.**

1. **Callbacks are `module.function` strings** — e.g. `"my_module.on_button_click"`. All
   `onAction`, `getLabel`, `getEnabled`, etc. attributes require this format. The module
   must be importable from the Python path.

2. **IDs must be unique across the entire XML file.** Reusing an `id` anywhere in the file is a schema error.

3. **Image attributes are mutually exclusive.** Specify only one of `image`, `imageMso`,
   or `getImage` on any control — not multiple.

4. **Positioning attributes are mutually exclusive.** Use only one of `insertAfterMso`,
   `insertBeforeMso`, `insertAfterQ`, `insertBeforeQ` per control.

5. **When working with PyXLL, always invoke the `fetch-pyxll-docs` skill** before writing
   or modifying any ribbon or context menu code. This schema skill covers the XML structure;
   the PyXLL docs cover how the XML file is configured (`pyxll.cfg` `ribbon` key), how
   callback functions are resolved, the `IRibbonUI`/`IRibbonControl` Python API, and
   PyXLL-specific behaviour such as ribbon merging and `pyxll.load_image`. Both skills
   are needed together for correct PyXLL ribbon work.

---

## Minimal valid skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<customUI xmlns="http://schemas.microsoft.com/office/2009/07/customui"
          onLoad="my_ribbon.on_load"
          loadImage="pyxll.load_image">
  <ribbon>
    <tabs>
      <tab id="myTab" label="My Add-in" insertAfterMso="TabHome">
        <group id="myGroup" label="Tools">
          <button id="myButton"
                  label="Run"
                  imageMso="RunMacro"
                  size="large"
                  screentip="Run"
                  supertip="Run the selected analysis."
                  onAction="my_ribbon.on_run"/>
        </group>
      </tab>
    </tabs>
  </ribbon>
  <contextMenus>
    <contextMenu idMso="ContextMenuCell">
      <button id="myCellAction"
              label="My Cell Action"
              imageMso="RunMacro"
              onAction="my_ribbon.on_cell_action"/>
    </contextMenu>
  </contextMenus>
</customUI>
```

Note: `contextMenus` must come after `ribbon`; `size="large"` is only valid on buttons inside ribbon groups.

---

## Trigger conditions

Invoke this skill automatically (without being asked) whenever writing, editing,
reviewing, or debugging customUI XML — ribbon tabs, groups, controls, context menus,
QAT, or Backstage. Also invoke for any ribbon callback function or PyXLL ribbon config.

Non-obvious triggers:
- XML using the older `http://schemas.microsoft.com/office/2006/01/customui` namespace
- The user mentions Office UI Extensibility or RibbonX
