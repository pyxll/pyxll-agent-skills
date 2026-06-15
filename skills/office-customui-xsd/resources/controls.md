# Controls Reference

Controls that can appear inside a ribbon `group`. See [index.md](index.md) for which controls
are allowed in menus, context menus, and buttonGroups.

For attribute details (label, image, enabled, etc.) see [attributes.md](attributes.md).

> **PyXLL callback format:** All callback attribute values (`onAction`, `getLabel`,
> `getEnabled`, `getImage`, etc.) must be **`module.function` strings** — e.g.
> `onAction="my_ribbon.on_run"`. The examples below use abbreviated names like
> `"OnRunAnalysis"` for readability; replace them with your actual `module.function`
> paths in real code.

---

## `button`

A push button. In a ribbon group it can be `size="large"` (tall, image above label) or
`size="normal"` (small, image left of label).

```xml
<button id="myBtn"
        label="Run Analysis"
        imageMso="RunMacro"
        size="large"
        screentip="Run Analysis"
        supertip="Run the analysis on the current selection."
        onAction="OnRunAnalysis"/>
```

**Unique attributes:**

| Attribute | Description |
|-----------|-------------|
| `size` / `getSize` | `"normal"` or `"large"` (ribbon group only) |
| `onAction` | Callback: `def cb(control): ...` |
| `description` / `getDescription` | Extended description (shown in large-item menus) |

---

## `toggleButton`

A button with an on/off pressed state (like Bold). Has the same attributes as `button`
plus `getPressed`.

```xml
<toggleButton id="myToggle"
              label="Auto Refresh"
              imageMso="Refresh"
              onAction="OnToggleAutoRefresh"
              getPressed="GetAutoRefreshPressed"/>
```

**Unique attributes:**

| Attribute | Description |
|-----------|-------------|
| `getPressed` | Callback: returns `True` if button is in pressed state |
| `onAction` | Callback receives `(control, pressed)` — the new pressed state |

---

## `checkBox`

A labelled checkbox. No image attributes. Similar to `toggleButton` but renders as a tick box.

```xml
<checkBox id="myCheck"
          label="Show Preview"
          onAction="OnShowPreviewChanged"
          getPressed="GetShowPreview"/>
```

No `image`, `imageMso`, `getImage`, `showImage`, `showLabel` or `size` attributes.
`onAction` callback receives `(control, pressed)`.

---

## `editBox`

A text input field in the ribbon.

```xml
<editBox id="myEditBox"
         label="Search:"
         sizeString="XXXXXXXXXX"
         maxLength="256"
         getText="GetSearchText"
         onChange="OnSearchChanged"/>
```

**Unique attributes:**

| Attribute | Description |
|-----------|-------------|
| `maxLength` | Max characters (1–1024) |
| `getText` | Callback: returns current text string |
| `onChange` | Callback: `(control, text)` — called when user changes text |
| `sizeString` | Sample string used to size the control width |

---

## `comboBox`

An editable dropdown (combines `editBox` with selectable items). Items can be static
(child `item` elements) or dynamic (via callbacks). Up to 1000 items.

```xml
<comboBox id="myCombo"
          label="Font:"
          sizeString="Calibri Body"
          getText="GetFontName"
          onChange="OnFontChanged"
          showItemImage="false">
  <item id="item1" label="Calibri"/>
  <item id="item2" label="Arial"/>
  <item id="item3" label="Times New Roman"/>
</comboBox>
```

**Unique attributes (in addition to editBox):**

| Attribute | Description |
|-----------|-------------|
| `showItemImage` | boolean — show images next to items |
| `getItemCount` | Callback: returns number of dynamic items |
| `getItemLabel` | Callback: `(control, index)` → label string |
| `getItemImage` | Callback: `(control, index)` → image |
| `getItemID` | Callback: `(control, index)` → ID string |
| `getItemScreentip` | Callback: `(control, index)` → screentip |
| `getItemSupertip` | Callback: `(control, index)` → supertip |
| `invalidateContentOnDrop` | boolean — re-fetch items each time dropdown opens |

