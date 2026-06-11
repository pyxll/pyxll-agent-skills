# Windows & Views

## Pane

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Index: Any`
- `Parent: Any`
- `ScrollColumn: Any`
- `ScrollRow: Any`
- `VisibleRange: Range`

**Methods:**
- `Activate() -> bool`
- `LargeScroll(Down?, Up?, ToRight?, ToLeft?) -> Any`
- `PointsToScreenPixelsX(Points: int) -> int`
- `PointsToScreenPixelsY(Points: int) -> int`
- `ScrollIntoView(Left: int, Top: int, Width: int, Height: int, Start?) -> None`
- `SmallScroll(Down?, Up?, ToRight?, ToLeft?) -> Any`

## Panes

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> Pane`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> Pane`
- `Item(Index: int) -> Pane`

## ProtectedViewWindow

**Properties:**
- `Caption: Any`
- `EnableResize: Any`
- `Height: Any`
- `Left: Any`
- `SourceName: Any`
- `SourcePath: Any`
- `Top: Any`
- `Visible: Any`
- `Width: Any`
- `WindowState: XlProtectedViewWindowState`
- `Workbook: Workbook`

**Methods:**
- `__call__() -> Any`
- `Activate() -> None`
- `Close() -> bool`
- `Edit(WriteResPassword?, UpdateLinks?) -> Workbook`

## ProtectedViewWindows

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ProtectedViewWindow`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Open(Filename: str, Password?, AddToMru?, RepairMode?) -> ProtectedViewWindow`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ProtectedViewWindow`
- `Item(Index) -> ProtectedViewWindow`

## SheetViews

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

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## Window

**Properties:**
- `ActiveCell: Range`
- `ActiveChart: Chart`
- `ActivePane: Pane`
- `ActiveSheet: Any`
- `ActiveSheetView: Any`
- `Application: Application`
- `AutoFilterDateGrouping: Any`
- `Caption: Any`
- `Creator: XlCreator`
- `DisplayFormulas: Any`
- `DisplayGridlines: Any`
- `DisplayHeadings: Any`
- `DisplayHorizontalScrollBar: Any`
- `DisplayOutline: Any`
- `DisplayRightToLeft: Any`
- `DisplayRuler: Any`
- `DisplayVerticalScrollBar: Any`
- `DisplayWhitespace: Any`
- `DisplayWorkbookTabs: Any`
- `DisplayZeros: Any`
- `EnableResize: Any`
- `FreezePanes: Any`
- `GridlineColor: Any`
- `GridlineColorIndex: XlColorIndex`
- `Height: Any`
- `Hwnd: Any`
- `Index: Any`
- `Left: Any`
- `OnWindow: Any`
- `Panes: Panes`
- `Parent: Any`
- `RangeSelection: Range`
- `ScrollColumn: Any`
- `ScrollRow: Any`
- `SelectedSheets: Sheets`
- `Selection: Any`
- `SheetViews: SheetViews`
- `Split: Any`
- `SplitColumn: Any`
- `SplitHorizontal: Any`
- `SplitRow: Any`
- `SplitVertical: Any`
- `TabRatio: Any`
- `Top: Any`
- `Type: XlWindowType`
- `UsableHeight: Any`
- `UsableWidth: Any`
- `View: XlWindowView`
- `Visible: Any`
- `VisibleRange: Range`
- `Width: Any`
- `WindowNumber: Any`
- `WindowState: XlWindowState`
- `Zoom: Any`

**Methods:**
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> Any`
- `Activate() -> Any`
- `ActivateNext() -> Any`
- `ActivatePrevious() -> Any`
- `Close(SaveChanges?, Filename?, RouteWorkbook?) -> bool`
- `LargeScroll(Down?, Up?, ToRight?, ToLeft?) -> Any`
- `NewWindow() -> Window`
- `PointsToScreenPixelsX(Points: int) -> int`
- `PointsToScreenPixelsY(Points: int) -> int`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> Any`
- `PrintPreview(EnableChanges?) -> Any`
- `RangeFromPoint(x: int, y: int) -> Dispatch`
- `ScrollIntoView(Left: int, Top: int, Width: int, Height: int, Start?) -> None`
- `ScrollWorkbookTabs(Sheets?, Position?) -> Any`
- `SmallScroll(Down?, Up?, ToRight?, ToLeft?) -> Any`

## Windows

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `SyncScrollingSideBySide: Any`

**Methods:**
- `__call__(Index) -> Window`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Arrange(ArrangeStyle: XlArrangeStyle?, ActiveWorkbook?, SyncHorizontal?, SyncVertical?) -> Any`
- `BreakSideBySide() -> bool`
- `CompareSideBySideWith(WindowName) -> bool`
- `ResetPositionsSideBySide() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Window`
- `Item(Index) -> Window`

