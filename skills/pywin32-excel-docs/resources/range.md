# Range, Names & Cells

## Areas

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> Range`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> Range`
- `Item(Index: int) -> Range`

## Comment

**Properties:**
- `Application: Application`
- `Author: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `Shape: Shape`
- `Visible: Any`

**Methods:**
- `Delete() -> None`
- `Next() -> Comment`
- `Previous() -> Comment`
- `Text(Text?, Start?, Overwrite?) -> str`

## CommentThreaded

**Properties:**
- `Application: Application`
- `Author: Author`
- `Creator: XlCreator`
- `Date: Any`
- `Parent: Any`
- `Replies: CommentsThreaded`
- `Resolved: Any`

**Methods:**
- `AddReply(Text?) -> CommentThreaded`
- `Delete() -> None`
- `Next() -> CommentThreaded`
- `Previous() -> CommentThreaded`
- `Text(Text?, Start?, Overwrite?) -> str`

## Comments

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> Comment`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index: int) -> Comment`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> Comment`

## CommentsThreaded

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> CommentThreaded`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index: int) -> CommentThreaded`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> CommentThreaded`

## CustomProperties

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> CustomProperty`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str, Value) -> CustomProperty`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> CustomProperty`
- `Item(Index) -> CustomProperty`

## CustomProperty

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Name: Any`
- `Parent: Any`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## Error

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Ignore: Any`
- `Parent: Any`
- `Value: Any`

**Methods:**
- `__call__() -> Any`

## Errors

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Error`
- `__getitem__(key) -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Error`
- `Item(Index) -> Error`

## Hyperlink

**Properties:**
- `Address: Any`
- `Application: Application`
- `Creator: XlCreator`
- `EmailSubject: Any`
- `Name: Any`
- `Parent: Any`
- `Range: Range`
- `ScreenTip: Any`
- `Shape: Shape`
- `SubAddress: Any`
- `TextToDisplay: Any`
- `Type: Any`

**Methods:**
- `AddToFavorites() -> None`
- `CreateNewDocument(Filename: str, EditNow: bool, Overwrite: bool) -> None`
- `Delete() -> None`
- `Follow(NewWindow?, AddHistory?, ExtraInfo?, Method?, HeaderInfo?) -> None`

## Hyperlinks

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Hyperlink`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Anchor: Dispatch, Address: str, SubAddress?, ScreenTip?, TextToDisplay?) -> Dispatch`
- `Delete() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Hyperlink`
- `Item(Index) -> Hyperlink`

## Name

**Properties:**
- `Application: Application`
- `Category: Any`
- `CategoryLocal: Any`
- `Comment: Any`
- `Creator: XlCreator`
- `Index: Any`
- `MacroType: XlXLMMacroType`
- `Name: Any`
- `NameLocal: Any`
- `Parent: Any`
- `RefersTo: Any`
- `RefersToLocal: Any`
- `RefersToR1C1: Any`
- `RefersToR1C1Local: Any`
- `RefersToRange: Range`
- `ShortcutKey: Any`
- `ValidWorkbookParameter: Any`
- `Value: Any`
- `Visible: Any`
- `WorkbookParameter: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## Names

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index?, IndexLocal?, RefersTo?) -> Name`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index?, IndexLocal?, RefersTo?) -> Name`
- `Add(Name?, RefersTo?, Visible?, MacroType?, ShortcutKey?, Category?, NameLocal?, RefersToLocal?, CategoryLocal?, RefersToR1C1?, RefersToR1C1Local?) -> Name`
- `Item(Index?, IndexLocal?, RefersTo?) -> Name`

## Phonetic

**Properties:**
- `Alignment: Any`
- `Application: Application`
- `CharacterType: Any`
- `Creator: XlCreator`
- `Font: Font`
- `Parent: Any`
- `Text: Any`
- `Visible: Any`

## Phonetics

**Properties:**
- `Alignment: Any`
- `Application: Application`
- `CharacterType: Any`
- `Count: Any`
- `Creator: XlCreator`
- `Font: Font`
- `Length: Any`
- `Parent: Any`
- `Start: Any`
- `Text: Any`
- `Visible: Any`

**Methods:**
- `__call__(Index: int) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Start: int, Length: int, Text: str) -> None`
- `Delete() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> Dispatch`
- `Item(Index: int) -> Dispatch`

