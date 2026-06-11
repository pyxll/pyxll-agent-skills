# Tables (ListObjects)

## DataFeedConnection

**Properties:**
- `AlwaysUseConnectionFile: Any`
- `Application: Application`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Connection: Any`
- `Creator: XlCreator`
- `EnableRefresh: Any`
- `Parent: Any`
- `RefreshDate: Any`
- `Refreshing: Any`
- `RefreshOnFileOpen: Any`
- `RefreshPeriod: Any`
- `SavePassword: Any`
- `ServerCredentialsMethod: XlCredentialsMethod`
- `SourceConnectionFile: Any`
- `SourceDataFile: Any`

**Methods:**
- `CancelRefresh() -> None`
- `Refresh() -> None`
- `SaveAsODC(ODCFileName: str, Description?, Keywords?) -> None`

## ListColumn

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DataBodyRange: Range`
- `Index: Any`
- `ListDataFormat: ListDataFormat`
- `Name: Any`
- `Parent: Any`
- `Range: Range`
- `SharePointFormula: Any`
- `Total: Range`
- `TotalsCalculation: XlTotalsCalculation`
- `XPath: XPath`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## ListColumns

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ListColumn`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Position?) -> ListColumn`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ListColumn`
- `Item(Index) -> ListColumn`

## ListDataFormat

**Properties:**
- `AllowFillIn: Any`
- `Application: Application`
- `Choices: Any`
- `Creator: XlCreator`
- `DecimalPlaces: Any`
- `DefaultValue: Any`
- `IsPercent: Any`
- `lcid: Any`
- `MaxCharacters: Any`
- `MaxNumber: Any`
- `MinNumber: Any`
- `Parent: Any`
- `ReadOnly: Any`
- `Required: Any`
- `Type: XlListDataType`

**Methods:**
- `__call__() -> Any`

## ListObject

**Properties:**
- `Active: Any`
- `AlternativeText: Any`
- `Application: Application`
- `AutoFilter: AutoFilter`
- `Comment: Any`
- `Creator: XlCreator`
- `DataBodyRange: Range`
- `DisplayName: Any`
- `DisplayRightToLeft: Any`
- `HeaderRowRange: Range`
- `InsertRowRange: Range`
- `ListColumns: ListColumns`
- `ListRows: ListRows`
- `Name: Any`
- `Parent: Any`
- `QueryTable: QueryTable`
- `Range: Range`
- `SharePointURL: Any`
- `ShowAutoFilter: Any`
- `ShowAutoFilterDropDown: Any`
- `ShowHeaders: Any`
- `ShowTableStyleColumnStripes: Any`
- `ShowTableStyleFirstColumn: Any`
- `ShowTableStyleLastColumn: Any`
- `ShowTableStyleRowStripes: Any`
- `ShowTotals: Any`
- `Slicers: Slicers`
- `Sort: Sort`
- `SourceType: XlListObjectSourceType`
- `Summary: Any`
- `TableObject: TableObject`
- `TableStyle: Any`
- `TotalsRowRange: Range`
- `XmlMap: XmlMap`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`
- `ExportToVisio() -> None`
- `Publish(Target, LinkSource: bool) -> str`
- `Refresh() -> None`
- `Resize(Range: Range) -> None`
- `Unlink() -> None`
- `Unlist() -> None`
- `UpdateChanges(iConflictType: XlListConflict?) -> None`

## ListObjects

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ListObject`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Add(SourceType: XlListObjectSourceType?, Source, LinkSource, XlListObjectHasHeaders: XlYesNoGuess?, Destination?) -> ListObject`
- `Add(SourceType: XlListObjectSourceType?, Source, LinkSource, XlListObjectHasHeaders: XlYesNoGuess?, Destination?, TableStyleName?) -> ListObject`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ListObject`
- `Item(Index) -> ListObject`

## ListRow

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Index: Any`
- `InvalidData: Any`
- `Parent: Any`
- `Range: Range`

**Methods:**
- `Delete() -> None`

## ListRows

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ListRow`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Add(Position?) -> ListRow`
- `Add(Position?, AlwaysInsert?) -> ListRow`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ListRow`
- `Item(Index) -> ListRow`

## ODBCConnection

**Properties:**
- `AlwaysUseConnectionFile: Any`
- `Application: Application`
- `BackgroundQuery: Any`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Connection: Any`
- `Creator: XlCreator`
- `EnableRefresh: Any`
- `Parent: Any`
- `RefreshDate: Any`
- `Refreshing: Any`
- `RefreshOnFileOpen: Any`
- `RefreshPeriod: Any`
- `RobustConnect: XlRobustConnect`
- `SavePassword: Any`
- `ServerCredentialsMethod: XlCredentialsMethod`
- `ServerSSOApplicationID: Any`
- `SourceConnectionFile: Any`
- `SourceData: Any`
- `SourceDataFile: Any`

