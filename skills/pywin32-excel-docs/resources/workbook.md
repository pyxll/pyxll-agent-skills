# Workbook & Workbooks

## AllowEditRange

**Properties:**
- `Range: Range`
- `Title: Any`
- `Users: UserAccessList`

**Methods:**
- `ChangePassword(Password: str) -> None`
- `Delete() -> None`
- `Unprotect(Password?) -> None`

## AllowEditRanges

**Properties:**
- `Count: Any`

**Methods:**
- `__call__(Index) -> AllowEditRange`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Title: str, Range: Range, Password?) -> AllowEditRange`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> AllowEditRange`
- `Item(Index) -> AllowEditRange`

## Connections

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> WorkbookConnection`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_AddFromFile(Filename: str) -> WorkbookConnection`
- `Add(Name: str, Description: str, ConnectionString, CommandText, lCmdtype?) -> WorkbookConnection`
- `Add2(Name: str, Description: str, ConnectionString, CommandText, lCmdtype?, CreateModelConnection?, ImportRelationships?) -> WorkbookConnection`
- `AddFromFile(Filename: str, CreateModelConnection?, ImportRelationships?) -> WorkbookConnection`
- `Item(Index) -> WorkbookConnection`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> WorkbookConnection`

## CustomView

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Name: Any`
- `Parent: Any`
- `PrintSettings: Any`
- `RowColSettings: Any`

**Methods:**
- `Delete() -> None`
- `Show() -> None`

## CustomViews

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(ViewName) -> CustomView`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(ViewName: str, PrintSettings?, RowColSettings?) -> CustomView`
- `Item(ViewName) -> CustomView`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(ViewName) -> CustomView`

## Mailer

**Properties:**
- `Application: Application`
- `BCCRecipients: Any`
- `CCRecipients: Any`
- `Creator: XlCreator`
- `Enclosures: Any`
- `Parent: Any`
- `Received: Any`
- `SendDateTime: Any`
- `Sender: Any`
- `Subject: Any`
- `ToRecipients: Any`
- `WhichAddress: Any`

## Protection

**Properties:**
- `AllowDeletingColumns: Any`
- `AllowDeletingRows: Any`
- `AllowEditRanges: AllowEditRanges`
- `AllowFiltering: Any`
- `AllowFormattingCells: Any`
- `AllowFormattingColumns: Any`
- `AllowFormattingRows: Any`
- `AllowInsertingColumns: Any`
- `AllowInsertingHyperlinks: Any`
- `AllowInsertingRows: Any`
- `AllowSorting: Any`
- `AllowUsingPivotTables: Any`

## PublishObject

**Properties:**
- `Application: Application`
- `AutoRepublish: Any`
- `Creator: XlCreator`
- `DivID: Any`
- `Filename: Any`
- `HtmlType: XlHtmlType`
- `Parent: Any`
- `Sheet: Any`
- `Source: Any`
- `SourceType: XlSourceType`
- `Title: Any`

**Methods:**
- `Delete() -> None`
- `Publish(Create?) -> None`

## PublishObjects

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PublishObject`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(SourceType: XlSourceType, Filename: str, Sheet?, Source?, HtmlType?, DivID?, Title?) -> PublishObject`
- `Delete() -> None`
- `Publish() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PublishObject`
- `Item(Index) -> PublishObject`

## PublishedDoc

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DisclosureScope: Any`
- `Parent: Any`
- `PublishedDate: Any`
- `Title: Any`
- `Url: Any`

## PublishedDocs

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> PublishedDoc`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index: int) -> PublishedDoc`
- `Item(Index: int) -> PublishedDoc`

## Queries

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `FastCombine: Any`
- `Parent: Any`

**Methods:**
- `__call__(NameOrIndex) -> WorkbookQuery`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str, Formula: str, Description?) -> WorkbookQuery`
- `Item(NameOrIndex) -> WorkbookQuery`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(NameOrIndex) -> WorkbookQuery`