## PivotTableChangeList

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ValueChange`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Tuple: str, Value: float, AllocationValue?, AllocationMethod?, AllocationWeightExpression?) -> ValueChange`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ValueChange`
- `Item(Index) -> ValueChange`

## QuickAnalysis

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `Hide(XlQuickAnalysisMode: XlQuickAnalysisMode?) -> None`
- `Show(XlQuickAnalysisMode: XlQuickAnalysisMode?) -> None`

## Range

**Properties:**
- `AddIndent: Any`
- `Address: Any`
- `AddressLocal: Any`
- `AllowEdit: Any`
- `Application: Application`
- `Areas: Areas`
- `Borders: Borders`
- `Cells: Range`
- `Characters: Characters`
- `Column: Any`
- `Columns: Range`
- `ColumnWidth: Any`
- `Comment: Comment`
- `CommentThreaded: CommentThreaded`
- `Count: Any`
- `CountLarge: Any`
- `Creator: XlCreator`
- `CurrentArray: Range`
- `CurrentRegion: Range`
- `Dependents: Range`
- `DirectDependents: Range`
- `DirectPrecedents: Range`
- `DisplayFormat: DisplayFormat`
- `EntireColumn: Range`
- `EntireRow: Range`
- `Errors: Errors`
- `Font: Font`
- `FormatConditions: FormatConditions`
- `Formula: Any`
- `Formula2: Any`
- `Formula2Local: Any`
- `Formula2R1C1: Any`
- `Formula2R1C1Local: Any`
- `FormulaArray: Any`
- `FormulaHidden: Any`
- `FormulaLabel: XlFormulaLabel`
- `FormulaLocal: Any`
- `FormulaR1C1: Any`
- `FormulaR1C1Local: Any`
- `HasArray: Any`
- `HasFormula: Any`
- `HasRichDataType: Any`
- `HasSpill: Any`
- `Height: Any`
- `Hidden: Any`
- `HorizontalAlignment: Any`
- `Hyperlinks: Hyperlinks`
- `ID: Any`
- `IndentLevel: Any`
- `Interior: Interior`
- `Left: Any`
- `LinkedDataTypeState: Any`
- `ListHeaderRows: Any`
- `ListObject: ListObject`
- `LocationInTable: XlLocationInTable`
- `Locked: Any`
- `MDX: Any`
- `MergeArea: Range`
- `MergeCells: Any`
- `Name: Any`
- `Next: Range`
- `NumberFormat: Any`
- `NumberFormatLocal: Any`
- `Offset: Range`
- `Orientation: Any`
- `OutlineLevel: Any`
- `PageBreak: Any`
- `Parent: Any`
- `Phonetic: Phonetic`
- `Phonetics: Phonetics`
- `PivotCell: PivotCell`
- `PivotField: PivotField`
- `PivotItem: PivotItem`
- `PivotTable: PivotTable`
- `Precedents: Range`
- `PrefixCharacter: Any`
- `Previous: Range`
- `QueryTable: QueryTable`
- `ReadingOrder: Any`
- `Resize: Range`
- `Row: Any`
- `RowHeight: Any`
- `Rows: Range`
- `SavedAsArray: Any`
- `ServerActions: Actions`
- `ShowDetail: Any`
- `ShrinkToFit: Any`
- `SmartTags: SmartTags`
- `SoundNote: SoundNote`
- `SparklineGroups: SparklineGroups`
- `SpillingToRange: Range`
- `SpillParent: Range`
- `Style: Any`
- `Summary: Any`
- `Text: Any`
- `Top: Any`
- `UseStandardHeight: Any`
- `UseStandardWidth: Any`
- `Validation: Validation`
- `Value: Any`
- `Value2: Any`
- `VerticalAlignment: Any`
- `Width: Any`
- `Worksheet: Worksheet`
- `WrapText: Any`
- `XPath: XPath`

**Methods:**
- `__call__(RowIndex?, ColumnIndex?) -> Any`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_AutoFilter(Field, Criteria1, Operator: XlAutoFilterOperator?, Criteria2?, VisibleDropDown?) -> Any`
- `_BorderAround(LineStyle, Weight: XlBorderWeight?, ColorIndex: XlColorIndex?, Color?) -> Any`
- `_ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?) -> None`
- `_PasteSpecial(Paste: XlPasteType?, Operation: XlPasteSpecialOperation?, SkipBlanks?, Transpose?) -> Any`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> Any`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> Any`
- `_Replace(What, Replacement, LookAt?, SearchOrder?, MatchCase?, MatchByte?, SearchFormat?, ReplaceFormat?) -> bool`
- `_Sort(Key1, Order1: XlSortOrder?, Key2, Type, Order2: XlSortOrder?, Key3, Order3: XlSortOrder?, Header: XlYesNoGuess?, OrderCustom, MatchCase, Orientation: XlSortOrientation?, SortMethod: XlSortMethod?, DataOption1: XlSortDataOption?, DataOption2: XlSortDataOption?, DataOption3: XlSortDataOption?) -> Any`
- `Activate() -> Any`
- `AddComment(Text?) -> Comment`
- `AddCommentThreaded(Text: str) -> CommentThreaded`
- `AdvancedFilter(Action: XlFilterAction, CriteriaRange?, CopyToRange?, Unique?) -> Any`
- `AllocateChanges() -> None`
- `ApplyNames(Names, IgnoreRelativeAbsolute, UseRowColumnNames, OmitColumn, OmitRow, Order: XlApplyNamesOrder?, AppendLast?) -> Any`
- `ApplyOutlineStyles() -> Any`
- `AutoComplete(String: str) -> str`
- `AutoFill(Destination: Range, Type: XlAutoFillType?) -> Any`
- `AutoFilter(Field, Criteria1, Operator: XlAutoFilterOperator?, Criteria2?, VisibleDropDown?, SubField?) -> Any`
- `AutoFit() -> Any`
- `AutoFormat(Format: XlRangeAutoFormat?, Number?, Font?, Alignment?, Border?, Pattern?, Width?) -> Any`
- `AutoOutline() -> Any`
- `BorderAround(LineStyle, Weight: XlBorderWeight?, ColorIndex: XlColorIndex?, Color?, ThemeColor?) -> Any`
- `Calculate() -> Any`
- `CalculateRowMajorOrder() -> Any`
- `CheckSpelling(CustomDictionary?, IgnoreUppercase?, AlwaysSuggest?, SpellLang?) -> Any`
- `Clear() -> Any`
- `ClearComments() -> None`
- `ClearContents() -> Any`
- `ClearFormats() -> Any`
- `ClearHyperlinks() -> None`
- `ClearNotes() -> Any`
- `ClearOutline() -> Any`
- `ColumnDifferences(Comparison) -> Range`
- `Consolidate(Sources?, Function?, TopRow?, LeftColumn?, CreateLinks?) -> Any`
- `ConvertToLinkedDataType(ServiceID: int, LanguageCulture: str) -> None`
- `Copy(Destination?) -> Any`
- `CopyFromRecordset(Data, MaxRows?, MaxColumns?) -> int`
- `CopyPicture(Appearance: XlPictureAppearance?, Format: XlCopyPictureFormat?) -> Any`
- `CreateNames(Top?, Left?, Bottom?, Right?) -> Any`
- `CreatePublisher(Edition, Appearance: XlPictureAppearance?, ContainsPICT?, ContainsBIFF?, ContainsRTF?, ContainsVALU?) -> Any`
- `Cut(Destination?) -> Any`
- `DataSeries(Rowcol, Type: XlDataSeriesType?, Date: XlDataSeriesDate?, Step?, Stop?, Trend?) -> Any`
- `DataTypeToText() -> None`
- `Delete(Shift?) -> Any`
- `DialogBox() -> Any`
- `Dirty() -> None`
- `DiscardChanges() -> None`
- `EditionOptions(Type: XlEditionType, Option: XlEditionOptionsOption, Name, Reference, Appearance: XlPictureAppearance?, ChartSize: XlPictureAppearance?, Format?) -> Any`
- `ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?, WorkIdentity?) -> None`
- `FillDown() -> Any`
- `FillLeft() -> Any`
- `FillRight() -> Any`
- `FillUp() -> Any`
- `Find(What, After, LookIn, LookAt, SearchOrder, SearchDirection: XlSearchDirection?, MatchCase?, MatchByte?, SearchFormat?) -> Range`
- `FindNext(After?) -> Range`
- `FindPrevious(After?) -> Range`
- `FlashFill() -> None`
- `FunctionWizard() -> Any`
- `GoalSeek(Goal, ChangingCell: Range) -> bool`
- `Group(Start?, End?, By?, Periods?) -> Any`
- `Insert(Shift?, CopyOrigin?) -> Any`
- `InsertIndent(InsertAmount: int) -> None`
- `Justify() -> Any`
- `ListNames() -> Any`
- `Merge(Across?) -> None`
- `NavigateArrow(TowardPrecedent?, ArrowNumber?, LinkNumber?) -> Any`
- `NoteText(Text?, Start?, Length?) -> str`
- `Parse(ParseLine?, Destination?) -> Any`
- `PasteSpecial(Paste: XlPasteType?, Operation: XlPasteSpecialOperation?, SkipBlanks?, Transpose?) -> Any`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> Any`
- `PrintPreview(EnableChanges?) -> Any`
- `RefreshLinkedDataType(DomainID?) -> None`
- `RemoveDuplicates(Columns, Header: XlYesNoGuess?) -> None`
- `RemoveSubtotal() -> Any`
- `Replace(What, Replacement, LookAt?, SearchOrder?, MatchCase?, MatchByte?, SearchFormat?, ReplaceFormat?, FormulaVersion?) -> bool`
- `RowDifferences(Comparison) -> Range`
- `Run(Arg1?, Arg2?, Arg3?, Arg4?, Arg5?, Arg6?, Arg7?, Arg8?, Arg9?, Arg10?, Arg11?, Arg12?, Arg13?, Arg14?, Arg15?, Arg16?, Arg17?, Arg18?, Arg19?, Arg20?, Arg21?, Arg22?, Arg23?, Arg24?, Arg25?, Arg26?, Arg27?, Arg28?, Arg29?, Arg30?) -> Any`
- `Select() -> Any`
- `SetCellDataTypeFromCell(SourceCell: Range) -> None`
- `SetPhonetic() -> None`
- `Show() -> Any`
- `ShowCard() -> None`
- `ShowDependents(Remove?) -> Any`
- `ShowErrors() -> Any`
- `ShowPrecedents(Remove?) -> Any`
- `Sort(Key1, Order1: XlSortOrder?, Key2, Type, Order2: XlSortOrder?, Key3, Order3: XlSortOrder?, Header: XlYesNoGuess?, OrderCustom, MatchCase, Orientation: XlSortOrientation?, SortMethod: XlSortMethod?, DataOption1: XlSortDataOption?, DataOption2: XlSortDataOption?, DataOption3: XlSortDataOption?, SubField1?) -> Any`
- `SortSpecial(SortMethod: XlSortMethod?, Key1, Order1: XlSortOrder?, Type, Key2, Order2: XlSortOrder?, Key3, Order3: XlSortOrder?, Header: XlYesNoGuess?, OrderCustom, MatchCase, Orientation: XlSortOrientation?, DataOption1: XlSortDataOption?, DataOption2: XlSortDataOption?, DataOption3: XlSortDataOption?) -> Any`
- `Speak(SpeakDirection?, SpeakFormulas?) -> None`
- `SpecialCells(Type: XlCellType, Value?) -> Range`
- `SubscribeTo(Edition: str, Format: XlSubscribeToFormat?) -> Any`
- `Subtotal(GroupBy: int, Function: XlConsolidationFunction, TotalList, Replace, PageBreaks, SummaryBelowData: XlSummaryRow?) -> Any`
- `Table(RowInput?, ColumnInput?) -> Any`
- `TextToColumns(Destination, DataType: XlTextParsingType?, TextQualifier: XlTextQualifier?, ConsecutiveDelimiter?, Tab?, Semicolon?, Comma?, Space?, Other?, OtherChar?, FieldInfo?, DecimalSeparator?, ThousandsSeparator?, TrailingMinusNumbers?) -> Any`
- `Ungroup() -> Any`
- `UnMerge() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `End(Direction: XlDirection) -> Range`
- `Get_Default(RowIndex?, ColumnIndex?) -> Any`
- `GetAddress(RowAbsolute, ColumnAbsolute, ReferenceStyle: XlReferenceStyle?, External?, RelativeTo?) -> str`
- `GetAddressLocal(RowAbsolute, ColumnAbsolute, ReferenceStyle: XlReferenceStyle?, External?, RelativeTo?) -> str`
- `GetCharacters(Start?, Length?) -> Characters`
- `GetOffset(RowOffset?, ColumnOffset?) -> Range`
- `GetResize(RowSize?, ColumnSize?) -> Range`
- `GetValue(RangeValueDataType?) -> Any`
- `Item(RowIndex, ColumnIndex?) -> Any`
- `Range(Cell1, Cell2?) -> Range`
- `Set_Default(RowIndex, ColumnIndex?, arg2) -> None`
- `SetItem(RowIndex, ColumnIndex, arg2) -> None`
- `SetValue(RangeValueDataType, arg1) -> None`