**Methods:**
- `CancelRefresh() -> None`
- `Refresh() -> None`
- `SaveAsODC(ODCFileName: str, Description?, Keywords?) -> None`

## ODBCError

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `ErrorString: Any`
- `Parent: Any`
- `SqlState: Any`

## ODBCErrors

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> ODBCError`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index: int) -> ODBCError`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> ODBCError`

## OLEDBConnection

**Properties:**
- `ADOConnection: Any`
- `AlwaysUseConnectionFile: Any`
- `Application: Application`
- `BackgroundQuery: Any`
- `CalculatedMembers: CalculatedMembers`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Connection: Any`
- `Creator: XlCreator`
- `EnableRefresh: Any`
- `IsConnected: Any`
- `LocalConnection: Any`
- `LocaleID: Any`
- `MaintainConnection: Any`
- `MaxDrillthroughRecords: Any`
- `OLAP: Any`
- `Parent: Any`
- `RefreshDate: Any`
- `Refreshing: Any`
- `RefreshOnFileOpen: Any`
- `RefreshPeriod: Any`
- `RetrieveInOfficeUILang: Any`
- `RobustConnect: XlRobustConnect`
- `SavePassword: Any`
- `ServerCredentialsMethod: XlCredentialsMethod`
- `ServerFillColor: Any`
- `ServerFontStyle: Any`
- `ServerNumberFormat: Any`
- `ServerSSOApplicationID: Any`
- `ServerTextColor: Any`
- `SourceConnectionFile: Any`
- `SourceDataFile: Any`
- `UseLocalConnection: Any`

**Methods:**
- `CancelRefresh() -> None`
- `MakeConnection() -> None`
- `Reconnect() -> None`
- `Refresh() -> None`
- `SaveAsODC(ODCFileName: str, Description?, Keywords?) -> None`

## OLEDBError

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `ErrorString: Any`
- `Native: Any`
- `Number: Any`
- `Parent: Any`
- `SqlState: Any`
- `Stage: Any`

## OLEDBErrors

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> OLEDBError`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index: int) -> OLEDBError`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: int) -> OLEDBError`

## Parameter

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DataType: XlParameterDataType`
- `Name: Any`
- `Parent: Any`
- `PromptString: Any`
- `RefreshOnChange: Any`
- `SourceRange: Range`
- `Type: XlParameterType`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `SetParam(Type: XlParameterType, Value) -> None`

## Parameters

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Parameter`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str, iDataType?) -> Parameter`
- `Delete() -> None`
- `Item(Index) -> Parameter`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Parameter`

## QueryTables

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> QueryTable`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Connection, Destination: Range, Sql?) -> QueryTable`
- `Item(Index) -> QueryTable`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> QueryTable`

## TableObject

**Properties:**
- `AdjustColumnWidth: Any`
- `Application: Application`
- `Creator: XlCreator`
- `Destination: Range`
- `EnableEditing: Any`
- `EnableRefresh: Any`
- `FetchedRowOverflow: Any`
- `ListObject: ListObject`
- `Parent: Any`
- `PreserveColumnInfo: Any`
- `PreserveFormatting: Any`
- `RefreshStyle: XlCellInsertionMode`
- `ResultRange: Range`
- `RowNumbers: Any`
- `WorkbookConnection: WorkbookConnection`

**Methods:**
- `Delete() -> None`
- `Refresh() -> bool`

## TextConnection

**Properties:**
- `Application: Application`
- `Connection: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `TextFileColumnDataTypes: Any`
- `TextFileCommaDelimiter: Any`
- `TextFileConsecutiveDelimiter: Any`
- `TextFileDecimalSeparator: Any`
- `TextFileFixedColumnWidths: Any`
- `TextFileHeaderRow: Any`
- `TextFileOtherDelimiter: Any`
- `TextFileParseType: XlTextParsingType`
- `TextFilePlatform: XlPlatform`
- `TextFilePromptOnRefresh: Any`
- `TextFileSemicolonDelimiter: Any`
- `TextFileSpaceDelimiter: Any`
- `TextFileStartRow: Any`
- `TextFileTabDelimiter: Any`
- `TextFileTextQualifier: XlTextQualifier`
- `TextFileThousandsSeparator: Any`
- `TextFileTrailingMinusNumbers: Any`
- `TextFileVisualLayout: XlTextVisualLayoutType`

## WorksheetDataConnection

**Properties:**
- `Application: Application`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Connection: Any`
- `Creator: XlCreator`
- `Parent: Any`

## QueryTable
*Bases: _QueryTable*

## _IQueryTable

