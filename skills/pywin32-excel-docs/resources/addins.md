# Add-ins, Dialogs & Legacy UI

## Action

**Properties:**
- `Application: Application`
- `Caption: Any`
- `Content: Any`
- `Coordinate: Any`
- `Creator: XlCreator`
- `Name: Any`
- `Parent: Any`
- `Type: XlActionType`

**Methods:**
- `Execute() -> None`

## Actions

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Action`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Action`
- `Item(Index) -> Action`

## AddIn

**Properties:**
- `Application: Application`
- `Author: Any`
- `CLSID: Any`
- `Comments: Any`
- `Creator: XlCreator`
- `FullName: Any`
- `Installed: Any`
- `IsOpen: Any`
- `Keywords: Any`
- `Name: Any`
- `Parent: Any`
- `Path: Any`
- `progID: Any`
- `Subject: Any`
- `Title: Any`

## AddIns

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> AddIn`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Filename: str, CopyFile?) -> AddIn`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> AddIn`
- `Item(Index) -> AddIn`

## AddIns2

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> AddIn`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Filename: str, CopyFile?) -> AddIn`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> AddIn`
- `Item(Index) -> AddIn`

## Author

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Name: Any`
- `Parent: Any`
- `ProviderID: Any`
- `UserID: Any`

## AutoCorrect

**Properties:**
- `Application: Application`
- `AutoExpandListRange: Any`
- `AutoFillFormulasInLists: Any`
- `CapitalizeNamesOfDays: Any`
- `CorrectCapsLock: Any`
- `CorrectSentenceCap: Any`
- `Creator: XlCreator`
- `DisplayAutoCorrectOptions: Any`
- `KeepGeneralFormatDigitsWithEAsText: Any`
- `KeepGeneralFormatLargeNumbersAsText: Any`
- `KeepGeneralFormatLeadingZerosAsText: Any`
- `Parent: Any`
- `ReplacementList: Any`
- `ReplaceText: Any`
- `TwoInitialCapitals: Any`

**Methods:**
- `AddReplacement(What: str, Replacement: str) -> Any`
- `DeleteReplacement(What: str) -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `GetReplacementList(Index?) -> Any`
- `SetReplacementList(Index, arg1) -> None`

## DefaultPivotTableLayoutOptions

**Properties:**
- `AllowMultipleFilters: Any`
- `Application: Application`
- `CalculatedMembersInFilters: Any`
- `ColumnGrand: Any`
- `CompactRowIndent: Any`
- `Creator: XlCreator`
- `DisplayContextTooltips: Any`
- `DisplayEmptyColumn: Any`
- `DisplayEmptyRow: Any`
- `DisplayErrorString: Any`
- `DisplayFieldCaptions: Any`
- `DisplayImmediateItems: Any`
- `DisplayMemberPropertyTooltips: Any`
- `DisplayNullString: Any`
- `EnableDrilldown: Any`
- `EnableWriteback: Any`
- `ErrorString: Any`
- `FieldListSortAscending: Any`
- `HasAutoFormat: Any`
- `InGridDropZones: Any`
- `LayoutBlankLine: Any`
- `MergeLabels: Any`
- `NullString: Any`
- `PageFieldOrder: Any`
- `PageFieldWrapCount: Any`
- `Parent: Any`
- `PreserveFormatting: Any`
- `PrintDrillIndicators: Any`
- `PrintTitles: Any`
- `RefreshOnFileOpen: Any`
- `RepeatAllLabels: XlPivotFieldRepeatLabels`
- `RepeatItemsOnEachPrintedPage: Any`
- `RowAxisLayout: XlLayoutRowType`
- `RowGrand: Any`
- `SaveData: Any`
- `ShowDrillIndicators: Any`
- `ShowValuesRow: Any`
- `SortUsingCustomLists: Any`
- `SubtotalHiddenPageItems: Any`
- `SubtotalLocation: Any`
- `Subtotals: Any`
- `TotalsAnnotation: Any`
- `ViewCalculatedMembers: Any`
- `VisualTotals: Any`
- `VisualTotalsForSets: Any`
- `xlMissingItemsNone: Any`

## Dialog

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `Show(Arg1?, Arg2?, Arg3?, Arg4?, Arg5?, Arg6?, Arg7?, Arg8?, Arg9?, Arg10?, Arg11?, Arg12?, Arg13?, Arg14?, Arg15?, Arg16?, Arg17?, Arg18?, Arg19?, Arg20?, Arg21?, Arg22?, Arg23?, Arg24?, Arg25?, Arg26?, Arg27?, Arg28?, Arg29?, Arg30?) -> bool`