## Ranges

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Range`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Range`
- `Item(Index) -> Range`

## SmartTag

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DownloadURL: Any`
- `Name: Any`
- `Parent: Any`
- `Properties: CustomProperties`
- `Range: Range`
- `SmartTagActions: SmartTagActions`
- `XML: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## SmartTagAction

**Properties:**
- `ActiveXControl: Any`
- `Application: Application`
- `CheckboxState: Any`
- `Creator: XlCreator`
- `ExpandHelp: Any`
- `ListSelection: Any`
- `Name: Any`
- `Parent: Any`
- `PresentInPane: Any`
- `RadioGroupSelection: Any`
- `TextboxText: Any`
- `Type: XlSmartTagControlType`

**Methods:**
- `__call__() -> Any`
- `Execute() -> None`

## SmartTagActions

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> SmartTagAction`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> SmartTagAction`
- `Item(Index) -> SmartTagAction`

## SmartTagRecognizer

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Enabled: Any`
- `FullName: Any`
- `Parent: Any`
- `progID: Any`

**Methods:**
- `__call__() -> Any`

## SmartTagRecognizers

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `Recognize: Any`

**Methods:**
- `__call__(Index) -> SmartTagRecognizer`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> SmartTagRecognizer`
- `Item(Index) -> SmartTagRecognizer`