Static `item` attributes: `id`, `label`, `image`, `imageMso`, `screentip`, `supertip`.

---

## `dropDown`

A dropdown that shows a selected item. Unlike `comboBox`, the user cannot type freely.
`onAction` is called when the user picks an item. Can contain `item` and `button` children
(buttons appear as extra actions, separate from the selection list; up to 16 buttons).

```xml
<dropDown id="myDropDown"
          label="Style:"
          onAction="OnStyleSelected"
          getSelectedItemIndex="GetStyleIndex"
          showItemImage="true"
          showItemLabel="true">
  <item id="style1" label="Normal" imageMso="StyleNormal"/>
  <item id="style2" label="Bold"   imageMso="Bold"/>
  <button id="moreBtn" label="More Styles..." onAction="OnMoreStyles"/>
</dropDown>
```

**Unique attributes:**

| Attribute | Description |
|-----------|-------------|
| `getSelectedItemID` | Callback: returns ID of selected item |
| `getSelectedItemIndex` | Callback: returns 0-based index of selected item |
| `showItemLabel` | boolean — show labels in dropdown |
| `showItemImage` | boolean — show images in dropdown |
| All `getItem*` callbacks | Same as comboBox |

`onAction` callback receives `(control, selectedId, selectedIndex)`.

---

## `gallery`

A grid-style dropdown (like the font colour picker). Extends `dropDown` with grid layout.

```xml
<gallery id="myGallery"
         label="Color"
         columns="4"
         rows="3"
         itemWidth="32"
         itemHeight="32"
         onAction="OnColorSelected"
         getItemCount="GetColorCount"
         getItemImage="GetColorImage"
         getItemLabel="GetColorLabel">
</gallery>
```

**Unique attributes (in addition to dropDown):**

| Attribute | Description |
|-----------|-------------|
| `columns` | Number of columns (1–1024) |
| `rows` | Number of rows (1–1024) |
| `itemWidth` | Item width in pixels (1–4096) |
| `itemHeight` | Item height in pixels (1–4096) |
| `getItemWidth` | Callback: returns item width |
| `getItemHeight` | Callback: returns item height |
| `showItemLabel` | boolean — show labels under items |
| `size` / `getSize` | `"normal"` or `"large"` (for ribbon placement) |
| `invalidateContentOnDrop` | boolean |

`showInRibbon` attribute exists but is not supported in Ribbon Extensibility documents.

---

## `menu`

A dropdown menu containing other controls. Controls nest recursively.

```xml
<menu id="myMenu"
      label="Options"
      imageMso="OptionsDialog"
      size="large"
      itemSize="normal">
  <button id="opt1" label="Option 1" onAction="OnOpt1"/>
  <menuSeparator id="sep1" title="Advanced"/>
  <button id="opt2" label="Advanced Option" onAction="OnOpt2"/>
  <menu id="subMenu" label="Sub Menu">
    <button id="sub1" label="Sub Item" onAction="OnSub1"/>
  </menu>
</menu>
```

**Attributes:**

| Attribute | Description |
|-----------|-------------|
| `itemSize` | `"normal"` or `"large"` — large shows `description` below label |
| `size` / `getSize` | `"normal"` or `"large"` for the button itself |
| `description` / `getDescription` | Extended description |

Menu contents can include: `button`, `checkBox`, `gallery`, `toggleButton`, `menuSeparator`,
`control` (clone), `splitButton`, `menu`, `dynamicMenu`.

`menuSeparator` attributes: `id`, `idQ`, `tag`, `title`, `getTitle`, positioning attributes.

---

## `dynamicMenu`

A menu whose content is generated at runtime via a `getContent` callback that returns
XML string. `getContent` is **required**.

