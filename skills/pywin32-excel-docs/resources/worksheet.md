# Worksheet & Worksheets

## AutoFilter

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `FilterMode: Any`
- `Filters: Filters`
- `Parent: Any`
- `Range: Range`
- `Sort: Sort`

**Methods:**
- `ApplyFilter() -> None`
- `ShowAllData() -> None`

## DialogSheet

**Properties:**
- `Application: Application`
- `AutoFilter: AutoFilter`
- `CodeName: Any`
- `Comments: Comments`
- `CommentsThreaded: CommentsThreaded`
- `Creator: XlCreator`
- `CustomProperties: CustomProperties`
- `DefaultButton: Any`
- `DialogFrame: DialogFrame`
- `DisplayAutomaticPageBreaks: Any`
- `DisplayPageBreaks: Any`
- `DisplayRightToLeft: Any`
- `EnableAutoFilter: Any`
- `EnableCalculation: Any`
- `EnableFormatConditionsCalculation: Any`
- `EnableOutlining: Any`
- `EnablePivotTable: Any`
- `EnableSelection: XlEnableSelection`
- `Focus: Any`
- `HPageBreaks: HPageBreaks`
- `Hyperlinks: Hyperlinks`
- `Index: Any`
- `MailEnvelope: MsoEnvelope`
- `Name: Any`
- `NamedSheetViews: NamedSheetViewCollection`
- `Names: Names`
- `Next: Any`
- `OnDoubleClick: Any`
- `OnSheetActivate: Any`
- `OnSheetDeactivate: Any`
- `PageSetup: PageSetup`
- `Parent: Any`
- `Previous: Any`
- `PrintedCommentPages: Any`
- `ProtectContents: Any`
- `ProtectDrawingObjects: Any`
- `Protection: Protection`
- `ProtectionMode: Any`
- `ProtectScenarios: Any`
- `QueryTables: QueryTables`
- `Scripts: Scripts`
- `ScrollArea: Any`
- `Shapes: Shapes`
- `SmartTags: SmartTags`
- `Sort: Sort`
- `Tab: Tab`
- `Visible: XlSheetVisibility`
- `VPageBreaks: VPageBreaks`

**Methods:**
- `_CheckSpelling(CustomDictionary?, IgnoreUppercase?, AlwaysSuggest?, SpellLang?, IgnoreFinalYaa?, SpellScript?) -> None`
- `_Evaluate(Name) -> Any`
- `_ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?) -> None`
- `_PasteSpecial(Format?, Link?, DisplayAsIcon?, IconFileName?, IconIndex?, IconLabel?) -> None`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `_Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?) -> None`
- `_SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `_SaveAs_(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `Activate() -> None`
- `Arcs(Index?) -> Dispatch`
- `Buttons(Index?) -> Dispatch`
- `ChartObjects(Index?) -> Dispatch`
- `CheckBoxes(Index?) -> Dispatch`
- `CheckSpelling(CustomDictionary?, IgnoreUppercase?, AlwaysSuggest?, SpellLang?) -> None`
- `CircleInvalid() -> None`
- `ClearCircles() -> None`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `DrawingObjects(Index?) -> Dispatch`
- `Drawings(Index?) -> Dispatch`
- `DropDowns(Index?) -> Dispatch`
- `EditBoxes(Index?) -> Dispatch`
- `Evaluate(Name) -> Any`
- `ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?, WorkIdentity?) -> None`
- `GroupBoxes(Index?) -> Dispatch`
- `GroupObjects(Index?) -> Dispatch`
- `Hide(Cancel?) -> bool`
- `Labels(Index?) -> Dispatch`
- `Lines(Index?) -> Dispatch`
- `ListBoxes(Index?) -> Dispatch`
- `Move(Before?, After?) -> None`
- `OLEObjects(Index?) -> Dispatch`
- `OptionButtons(Index?) -> Dispatch`
- `Ovals(Index?) -> Dispatch`
- `Paste(Destination?, Link?) -> None`
- `PasteSpecial(Format?, Link?, DisplayAsIcon?, IconFileName?, IconIndex?, IconLabel?, NoHTMLFormatting?) -> None`
- `Pictures(Index?) -> Dispatch`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?, AllowFormattingCells?, AllowFormattingColumns?, AllowFormattingRows?, AllowInsertingColumns?, AllowInsertingRows?, AllowInsertingHyperlinks?, AllowDeletingColumns?, AllowDeletingRows?, AllowSorting?, AllowFiltering?, AllowUsingPivotTables?) -> None`
- `Rectangles(Index?) -> Dispatch`
- `ResetAllPageBreaks() -> None`
- `SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `ScrollBars(Index?) -> Dispatch`
- `Select(Replace?) -> None`
- `Show() -> bool`
- `Spinners(Index?) -> Dispatch`
- `TextBoxes(Index?) -> Dispatch`
- `Unprotect(Password?) -> None`