## SmartTags

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> SmartTag`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(SmartTagType: str) -> SmartTag`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> SmartTag`

## Validation

**Properties:**
- `AlertStyle: Any`
- `Application: Application`
- `Creator: XlCreator`
- `ErrorMessage: Any`
- `ErrorTitle: Any`
- `Formula1: Any`
- `Formula2: Any`
- `IgnoreBlank: Any`
- `IMEMode: Any`
- `InCellDropdown: Any`
- `InputMessage: Any`
- `InputTitle: Any`
- `Operator: Any`
- `Parent: Any`
- `ShowError: Any`
- `ShowInput: Any`
- `Type: Any`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `Add(Type: XlDVType, AlertStyle?, Operator?, Formula1?, Formula2?) -> None`
- `Delete() -> None`
- `Modify(Type?, AlertStyle?, Operator?, Formula1?, Formula2?) -> None`

## ValueChange

**Properties:**
- `AllocationMethod: XlAllocationMethod`
- `AllocationValue: XlAllocationValue`
- `AllocationWeightExpression: Any`
- `Application: Application`
- `Creator: XlCreator`
- `Order: Any`
- `Parent: Any`
- `PivotCell: PivotCell`
- `Tuple: Any`
- `Value: Any`
- `VisibleInPivotTable: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## Watch

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `Source: Any`