## RoutingSlip

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Delivery: XlRoutingSlipDelivery`
- `Message: Any`
- `Parent: Any`
- `Recipients: Any`
- `ReturnWhenDone: Any`
- `Status: XlRoutingSlipStatus`
- `Subject: Any`
- `TrackStatus: Any`

**Methods:**
- `Reset() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `GetRecipients(Index?) -> Any`
- `SetRecipients(Index, arg1) -> None`

## Scenario

**Properties:**
- `Application: Application`
- `ChangingCells: Range`
- `Comment: Any`
- `Creator: XlCreator`
- `Hidden: Any`
- `Index: Any`
- `Locked: Any`
- `Name: Any`
- `Parent: Any`
- `Values: Any`

**Methods:**
- `ChangeScenario(ChangingCells, Values?) -> Any`
- `Delete() -> Any`
- `Show() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `GetValues(Index?) -> Any`

## Scenarios

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str, ChangingCells, Values?, Comment?, Locked?, Hidden?) -> Scenario`
- `CreateSummary(ReportType: XlSummaryReportType?, ResultCells?) -> Any`
- `Item(Index) -> Scenario`
- `Merge(Source) -> Any`

## ServerViewableItems

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
- `Add(Obj) -> Dispatch`
- `Delete(Index) -> None`
- `DeleteAll() -> None`
- `Item(Index) -> Dispatch`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`

## SmartTagOptions

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DisplaySmartTags: XlSmartTagDisplayMode`
- `EmbedSmartTags: Any`
- `Parent: Any`

## UserAccess

**Properties:**
- `AllowEdit: Any`
- `Name: Any`

**Methods:**
- `Delete() -> None`

## UserAccessList

**Properties:**
- `Count: Any`