## Dialogs

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: XlBuiltInDialog) -> Dialog`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: XlBuiltInDialog) -> Dialog`
- `Item(Index: XlBuiltInDialog) -> Dialog`

## FileExportConverter

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Description: Any`
- `Extensions: Any`
- `FileFormat: Any`
- `Parent: Any`

## FileExportConverters

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> FileExportConverter`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> FileExportConverter`
- `Item(Index) -> FileExportConverter`

## HeaderFooter

**Properties:**
- `Picture: Graphic`
- `Text: Any`

## Menu

**Properties:**
- `Application: Application`
- `Caption: Any`
- `Creator: XlCreator`
- `Enabled: Any`
- `Index: Any`
- `MenuItems: MenuItems`
- `Parent: Any`

**Methods:**
- `Delete() -> None`

## MenuBar

**Properties:**
- `Application: Application`
- `BuiltIn: Any`
- `Caption: Any`
- `Creator: XlCreator`
- `Index: Any`
- `Menus: Menus`
- `Parent: Any`

**Methods:**
- `Activate() -> None`
- `Delete() -> None`
- `Reset() -> None`

## MenuBars

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> MenuBar`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name?) -> MenuBar`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> MenuBar`
- `Item(Index) -> MenuBar`

## MenuItem

**Properties:**
- `Application: Application`
- `Caption: Any`
- `Checked: Any`
- `Creator: XlCreator`
- `Enabled: Any`
- `HelpContextID: Any`
- `HelpFile: Any`
- `Index: Any`
- `OnAction: Any`
- `Parent: Any`
- `StatusBar: Any`

**Methods:**
- `Delete() -> None`

## MenuItems

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Caption: str, OnAction?, ShortcutKey?, Before?, Restore?, StatusBar?, HelpFile?, HelpContextID?) -> MenuItem`
- `AddMenu(Caption: str, Before?, Restore?) -> Menu`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## Menus

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Menu`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Caption: str, Before?, Restore?) -> Menu`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Menu`
- `Item(Index) -> Menu`

## Page

**Properties:**
- `CenterFooter: HeaderFooter`
- `CenterHeader: HeaderFooter`
- `LeftFooter: HeaderFooter`
- `LeftHeader: HeaderFooter`
- `RightFooter: HeaderFooter`
- `RightHeader: HeaderFooter`

## Pages

**Properties:**
- `Count: Any`

**Methods:**
- `__call__(Index) -> Page`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Page`
- `Item(Index) -> Page`

## RecentFile

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Index: Any`
- `Name: Any`
- `Parent: Any`
- `Path: Any`

**Methods:**
- `Delete() -> None`
- `Open() -> Workbook`

## RecentFiles

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Maximum: Any`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> RecentFile`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str) -> RecentFile`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> RecentFile`
- `Item(Index: int) -> RecentFile`

## SoundNote

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `Import(Filename: str) -> Any`
- `Play() -> Any`
- `Record() -> Any`

## Toolbar

**Properties:**
- `Application: Application`
- `BuiltIn: Any`
- `Creator: XlCreator`
- `Height: Any`
- `Left: Any`
- `Name: Any`
- `Parent: Any`
- `Position: Any`
- `Protection: XlToolbarProtection`
- `ToolbarButtons: ToolbarButtons`
- `Top: Any`
- `Visible: Any`
- `Width: Any`

**Methods:**
- `Delete() -> None`
- `Reset() -> None`

## ToolbarButton

**Properties:**
- `Application: Application`
- `BuiltIn: Any`
- `BuiltInFace: Any`
- `Creator: XlCreator`
- `Enabled: Any`
- `HelpContextID: Any`
- `HelpFile: Any`
- `ID: Any`
- `IsGap: Any`
- `Name: Any`
- `OnAction: Any`
- `Parent: Any`
- `Pushed: Any`
- `StatusBar: Any`
- `Width: Any`

**Methods:**
- `Copy(Toolbar: Toolbar, Before: int) -> None`
- `CopyFace() -> None`
- `Delete() -> None`
- `Edit() -> None`
- `Move(Toolbar: Toolbar, Before: int) -> None`
- `PasteFace() -> None`
- `Reset() -> None`

## ToolbarButtons

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> ToolbarButton`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Button?, Before?, OnAction?, Pushed?, Enabled?, StatusBar?, HelpFile?, HelpContextID?) -> ToolbarButton`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> ToolbarButton`
- `Item(Index: int) -> ToolbarButton`

## Toolbars

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Toolbar`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name?) -> Toolbar`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Toolbar`
- `Item(Index) -> Toolbar`

## TreeviewControl

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Drilled: Any`
- `Hidden: Any`
- `Parent: Any`