**Methods:**
- `Delete() -> None`

## Watches

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Watch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Source) -> Watch`
- `Delete() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Watch`
- `Item(Index) -> Watch`

## XPath

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Map: XmlMap`
- `Parent: Any`
- `Repeating: Any`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `Clear() -> None`
- `SetValue(Map: XmlMap, XPath: str, SelectionNamespace?, Repeating?) -> None`

## XmlDataBinding

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `SourceUrl: Any`

**Methods:**
- `__call__() -> Any`
- `ClearSettings() -> None`
- `LoadSettings(Url: str) -> None`
- `Refresh() -> XlXmlImportResult`

## XmlMap

**Properties:**
- `AdjustColumnWidth: Any`
- `AppendOnImport: Any`
- `Application: Application`
- `Creator: XlCreator`
- `DataBinding: XmlDataBinding`
- `IsExportable: Any`
- `Name: Any`
- `Parent: Any`
- `PreserveColumnFilter: Any`
- `PreserveNumberFormatting: Any`
- `RootElementName: Any`
- `RootElementNamespace: XmlNamespace`
- `SaveDataSourceDefinition: Any`
- `Schemas: XmlSchemas`
- `ShowImportExportValidationErrors: Any`
- `WorkbookConnection: WorkbookConnection`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`
- `Export(Url: str, Overwrite?) -> XlXmlExportResult`
- `ExportXml(Data: str?) -> XlXmlExportResult`
- `Import(Url: str, Overwrite?) -> XlXmlImportResult`
- `ImportXml(XmlData: str, Overwrite?) -> XlXmlImportResult`

## XmlMaps

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> XmlMap`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Schema: str, RootElementName?) -> XmlMap`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> XmlMap`
- `Item(Index) -> XmlMap`

## XmlNamespace

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `Prefix: Any`
- `Uri: Any`

**Methods:**
- `__call__() -> Any`

## XmlNamespaces

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `Value: Any`

**Methods:**
- `__call__(Index) -> XmlNamespace`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `InstallManifest(Path: str, InstallForAllUsers?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> XmlNamespace`
- `Item(Index) -> XmlNamespace`

## XmlSchema

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Name: Any`
- `Namespace: XmlNamespace`
- `Parent: Any`
- `XML: Any`

## XmlSchemas

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> XmlSchema`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> XmlSchema`
- `Item(Index) -> XmlSchema`