```xml
<dynamicMenu id="myDynMenu"
             label="Recent Files"
             imageMso="FileOpen"
             size="large"
             getContent="GetRecentFilesContent"
             invalidateContentOnDrop="true"/>
```

The `getContent` callback returns an XML string with a `<menu>` root element:

```python
def GetRecentFilesContent(control):
    return '''<menu xmlns="http://schemas.microsoft.com/office/2009/07/customui">
      <button id="f1" label="File1.xlsx" onAction="OpenFile1"/>
      <button id="f2" label="File2.xlsx" onAction="OpenFile2"/>
    </menu>'''
```

**Unique attributes:**

| Attribute | Description |
|-----------|-------------|
| `getContent` | **Required** callback returning XML string |
| `invalidateContentOnDrop` | boolean — re-fetch content each time dropdown opens |
| `size` / `getSize` | Button size |

---

## `splitButton`

A combined button + dropdown arrow. The button part (or toggle button) gets `onAction`;
the arrow opens a menu. The `label`, `image`, `screentip`, and `supertip` come from the
inner button, not from the `splitButton` element itself.

```xml
<splitButton id="mySplit" size="large">
  <button id="splitBtn"
          label="Save"
          imageMso="FileSave"
          onAction="OnSave"/>
  <menu id="splitMenu">
    <button id="saveAs" label="Save As..." onAction="OnSaveAs"/>
    <button id="saveAll" label="Save All" onAction="OnSaveAll"/>
  </menu>
</splitButton>
```

The inner button can be `button` or `toggleButton`. The menu is a `menu` element.
`splitButton` attributes: `id`, `idQ`, `tag`, `enabled`, `getEnabled`, `visible`, `getVisible`,
`keytip`, `getKeytip`, `insertAfterMso`, etc. (but NOT `label`, `image`, `screentip` — those
come from the inner button).

`size` / `getSize` is available on the `splitButton` element.

---

## `box`

An invisible layout container. Groups controls horizontally or vertically without the visual
group border.

```xml
<box id="myBox" boxStyle="horizontal" visible="true">
  <button id="b1" label="A" onAction="OnA"/>
  <button id="b2" label="B" onAction="OnB"/>
</box>
```

**Attributes:** `id`, `idQ`, `tag`, `visible`, `getVisible`, `boxStyle` (`"horizontal"` or
`"vertical"`), positioning attributes.

Can contain all controls from `EG_Controls` (same as group).

---

## `buttonGroup`

A horizontal container that renders its controls with an integrated, connected look
(no separating borders). Narrower control set than `box`.

```xml
<buttonGroup id="myBtnGroup">
  <button id="bg1" label="Left"  onAction="OnLeft"/>
  <button id="bg2" label="Right" onAction="OnRight"/>
  <separator id="bgSep"/>
  <toggleButton id="bg3" label="Lock" onAction="OnLock" getPressed="GetLocked"/>
</buttonGroup>
```

Allowed children: `control` (clone), `button`, `toggleButton`, `gallery`, `menu`,
`dynamicMenu`, `splitButton`, `separator`.

**Attributes:** `id`, `idQ`, `tag`, `visible`, `getVisible`, positioning attributes.

---

## `labelControl`

Shows text only (no image, no action). Useful for section headings within a group.

```xml
<labelControl id="myLabel" label="Status: Ready"/>
```

No `image`, `imageMso`, `getImage`, `showImage`, `keytip`, `getKeytip` attributes.
No `onAction`. Label can be dynamic via `getLabel`.

---

## `control` (clone)

References an existing control (built-in or custom) to reuse it in another location,
or to override its enabled/visible/label state.

In a ribbon group, `control` can clone a built-in control with optional size override:

```xml
<!-- Clone built-in Save with large size -->
<control idMso="FileSave" size="large"/>
```

In a menu or buttonGroup, `control` clones by `idMso` or `idQ` (not `id` — custom
controls can't be cloned by `id` in menus).

The `onAction` attribute is **prohibited** on clones — action is inherited.