## DialogSheetView

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `Sheet: Any`

## DialogSheets

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `HPageBreaks: HPageBreaks`
- `Parent: Any`
- `Visible: Any`
- `VPageBreaks: VPageBreaks`

**Methods:**
- `__call__(Index) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `Add(Before?, After?, Count?) -> DialogSheet`
- `Add2(Before?, After?, Count?, NewLayout?) -> Dispatch`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `Move(Before?, After?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Select(Replace?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## Filter

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Criteria1: Any`
- `Criteria2: Any`
- `On: Any`
- `Operator: XlAutoFilterOperator`
- `Parent: Any`

**Methods:**
- `__len__() -> Any`
- `__nonzero__() -> Any`

## Filters

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> Filter`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> Filter`
- `Item(Index: int) -> Filter`

## HPageBreak

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Extent: XlPageBreakExtent`
- `Location: Range`
- `Parent: Worksheet`
- `Type: XlPageBreak`

**Methods:**
- `Delete() -> None`
- `DragOff(Direction: XlDirection, RegionIndex: int) -> None`

## HPageBreaks

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> HPageBreak`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Before: Dispatch) -> HPageBreak`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> HPageBreak`
- `Item(Index: int) -> HPageBreak`

## Module

**Properties:**
- `Application: Application`
- `CodeName: Any`
- `Creator: XlCreator`
- `Index: Any`
- `Name: Any`
- `Next: Any`
- `OnDoubleClick: Any`
- `OnSheetActivate: Any`
- `OnSheetDeactivate: Any`
- `PageSetup: PageSetup`
- `Parent: Any`
- `Previous: Any`
- `ProtectContents: Any`
- `ProtectionMode: Any`
- `Shapes: Shapes`
- `Visible: XlSheetVisibility`

**Methods:**
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `_Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?) -> None`
- `_SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `_SaveAs_(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `Activate() -> None`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `InsertFile(Filename, Merge?) -> Any`
- `Move(Before?, After?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?) -> None`
- `SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `Select(Replace?) -> None`
- `Unprotect(Password?) -> None`

## ModuleView

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `Sheet: Any`

## Modules

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `HPageBreaks: HPageBreaks`
- `Parent: Any`
- `Visible: Any`
- `VPageBreaks: VPageBreaks`

**Methods:**
- `__call__(Index) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `Add(Before?, After?, Count?) -> Module`
- `Add2(Before?, After?, Count?, NewLayout?) -> Dispatch`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `Move(Before?, After?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?, IgnorePrintAreas?) -> None`
- `Select(Replace?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## NamedSheetView

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Activate() -> None`
- `Delete() -> None`
- `Duplicate(Name?) -> NamedSheetView`

## NamedSheetViewCollection

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str) -> NamedSheetView`
- `EnterTemporary() -> NamedSheetView`
- `Exit() -> None`
- `GetActive() -> NamedSheetView`
- `GetItem(Name: str) -> NamedSheetView`
- `GetItemAt(Index: int) -> NamedSheetView`

## Outline

**Properties:**
- `Application: Application`
- `AutomaticStyles: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `SummaryColumn: XlSummaryColumn`
- `SummaryRow: XlSummaryRow`

**Methods:**
- `ShowLevels(RowLevels?, ColumnLevels?) -> Any`

## PageSetup

**Properties:**
- `AlignMarginsHeaderFooter: Any`
- `Application: Application`
- `BlackAndWhite: Any`
- `BottomMargin: Any`
- `CenterFooter: Any`
- `CenterFooterPicture: Graphic`
- `CenterHeader: Any`
- `CenterHeaderPicture: Graphic`
- `CenterHorizontally: Any`
- `CenterVertically: Any`
- `ChartSize: XlObjectSize`
- `Creator: XlCreator`
- `DifferentFirstPageHeaderFooter: Any`
- `Draft: Any`
- `EvenPage: Page`
- `FirstPage: Page`
- `FirstPageNumber: Any`
- `FitToPagesTall: Any`
- `FitToPagesWide: Any`
- `FooterMargin: Any`
- `HeaderMargin: Any`
- `LeftFooter: Any`
- `LeftFooterPicture: Graphic`
- `LeftHeader: Any`
- `LeftHeaderPicture: Graphic`
- `LeftMargin: Any`
- `OddAndEvenPagesHeaderFooter: Any`
- `Order: XlOrder`
- `Orientation: XlPageOrientation`
- `Pages: Pages`
- `PaperSize: XlPaperSize`
- `Parent: Any`
- `PrintArea: Any`
- `PrintComments: XlPrintLocation`
- `PrintErrors: XlPrintErrors`
- `PrintGridlines: Any`
- `PrintHeadings: Any`
- `PrintNotes: Any`
- `PrintQuality: Any`
- `PrintTitleColumns: Any`
- `PrintTitleRows: Any`
- `RightFooter: Any`
- `RightFooterPicture: Graphic`
- `RightHeader: Any`
- `RightHeaderPicture: Graphic`
- `RightMargin: Any`
- `ScaleWithDocHeaderFooter: Any`
- `TopMargin: Any`
- `Zoom: Any`

**Property Accessors** *(parameterized — must be called as method):*
- `GetPrintQuality(Index?) -> Any`
- `SetPrintQuality(Index, arg1) -> None`

## Sheets

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `HPageBreaks: HPageBreaks`
- `Parent: Any`
- `Visible: Any`
- `VPageBreaks: VPageBreaks`

**Methods:**
- `__call__(Index) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `Add(Before?, After?, Count?, Type?) -> Dispatch`
- `Add2(Before?, After?, Count?, NewLayout?) -> Dispatch`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `FillAcrossSheets(Range: Range, Type: XlFillWith?) -> None`
- `Move(Before?, After?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?, IgnorePrintAreas?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Select(Replace?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## Sort

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Header: XlYesNoGuess`
- `MatchCase: Any`
- `Orientation: XlSortOrientation`
- `Parent: Any`
- `Rng: Range`
- `SortFields: SortFields`
- `SortMethod: XlSortMethod`

**Methods:**
- `Apply() -> None`
- `SetRange(Rng: Range) -> None`

## SortField

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `CustomOrder: Any`
- `DataOption: XlSortDataOption`
- `Key: Range`
- `Order: XlSortOrder`
- `Parent: Any`
- `Priority: Any`
- `SortOn: XlSortOn`
- `SortOnValue: Any`
- `SubField: Any`

**Methods:**
- `Delete() -> None`
- `ModifyKey(Key: Range) -> None`
- `SetIcon(Icon: Icon) -> None`

## SortFields

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> SortField`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Key: Range, SortOn?, Order?, CustomOrder?, DataOption?) -> SortField`
- `Add2(Key: Range, SortOn?, Order?, CustomOrder?, DataOption?, SubField?) -> SortField`
- `Clear() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> SortField`
- `Item(Index) -> SortField`

## Tab

**Properties:**
- `Application: Application`
- `Color: Any`
- `ColorIndex: XlColorIndex`
- `Creator: XlCreator`
- `Parent: Any`
- `ThemeColor: XlThemeColor`
- `TintAndShade: Any`

## VPageBreak

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Extent: XlPageBreakExtent`
- `Location: Range`
- `Parent: Worksheet`
- `Type: XlPageBreak`

**Methods:**
- `Delete() -> None`
- `DragOff(Direction: XlDirection, RegionIndex: int) -> None`

## VPageBreaks

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> VPageBreak`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Before: Dispatch) -> VPageBreak`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> VPageBreak`
- `Item(Index: int) -> VPageBreak`

## WorksheetView

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DisplayFormulas: Any`
- `DisplayGridlines: Any`
- `DisplayHeadings: Any`
- `DisplayOutline: Any`
- `DisplayZeros: Any`
- `Parent: Any`
- `Sheet: Any`

## Worksheets

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `HPageBreaks: HPageBreaks`
- `Parent: Any`
- `Visible: Any`
- `VPageBreaks: VPageBreaks`

**Methods:**
- `__call__(Index) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `Add(Before?, After?, Count?, Type?) -> Dispatch`
- `Add2(Before?, After?, Count?, NewLayout?) -> Dispatch`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `FillAcrossSheets(Range: Range, Type: XlFillWith?) -> None`
- `Move(Before?, After?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?, IgnorePrintAreas?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Select(Replace?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## Worksheet
*Bases: _Worksheet*

## _Worksheet

**Properties:**
- `Application: Application`
- `AutoFilter: AutoFilter`
- `AutoFilterMode: Any`
- `Cells: Range`
- `CircularReference: Range`
- `CodeName: Any`
- `Columns: Range`
- `Comments: Comments`
- `CommentsThreaded: CommentsThreaded`
- `ConsolidationFunction: XlConsolidationFunction`
- `ConsolidationOptions: Any`
- `ConsolidationSources: Any`
- `Creator: XlCreator`
- `CustomProperties: CustomProperties`
- `DisplayAutomaticPageBreaks: Any`
- `DisplayPageBreaks: Any`
- `DisplayRightToLeft: Any`
- `EnableAutoFilter: Any`
- `EnableCalculation: Any`
- `EnableFormatConditionsCalculation: Any`
- `EnableOutlining: Any`
- `EnablePivotTable: Any`
- `EnableSelection: XlEnableSelection`
- `FilterMode: Any`
- `HPageBreaks: HPageBreaks`
- `Hyperlinks: Hyperlinks`
- `Index: Any`
- `ListObjects: ListObjects`
- `MailEnvelope: MsoEnvelope`
- `Name: Any`
- `NamedSheetViews: NamedSheetViewCollection`
- `Names: Names`
- `Next: Any`
- `OnCalculate: Any`
- `OnData: Any`
- `OnDoubleClick: Any`
- `OnEntry: Any`
- `OnSheetActivate: Any`
- `OnSheetDeactivate: Any`
- `Outline: Outline`
- `PageSetup: PageSetup`
- `Parent: Any`
- `Previous: Any`
- `PrintedCommentPages: Any`
- `ProtectContents: Any`
- `ProtectDrawingObjects: Any`
- `Protection: Protection`
- `ProtectionMode: Any`
- `ProtectScenarios: Any`
- `QueryTables: QueryTables`
- `Rows: Range`
- `Scripts: Scripts`
- `ScrollArea: Any`
- `Shapes: Shapes`
- `SmartTags: SmartTags`
- `Sort: Sort`
- `StandardHeight: Any`
- `StandardWidth: Any`
- `Tab: Tab`
- `TransitionExpEval: Any`
- `TransitionFormEntry: Any`
- `Type: XlSheetType`
- `UsedRange: Range`
- `Visible: XlSheetVisibility`
- `VPageBreaks: VPageBreaks`

**Methods:**
- `_CheckSpelling(CustomDictionary?, IgnoreUppercase?, AlwaysSuggest?, SpellLang?, IgnoreFinalYaa?, SpellScript?) -> None`
- `_Evaluate(Name) -> Any`
- `_ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?) -> None`
- `_PasteSpecial(Format?, Link?, DisplayAsIcon?, IconFileName?, IconIndex?, IconLabel?) -> None`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `_Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?) -> None`
- `_SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `_SaveAs_(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `Activate() -> None`
- `Arcs(Index?) -> Dispatch`
- `Buttons(Index?) -> Dispatch`
- `Calculate() -> None`
- `ChartObjects(Index?) -> Dispatch`
- `CheckBoxes(Index?) -> Dispatch`
- `CheckSpelling(CustomDictionary?, IgnoreUppercase?, AlwaysSuggest?, SpellLang?) -> None`
- `CircleInvalid() -> None`
- `ClearArrows() -> None`
- `ClearCircles() -> None`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `DrawingObjects(Index?) -> Dispatch`
- `Drawings(Index?) -> Dispatch`
- `DropDowns(Index?) -> Dispatch`
- `Evaluate(Name) -> Any`
- `ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?, WorkIdentity?) -> None`
- `GroupBoxes(Index?) -> Dispatch`
- `GroupObjects(Index?) -> Dispatch`
- `Labels(Index?) -> Dispatch`
- `Lines(Index?) -> Dispatch`
- `ListBoxes(Index?) -> Dispatch`
- `Move(Before?, After?) -> None`
- `OLEObjects(Index?) -> Dispatch`
- `OptionButtons(Index?) -> Dispatch`
- `Ovals(Index?) -> Dispatch`
- `Paste(Destination?, Link?) -> None`
- `PasteSpecial(Format?, Link?, DisplayAsIcon?, IconFileName?, IconIndex?, IconLabel?, NoHTMLFormatting?) -> None`
- `Pictures(Index?) -> Dispatch`
- `PivotTables(Index?) -> Dispatch`
- `PivotTableWizard(SourceType?, SourceData?, TableDestination?, TableName?, RowGrand?, ColumnGrand?, SaveData?, HasAutoFormat?, AutoPage?, Reserved?, BackgroundQuery?, OptimizeCache?, PageFieldOrder?, PageFieldWrapCount?, ReadData?, Connection?) -> PivotTable`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?, IgnorePrintAreas?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?, AllowFormattingCells?, AllowFormattingColumns?, AllowFormattingRows?, AllowInsertingColumns?, AllowInsertingRows?, AllowInsertingHyperlinks?, AllowDeletingColumns?, AllowDeletingRows?, AllowSorting?, AllowFiltering?, AllowUsingPivotTables?) -> None`
- `Rectangles(Index?) -> Dispatch`
- `ResetAllPageBreaks() -> None`
- `SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `Scenarios(Index?) -> Dispatch`
- `ScrollBars(Index?) -> Dispatch`
- `Select(Replace?) -> None`
- `SetBackgroundPicture(Filename: str) -> None`
- `ShowAllData() -> None`
- `ShowDataForm() -> None`
- `Spinners(Index?) -> Dispatch`
- `TextBoxes(Index?) -> Dispatch`
- `Unprotect(Password?) -> None`
- `XmlDataQuery(XPath: str, SelectionNamespaces?, Map?) -> Range`
- `XmlMapQuery(XPath: str, SelectionNamespaces?, Map?) -> Range`

**Property Accessors** *(parameterized — must be called as method):*
- `Range(Cell1, Cell2?) -> Range`

