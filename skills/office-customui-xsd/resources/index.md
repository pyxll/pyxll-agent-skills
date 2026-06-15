# Office CustomUI XML Reference — Index

Schema: `http://schemas.microsoft.com/office/2009/07/customui` (office-customui-2009-07.xsd)

Used in Excel add-ins (including PyXLL) to customize the ribbon toolbar, context menus,
Quick Access Toolbar (QAT), and the Backstage (File menu).

## Which doc to read

| Task | Read |
|------|------|
| Starting a new customUI XML file | [document-structure.md](document-structure.md) |
| Adding a custom ribbon tab, group, or contextual tab | [ribbon.md](ribbon.md) |
| Adding controls to a group (buttons, dropdowns, etc.) | [controls.md](controls.md) |
| Adding items to a right-click context menu | [context-menus.md](context-menus.md) |
| Understanding any attribute (label, image, callbacks, etc.) | [attributes.md](attributes.md) |
| Customizing the File menu (Backstage) | [backstage.md](backstage.md) |
| Something not found in the above docs | Read [../resources/office-customui-2009-07.xsd](office-customui-2009-07.xsd) |

## Top-level structure

```xml
<customUI xmlns="http://schemas.microsoft.com/office/2009/07/customui"
          onLoad="OnRibbonLoad">
  <commands>...</commands>       <!-- optional: override built-in commands -->
  <ribbon>...</ribbon>           <!-- ribbon tabs, groups, QAT -->
  <backstage>...</backstage>     <!-- File menu customization -->
  <contextMenus>...</contextMenus> <!-- right-click menu customization -->
</customUI>
```

## Element quick reference

| Element | Parent | Description |
|---------|--------|-------------|
| `customUI` | (root) | Root element |
| `commands` | `customUI` | Global built-in command overrides |
| `command` | `commands` | Override `onAction`/`enabled` for a built-in by `idMso` |
| `ribbon` | `customUI` | Ribbon toolbar |
| `tabs` | `ribbon` | Collection of custom/modified tabs |
| `tab` | `tabs` | A ribbon tab |
| `group` | `tab` | A group within a tab |
| `contextualTabs` | `ribbon` | Contextual tab sets (appear on selection) |
| `tabSet` | `contextualTabs` | A contextual tab set identified by `idMso` |
| `qat` | `ribbon` | Quick Access Toolbar |
| `sharedControls` | `qat` | QAT controls for all windows |
| `documentControls` | `qat` | QAT controls for the current document |
| `contextMenus` | `customUI` | Collection of context menus |
| `contextMenu` | `contextMenus` | A specific context menu (identified by `idMso`) |
| `backstage` | `customUI` | File menu (Backstage) |

## Controls available per location

| Control | Ribbon group | Menu | Context menu | ButtonGroup | QAT |
|---------|:-----------:|:----:|:------------:|:-----------:|:---:|
| `button` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `toggleButton` | ✓ | ✓ | ✓ | ✓ | — |
| `checkBox` | ✓ | ✓ | ✓ | — | — |
| `editBox` | ✓ | — | — | — | — |
| `comboBox` | ✓ | — | — | — | — |
| `dropDown` | ✓ | — | — | — | — |
| `gallery` | ✓ | ✓ | ✓ | ✓ | — |
| `menu` | ✓ | ✓ | ✓ | ✓ | — |
| `dynamicMenu` | ✓ | ✓ | ✓ | ✓ | — |
| `splitButton` | ✓ | ✓ | ✓ | ✓ | — |
| `labelControl` | ✓ | — | — | — | — |
| `box` | ✓ | — | — | — | — |
| `buttonGroup` | ✓ | — | — | — | — |
| `control` (clone) | ✓ | ✓ | ✓ | ✓ | ✓ |
| `separator` | ✓ | — | — | ✓ | ✓ |
| `menuSeparator` | — | ✓ | ✓ | — | — |