**Methods:**
- `__call__(Index) -> UserAccess`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str, AllowEdit: bool) -> UserAccess`
- `DeleteAll() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> UserAccess`
- `Item(Index) -> UserAccess`

## WorkbookConnection

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DataFeedConnection: DataFeedConnection`
- `Description: Any`
- `InModel: Any`
- `ModelConnection: ModelConnection`
- `ModelTables: ModelTables`
- `Name: Any`
- `ODBCConnection: ODBCConnection`
- `OLEDBConnection: OLEDBConnection`
- `Parent: Any`
- `Ranges: Ranges`
- `RefreshWithRefreshAll: Any`
- `TextConnection: TextConnection`
- `Type: XlConnectionType`
- `WorksheetDataConnection: WorksheetDataConnection`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`
- `Refresh() -> None`

## WorkbookQuery

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Description: Any`
- `Formula: Any`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## Workbooks

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Workbook`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Open(Filename: str, UpdateLinks?, ReadOnly?, Format?, Password?, WriteResPassword?, IgnoreReadOnlyRecommended?, Origin?, Delimiter?, Editable?, Notify?, Converter?, AddToMru?) -> Workbook`
- `_OpenText(Filename: str, Origin, StartRow, DataType, TextQualifier: XlTextQualifier?, ConsecutiveDelimiter?, Tab?, Semicolon?, Comma?, Space?, Other?, OtherChar?, FieldInfo?, TextVisualLayout?, DecimalSeparator?, ThousandsSeparator?) -> None`
- `_OpenText_(Filename: str, Origin, StartRow, DataType, TextQualifier: XlTextQualifier?, ConsecutiveDelimiter?, Tab?, Semicolon?, Comma?, Space?, Other?, OtherChar?, FieldInfo?, TextVisualLayout?) -> None`
- `_OpenXML(Filename: str, Stylesheets?) -> Workbook`
- `Add(Template?) -> Workbook`
- `CanCheckOut(Filename: str) -> bool`
- `CheckOut(Filename: str) -> None`
- `Close() -> None`
- `Open(Filename: str, UpdateLinks?, ReadOnly?, Format?, Password?, WriteResPassword?, IgnoreReadOnlyRecommended?, Origin?, Delimiter?, Editable?, Notify?, Converter?, AddToMru?, Local?, CorruptLoad?) -> Workbook`
- `OpenDatabase(Filename: str, CommandText?, CommandType?, BackgroundQuery?, ImportDataAs?) -> Workbook`
- `OpenText(Filename: str, Origin, StartRow, DataType, TextQualifier: XlTextQualifier?, ConsecutiveDelimiter?, Tab?, Semicolon?, Comma?, Space?, Other?, OtherChar?, FieldInfo?, TextVisualLayout?, DecimalSeparator?, ThousandsSeparator?, TrailingMinusNumbers?, Local?) -> None`
- `OpenXML(Filename: str, Stylesheets?, LoadOption?) -> Workbook`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Workbook`
- `Item(Index) -> Workbook`

## Workbook
*Bases: _Workbook*

## _Workbook

**Properties:**
- `AcceptLabelsInFormulas: Any`
- `AccuracyVersion: Any`
- `ActiveChart: Chart`
- `ActiveSheet: Any`
- `ActiveSlicer: Slicer`
- `Application: Application`
- `Author: Any`
- `AutoSaveOn: Any`
- `AutoUpdateFrequency: Any`
- `AutoUpdateSaveChanges: Any`
- `BuiltinDocumentProperties: Any`
- `CalculationVersion: Any`
- `CaseSensitive: Any`
- `ChangeHistoryDuration: Any`
- `ChartDataPointTrack: Any`
- `Charts: Sheets`
- `CheckCompatibility: Any`
- `CodeName: Any`
- `Colors: Any`
- `CommandBars: CommandBars`
- `Comments: Any`
- `ConflictResolution: XlSaveConflictResolution`
- `Connections: Connections`
- `ConnectionsDisabled: Any`
- `Container: Any`
- `ContentTypeProperties: MetaProperties`
- `CreateBackup: Any`
- `Creator: XlCreator`
- `CustomDocumentProperties: Any`
- `CustomViews: CustomViews`
- `CustomXMLParts: CustomXMLParts`
- `Date1904: Any`
- `DefaultPivotTableStyle: Any`
- `DefaultSlicerStyle: Any`
- `DefaultTableStyle: Any`
- `DefaultTimelineStyle: Any`
- `DialogSheets: Sheets`
- `DisplayDrawingObjects: XlDisplayDrawingObjects`
- `DisplayInkComments: Any`
- `DocumentInspectors: DocumentInspectors`
- `DocumentLibraryVersions: DocumentLibraryVersions`
- `DoNotPromptForConvert: Any`
- `EnableAutoRecover: Any`
- `EncryptionProvider: Any`
- `EnvelopeVisible: Any`
- `Excel4IntlMacroSheets: Sheets`
- `Excel4MacroSheets: Sheets`
- `Excel8CompatibilityMode: Any`
- `FileFormat: XlFileFormat`
- `Final: Any`
- `ForceFullCalculation: Any`
- `FullName: Any`
- `FullNameURLEncoded: Any`
- `HasMailer: Any`
- `HasPassword: Any`
- `HasRoutingSlip: Any`
- `HasVBProject: Any`
- `HighlightChangesOnScreen: Any`
- `HTMLProject: HTMLProject`
- `IconSets: IconSets`
- `InactiveListBorderVisible: Any`
- `IsAddin: Any`
- `IsInplace: Any`
- `KeepChangeHistory: Any`
- `Keywords: Any`
- `ListChangesOnNewSheet: Any`
- `Mailer: Mailer`
- `Model: Model`
- `Modules: Sheets`
- `MultiUserEditing: Any`
- `Name: Any`
- `Names: Names`
- `OnSave: Any`
- `OnSheetActivate: Any`
- `OnSheetDeactivate: Any`
- `Parent: Any`
- `Password: Any`
- `PasswordEncryptionAlgorithm: Any`
- `PasswordEncryptionFileProperties: Any`
- `PasswordEncryptionKeyLength: Any`
- `PasswordEncryptionProvider: Any`
- `Path: Any`
- `Permission: Permission`
- `PersonalViewListSettings: Any`
- `PersonalViewPrintSettings: Any`
- `PivotTables: Any`
- `PrecisionAsDisplayed: Any`
- `ProtectStructure: Any`
- `ProtectWindows: Any`
- `PublishObjects: PublishObjects`
- `Queries: Queries`
- `ReadOnly: Any`
- `ReadOnlyRecommended: Any`
- `RemovePersonalInformation: Any`
- `Research: Research`
- `RevisionNumber: Any`
- `Routed: Any`
- `RoutingSlip: RoutingSlip`
- `Saved: Any`
- `SaveLinkValues: Any`
- `SensitivityLabel: ISensitivityLabel`
- `ServerPolicy: ServerPolicy`
- `ServerViewableItems: ServerViewableItems`
- `SharedWorkspace: SharedWorkspace`
- `Sheets: Sheets`
- `ShowConflictHistory: Any`
- `ShowPivotChartActiveFields: Any`
- `ShowPivotTableFieldList: Any`
- `Signatures: SignatureSet`
- `SlicerCaches: SlicerCaches`
- `SmartDocument: SmartDocument`
- `SmartTagOptions: SmartTagOptions`
- `Styles: Styles`
- `Subject: Any`
- `Sync: Sync`
- `TableStyles: TableStyles`
- `TemplateRemoveExtData: Any`
- `Theme: OfficeTheme`
- `Title: Any`
- `UpdateLinks: XlUpdateLinks`
- `UpdateRemoteReferences: Any`
- `UserControl: Any`
- `UserStatus: Any`
- `UseWholeCellCriteria: Any`
- `UseWildcards: Any`
- `VBASigned: Any`
- `VBProject: VBProject`
- `WebOptions: WebOptions`
- `Windows: Windows`
- `WorkIdentity: Any`
- `Worksheets: Sheets`
- `WritePassword: Any`
- `WriteReserved: Any`
- `WriteReservedBy: Any`
- `XmlMaps: XmlMaps`
- `XmlNamespaces: XmlNamespaces`

**Methods:**
- `_ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?) -> None`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `_Protect(Password?, Structure?, Windows?) -> None`
- `_ProtectSharing(Filename?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, SharingPassword?) -> None`
- `_SaveAs(Filename, FileFormat, Password, WriteResPassword, ReadOnlyRecommended, CreateBackup, AccessMode: XlSaveAsAccessMode?, ConflictResolution?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `_SaveAs_(Filename, FileFormat, Password, WriteResPassword, ReadOnlyRecommended, CreateBackup, AccessMode: XlSaveAsAccessMode?, ConflictResolution?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `AcceptAllChanges(When?, Who?, Where?) -> None`
- `Activate() -> None`
- `AddToFavorites() -> None`
- `ApplyTheme(Filename: str) -> None`
- `BreakLink(Name: str, Type: XlLinkType) -> None`
- `CanCheckIn() -> bool`
- `ChangeFileAccess(Mode: XlFileAccess, WritePassword?, Notify?) -> None`
- `ChangeLink(Name: str, NewName: str, Type: XlLinkType?) -> None`
- `CheckIn(SaveChanges?, Comments?, MakePublic?) -> None`
- `CheckInWithVersion(SaveChanges?, Comments?, MakePublic?, VersionType?) -> None`
- `Close(SaveChanges?, Filename?, RouteWorkbook?) -> None`
- `ConvertComments() -> None`
- `CreateForecastSheet(Timeline: Range, Values: Range, ForecastStart?, ForecastEnd?, ConfInt?, Seasonality?, DataCompletion?, Aggregation?, ChartType?, ShowStatsTable?) -> None`
- `DeleteNumberFormat(NumberFormat: str) -> None`
- `Dummy26() -> None`
- `Dummy27() -> None`
- `EnableConnections() -> None`
- `EndReview() -> None`
- `ExclusiveAccess() -> bool`
- `ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?, WorkIdentity?) -> None`
- `FollowHyperlink(Address: str, SubAddress?, NewWindow?, AddHistory?, ExtraInfo?, Method?, HeaderInfo?) -> None`
- `ForwardMailer() -> None`
- `GetWorkflowTasks() -> WorkflowTasks`
- `GetWorkflowTemplates() -> WorkflowTemplates`
- `HighlightChangesOptions(When?, Who?, Where?) -> None`
- `LinkInfo(Name: str, LinkInfo: XlLinkInfo, Type?, EditionRef?) -> Any`
- `LinkSources(Type?) -> Any`
- `LockServerFile() -> None`
- `LookUpInDocs(Filename?) -> PublishedDocs`
- `MergeWorkbook(Filename) -> None`
- `NewWindow() -> Window`
- `OpenLinks(Name: str, ReadOnly?, Type?) -> None`
- `PivotCaches() -> PivotCaches`
- `PivotTableWizard(SourceType?, SourceData?, TableDestination?, TableName?, RowGrand?, ColumnGrand?, SaveData?, HasAutoFormat?, AutoPage?, Reserved?, BackgroundQuery?, OptimizeCache?, PageFieldOrder?, PageFieldWrapCount?, ReadData?, Connection?) -> None`
- `Post(DestName?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?, IgnorePrintAreas?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Protect(Password?, Structure?, Windows?) -> None`
- `ProtectSharing(Filename?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, SharingPassword?, FileFormat?) -> None`
- `PublishToDocs(Title: str, DisclosureScope: XlPublishToDocsDisclosureScope, OverwriteUrl?) -> str`
- `PublishToPBI(PublishType?, nameConflict?, bstrGroupName?) -> str`
- `PurgeChangeHistoryNow(Days: int, SharingPassword?) -> None`
- `RecheckSmartTags() -> None`
- `RefreshAll() -> None`
- `RejectAllChanges(When?, Who?, Where?) -> None`
- `ReloadAs(Encoding: MsoEncoding) -> None`
- `RemoveDocumentInformation(RemoveDocInfoType: XlRemoveDocInfoType) -> None`
- `RemoveUser(Index: int) -> None`
- `Reply() -> None`
- `ReplyAll() -> None`
- `ReplyWithChanges(ShowMessage?) -> None`
- `ResetColors() -> None`
- `Route() -> None`
- `RunAutoMacros(Which: XlRunAutoMacro) -> None`
- `Save() -> None`
- `SaveAs(Filename, FileFormat, Password, WriteResPassword, ReadOnlyRecommended, CreateBackup, AccessMode: XlSaveAsAccessMode?, ConflictResolution?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?, WorkIdentity?) -> None`
- `SaveAsXMLData(Filename: str, Map: XmlMap) -> None`
- `SaveCopyAs(Filename?) -> None`
- `sblt(s: str) -> None`
- `SendFaxOverInternet(Recipients?, Subject?, ShowMessage?) -> None`
- `SendForReview(Recipients?, Subject?, ShowMessage?, IncludeAttachment?) -> None`
- `SendMail(Recipients, Subject?, ReturnReceipt?) -> None`
- `SendMailer(FileFormat, Priority: XlPriority?) -> None`
- `SetLinkOnData(Name: str, Procedure?) -> None`
- `SetPasswordEncryptionOptions(PasswordEncryptionProvider?, PasswordEncryptionAlgorithm?, PasswordEncryptionKeyLength?, PasswordEncryptionFileProperties?) -> None`
- `ToggleFormsDesign() -> None`
- `Unprotect(Password?) -> None`
- `UnprotectSharing(SharingPassword?) -> None`
- `UpdateFromFile() -> None`
- `UpdateLink(Name?, Type?) -> None`
- `WebPagePreview() -> None`
- `XmlImport(Url: str, ImportMap: XmlMap?, Overwrite?, Destination?) -> XlXmlImportResult`
- `XmlImportXml(Data: str, ImportMap: XmlMap?, Overwrite?, Destination?) -> XlXmlImportResult`

**Property Accessors** *(parameterized — must be called as method):*
- `GetColors(Index?) -> Any`
- `SetColors(Index, arg1) -> None`