**Properties:**
- `AdjustColumnWidth: Any`
- `Application: Any`
- `BackgroundQuery: Any`
- `CommandText: Any`
- `CommandType: Any`
- `Connection: Any`
- `Creator: Any`
- `Destination: Any`
- `EditWebPage: Any`
- `EnableEditing: Any`
- `EnableRefresh: Any`
- `FetchedRowOverflow: Any`
- `FieldNames: Any`
- `FillAdjacentFormulas: Any`
- `HasAutoFormat: Any`
- `ListObject: Any`
- `MaintainConnection: Any`
- `Name: Any`
- `Parameters: Any`
- `Parent: Any`
- `PostText: Any`
- `PreserveColumnInfo: Any`
- `PreserveFormatting: Any`
- `QueryType: Any`
- `Recordset: Any`
- `Refreshing: Any`
- `RefreshOnFileOpen: Any`
- `RefreshPeriod: Any`
- `RefreshStyle: Any`
- `ResultRange: Any`
- `RobustConnect: Any`
- `RowNumbers: Any`
- `SaveData: Any`
- `SavePassword: Any`
- `Sort: Any`
- `SourceConnectionFile: Any`
- `SourceDataFile: Any`
- `Sql: Any`
- `TablesOnlyFromHTML: Any`
- `TextFileColumnDataTypes: Any`
- `TextFileCommaDelimiter: Any`
- `TextFileConsecutiveDelimiter: Any`
- `TextFileDecimalSeparator: Any`
- `TextFileFixedColumnWidths: Any`
- `TextFileOtherDelimiter: Any`
- `TextFileParseType: Any`
- `TextFilePlatform: Any`
- `TextFilePromptOnRefresh: Any`
- `TextFileSemicolonDelimiter: Any`
- `TextFileSpaceDelimiter: Any`
- `TextFileStartRow: Any`
- `TextFileTabDelimiter: Any`
- `TextFileTextQualifier: Any`
- `TextFileThousandsSeparator: Any`
- `TextFileTrailingMinusNumbers: Any`
- `TextFileVisualLayout: Any`
- `WebConsecutiveDelimitersAsOne: Any`
- `WebDisableDateRecognition: Any`
- `WebDisableRedirections: Any`
- `WebFormatting: Any`
- `WebPreFormattedTextToColumns: Any`
- `WebSelectionType: Any`
- `WebSingleBlockTextImport: Any`
- `WebTables: Any`
- `WorkbookConnection: Any`

## _QueryTable

**Properties:**
- `AdjustColumnWidth: Any`
- `Application: Application`
- `BackgroundQuery: Any`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Connection: Any`
- `Creator: XlCreator`
- `Destination: Range`
- `EditWebPage: Any`
- `EnableEditing: Any`
- `EnableRefresh: Any`
- `FetchedRowOverflow: Any`
- `FieldNames: Any`
- `FillAdjacentFormulas: Any`
- `HasAutoFormat: Any`
- `ListObject: ListObject`
- `MaintainConnection: Any`
- `Name: Any`
- `Parameters: Parameters`
- `Parent: Any`
- `PostText: Any`
- `PreserveColumnInfo: Any`
- `PreserveFormatting: Any`
- `QueryType: XlQueryType`
- `Recordset: Any`
- `Refreshing: Any`
- `RefreshOnFileOpen: Any`
- `RefreshPeriod: Any`
- `RefreshStyle: XlCellInsertionMode`
- `ResultRange: Range`
- `RobustConnect: XlRobustConnect`
- `RowNumbers: Any`
- `SaveData: Any`
- `SavePassword: Any`
- `Sort: Sort`
- `SourceConnectionFile: Any`
- `SourceDataFile: Any`
- `Sql: Any`
- `TablesOnlyFromHTML: Any`
- `TextFileColumnDataTypes: Any`
- `TextFileCommaDelimiter: Any`
- `TextFileConsecutiveDelimiter: Any`
- `TextFileDecimalSeparator: Any`
- `TextFileFixedColumnWidths: Any`
- `TextFileOtherDelimiter: Any`
- `TextFileParseType: XlTextParsingType`
- `TextFilePlatform: Any`
- `TextFilePromptOnRefresh: Any`
- `TextFileSemicolonDelimiter: Any`
- `TextFileSpaceDelimiter: Any`
- `TextFileStartRow: Any`
- `TextFileTabDelimiter: Any`
- `TextFileTextQualifier: XlTextQualifier`
- `TextFileThousandsSeparator: Any`
- `TextFileTrailingMinusNumbers: Any`
- `TextFileVisualLayout: XlTextVisualLayoutType`
- `WebConsecutiveDelimitersAsOne: Any`
- `WebDisableDateRecognition: Any`
- `WebDisableRedirections: Any`
- `WebFormatting: XlWebFormatting`
- `WebPreFormattedTextToColumns: Any`
- `WebSelectionType: XlWebSelectionType`
- `WebSingleBlockTextImport: Any`
- `WebTables: Any`
- `WorkbookConnection: WorkbookConnection`

**Methods:**
- `CancelRefresh() -> None`
- `Delete() -> None`
- `Refresh(BackgroundQuery?) -> bool`
- `ResetTimer() -> None`
- `SaveAsODC(ODCFileName: str, Description?, Keywords?) -> None`

