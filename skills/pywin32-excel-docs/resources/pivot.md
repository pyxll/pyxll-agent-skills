# PivotTables

## CalculatedFields

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Field) -> PivotField`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Add(Name: str, Formula: str) -> PivotField`
- `Add(Name: str, Formula: str, UseStandardFormula?) -> PivotField`
- `Item(Index) -> PivotField`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Field) -> PivotField`

## CalculatedItems

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Field) -> PivotItem`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Add(Name: str, Formula: str) -> PivotItem`
- `Add(Name: str, Formula: str, UseStandardFormula?) -> PivotItem`
- `Item(Index) -> PivotItem`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Field) -> PivotItem`

## CalculatedMember

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DisplayFolder: Any`
- `Dynamic: Any`
- `FlattenHierarchies: Any`
- `Formula: Any`
- `HierarchizeDistinct: Any`
- `IsValid: Any`
- `MeasureGroup: Any`
- `Name: Any`
- `NumberFormat: XlCalcMemNumberFormatType`
- `Parent: Any`
- `ParentHierarchy: Any`
- `ParentMember: Any`
- `SolveOrder: Any`
- `SourceName: Any`
- `Type: XlCalculatedMemberType`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## CalculatedMembers

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> CalculatedMember`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Add(Name: str, Formula: str, SolveOrder?, Type?) -> CalculatedMember`
- `Add(Name: str, Formula, SolveOrder?, Type?, Dynamic?, DisplayFolder?, HierarchizeDistinct?) -> CalculatedMember`
- `AddCalculatedMember(Name: str, Formula, SolveOrder?, Type?, DisplayFolder?, MeasureGroup?, ParentHierarchy?, ParentMember?, NumberFormat?) -> CalculatedMember`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> CalculatedMember`
- `Item(Index) -> CalculatedMember`

## CubeField

**Properties:**
- `AllItemsVisible: Any`
- `Application: Application`
- `Caption: Any`
- `Creator: XlCreator`
- `CubeFieldSubType: XlCubeFieldSubType`
- `CubeFieldType: XlCubeFieldType`
- `CurrentPageName: Any`
- `DragToColumn: Any`
- `DragToData: Any`
- `DragToHide: Any`
- `DragToPage: Any`
- `DragToRow: Any`
- `EnableMultiplePageItems: Any`
- `FlattenHierarchies: Any`
- `HasMemberProperties: Any`
- `HiddenLevels: Any`
- `HierarchizeDistinct: Any`
- `IncludeNewItemsInFilter: Any`
- `IsDate: Any`
- `LayoutForm: XlLayoutFormType`
- `LayoutSubtotalLocation: XlSubtototalLocationType`
- `Name: Any`
- `Orientation: XlPivotFieldOrientation`
- `Parent: Any`
- `PivotFields: PivotFields`
- `Position: Any`
- `ShowInFieldList: Any`
- `TreeviewControl: TreeviewControl`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `_AddMemberPropertyField(Property: str, PropertyOrder?) -> None`
- `AddMemberPropertyField(Property: str, PropertyOrder?, PropertyDisplayedIn?) -> None`
- `AutoGroup(Orientation?, Position?) -> None`
- `ClearManualFilter() -> None`
- `CreatePivotFields() -> None`
- `Delete() -> None`

## CubeFields

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> CubeField`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `AddSet(Name: str, Caption: str) -> CubeField`
- `GetMeasure(AttributeHierarchy, Function: XlConsolidationFunction, Caption?) -> CubeField`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> CubeField`
- `Item(Index) -> CubeField`

## PivotAxis

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `PivotLines: PivotLines`

## PivotCache

**Properties:**
- `ADOConnection: Any`
- `Application: Application`
- `BackgroundQuery: Any`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Connection: Any`
- `Creator: XlCreator`
- `EnableRefresh: Any`
- `Index: Any`
- `IsConnected: Any`
- `LocalConnection: Any`
- `MaintainConnection: Any`
- `MemoryUsed: Any`
- `MissingItemsLimit: XlPivotTableMissingItems`
- `OLAP: Any`
- `OptimizeCache: Any`
- `Parent: Any`
- `QueryType: XlQueryType`
- `RecordCount: Any`
- `Recordset: Any`
- `RefreshDate: Any`
- `RefreshName: Any`
- `RefreshOnFileOpen: Any`
- `RefreshPeriod: Any`
- `RobustConnect: XlRobustConnect`
- `SavePassword: Any`
- `SourceConnectionFile: Any`
- `SourceData: Any`
- `SourceDataFile: Any`
- `SourceType: XlPivotTableSourceType`
- `Sql: Any`
- `UpgradeOnRefresh: Any`
- `UseLocalConnection: Any`
- `Version: XlPivotTableVersionList`
- `WorkbookConnection: WorkbookConnection`

**Methods:**
- `CreatePivotChart(ChartDestination, XlChartType?, Left?, Top?, Width?, Height?) -> Shape`
- `CreatePivotTable(TableDestination, TableName?, ReadData?, DefaultVersion?) -> PivotTable`
- `MakeConnection() -> None`
- `Refresh() -> None`
- `ResetTimer() -> None`
- `SaveAsODC(ODCFileName: str, Description?, Keywords?) -> None`

## PivotCaches

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PivotCache`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(SourceType: XlPivotTableSourceType, SourceData?) -> PivotCache`
- `Create(SourceType: XlPivotTableSourceType, SourceData?, Version?) -> PivotCache`
- `Item(Index) -> PivotCache`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PivotCache`

## PivotCell

**Properties:**
- `Application: Application`
- `CellChanged: XlCellChangedState`
- `ColumnItems: PivotItemList`
- `Creator: XlCreator`
- `CustomSubtotalFunction: XlConsolidationFunction`
- `DataField: PivotField`
- `DataSourceValue: Any`
- `MDX: Any`
- `Parent: Any`
- `PivotCellType: XlPivotCellType`
- `PivotColumnLine: PivotLine`
- `PivotField: PivotField`
- `PivotItem: PivotItem`
- `PivotRowLine: PivotLine`
- `PivotTable: PivotTable`
- `Range: Range`
- `RowItems: PivotItemList`
- `ServerActions: Actions`

**Methods:**
- `AllocateChange() -> None`
- `DiscardChange() -> None`

## PivotField

**Properties:**
- `AllItemsVisible: Any`
- `Application: Application`
- `AutoShowCount: Any`
- `AutoShowField: Any`
- `AutoShowRange: Any`
- `AutoShowType: Any`
- `AutoSortCustomSubtotal: Any`
- `AutoSortField: Any`
- `AutoSortOrder: Any`
- `AutoSortPivotLine: PivotLine`
- `BaseField: Any`
- `BaseItem: Any`
- `Calculation: XlPivotFieldCalculation`
- `Caption: Any`
- `ChildField: PivotField`
- `ChildItems: Any`
- `Creator: XlCreator`
- `CubeField: CubeField`
- `CurrentPage: Any`
- `CurrentPageList: Any`
- `CurrentPageName: Any`
- `DatabaseSort: Any`
- `DataRange: Range`
- `DataType: XlPivotFieldDataType`
- `DisplayAsCaption: Any`
- `DisplayAsTooltip: Any`
- `DisplayInReport: Any`
- `DragToColumn: Any`
- `DragToData: Any`
- `DragToHide: Any`
- `DragToPage: Any`
- `DragToRow: Any`
- `DrilledDown: Any`
- `EnableItemSelection: Any`
- `EnableMultiplePageItems: Any`
- `Formula: Any`
- `Function: XlConsolidationFunction`
- `GroupLevel: Any`
- `Hidden: Any`
- `HiddenItems: Any`
- `HiddenItemsList: Any`
- `IncludeNewItemsInFilter: Any`
- `IsCalculated: Any`
- `IsMemberProperty: Any`
- `LabelRange: Range`
- `LayoutBlankLine: Any`
- `LayoutCompactRow: Any`
- `LayoutForm: XlLayoutFormType`
- `LayoutPageBreak: Any`
- `LayoutSubtotalLocation: XlSubtototalLocationType`
- `MemberPropertyCaption: Any`
- `MemoryUsed: Any`
- `Name: Any`
- `NumberFormat: Any`
- `Orientation: XlPivotFieldOrientation`
- `Parent: Any`
- `ParentField: PivotField`
- `ParentItems: Any`
- `PivotFilters: PivotFilters`
- `Position: Any`
- `PropertyOrder: Any`
- `PropertyParentField: PivotField`
- `RepeatLabels: Any`
- `ServerBased: Any`
- `ShowAllItems: Any`
- `ShowDetail: Any`
- `ShowingInAxis: Any`
- `SourceCaption: Any`
- `SourceName: Any`
- `StandardFormula: Any`
- `SubtotalName: Any`
- `Subtotals: Any`
- `TotalLevels: Any`
- `UseMemberPropertyAsCaption: Any`
- `Value: Any`
- `VisibleItems: Any`
- `VisibleItemsList: Any`

**Methods:**
- `__call__() -> Any`
- `_AutoSort(Order: int, Field: str) -> None`
- `AddPageItem(Item: str, ClearList?) -> None`
- `AutoGroup() -> None`
- `AutoShow(Type: int, Range: int, Count: int, Field: str) -> None`
- `AutoSort(Order: int, Field: str, PivotLine?, CustomSubtotal?) -> None`
- `CalculatedItems() -> CalculatedItems`
- `ClearAllFilters() -> None`
- `ClearLabelFilters() -> None`
- `ClearManualFilter() -> None`
- `ClearValueFilters() -> None`
- `Delete() -> None`
- `DrillTo(Field: str) -> None`
- `PivotItems(Index?) -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `GetChildItems(Index?) -> Any`
- `GetHiddenItems(Index?) -> Any`
- `GetParentItems(Index?) -> Any`
- `GetSubtotals(Index?) -> Any`
- `GetVisibleItems(Index?) -> Any`
- `SetSubtotals(Index, arg1) -> None`

## PivotFields

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: PivotTable`

**Methods:**
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> Dispatch`

## PivotFilter

**Properties:**
- `Active: Any`
- `Application: Application`
- `Creator: XlCreator`
- `DataCubeField: CubeField`
- `DataField: PivotField`
- `Description: Any`
- `FilterType: XlPivotFilterType`
- `IsMemberPropertyFilter: Any`
- `MemberPropertyField: PivotField`
- `Name: Any`
- `Order: Any`
- `Parent: Any`
- `PivotField: PivotField`
- `Value1: Any`
- `Value2: Any`
- `WholeDayFilter: Any`

**Methods:**
- `Delete() -> None`

## PivotFilters

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PivotFilter`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Type: XlPivotFilterType, DataField?, Value1?, Value2?, Order?, Name?, Description?, MemberPropertyField?) -> PivotFilter`
- `Add2(Type: XlPivotFilterType, DataField?, Value1?, Value2?, Order?, Name?, Description?, MemberPropertyField?, WholeDayFilter?) -> PivotFilter`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PivotFilter`
- `Item(Index) -> PivotFilter`

## PivotFormula

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Formula: Any`
- `Index: Any`
- `Parent: Any`
- `StandardFormula: Any`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`

## PivotFormulas

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PivotFormula`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Add(Formula: str) -> PivotFormula`
- `Add(Formula: str, UseStandardFormula?) -> PivotFormula`
- `Item(Index) -> PivotFormula`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PivotFormula`

## PivotItem

**Properties:**
- `Application: Application`
- `Caption: Any`
- `ChildItems: Any`
- `Creator: XlCreator`
- `DataRange: Range`
- `DrilledDown: Any`
- `Formula: Any`
- `IsCalculated: Any`
- `LabelRange: Range`
- `Name: Any`
- `Parent: PivotField`
- `ParentItem: PivotItem`
- `ParentShowDetail: Any`
- `Position: Any`
- `RecordCount: Any`
- `ShowDetail: Any`
- `SourceName: Any`
- `SourceNameStandard: Any`
- `StandardFormula: Any`
- `Value: Any`
- `Visible: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`
- `DrillTo(Field: str) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetChildItems(Index?) -> Any`

## PivotItemList

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Field) -> PivotItem`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> PivotItem`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Field) -> PivotItem`

## PivotItems

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: PivotField`

**Methods:**
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str) -> None`
- `Item(Index) -> Dispatch`

## PivotLayout

**Properties:**
- `Application: Application`
- `ColumnFields: Any`
- `Creator: XlCreator`
- `CubeFields: CubeFields`
- `DataFields: Any`
- `HiddenFields: Any`
- `InnerDetail: Any`
- `PageFields: Any`
- `Parent: Any`
- `PivotCache: PivotCache`
- `PivotFields: Any`
- `PivotTable: PivotTable`
- `RowFields: Any`
- `VisibleFields: Any`

**Methods:**
- `AddFields(RowFields?, ColumnFields?, PageFields?, AppendField?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetColumnFields(Index?) -> Dispatch`
- `GetDataFields(Index?) -> Dispatch`
- `GetHiddenFields(Index?) -> Dispatch`
- `GetPageFields(Index?) -> Dispatch`
- `GetPivotFields(Index?) -> Dispatch`
- `GetRowFields(Index?) -> Dispatch`
- `GetVisibleFields(Index?) -> Dispatch`

## PivotLine

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `LineType: XlPivotLineType`
- `Parent: Any`
- `PivotLineCells: PivotLineCells`
- `PivotLineCellsFull: PivotLineCells`
- `Position: Any`

## PivotLineCells

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Full: Any`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PivotCell`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PivotCell`
- `Item(Index) -> PivotCell`

## PivotLines

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PivotLine`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PivotLine`
- `Item(Index) -> PivotLine`

## PivotTable

**Properties:**
- `ActiveFilters: PivotFilters`
- `Allocation: XlAllocation`
- `AllocationMethod: XlAllocationMethod`
- `AllocationValue: XlAllocationValue`
- `AllocationWeightExpression: Any`
- `AllowMultipleFilters: Any`
- `AlternativeText: Any`
- `Application: Application`
- `CacheIndex: Any`
- `CalculatedMembers: CalculatedMembers`
- `CalculatedMembersInFilters: Any`
- `ChangeList: PivotTableChangeList`
- `ColumnFields: Any`
- `ColumnGrand: Any`
- `ColumnRange: Range`
- `CompactLayoutColumnHeader: Any`
- `CompactLayoutRowHeader: Any`
- `CompactRowIndent: Any`
- `Creator: XlCreator`
- `CubeFields: CubeFields`
- `DataBodyRange: Range`
- `DataFields: Any`
- `DataLabelRange: Range`
- `DataPivotField: PivotField`
- `DisplayContextTooltips: Any`
- `DisplayEmptyColumn: Any`
- `DisplayEmptyRow: Any`
- `DisplayErrorString: Any`
- `DisplayFieldCaptions: Any`
- `DisplayImmediateItems: Any`
- `DisplayMemberPropertyTooltips: Any`
- `DisplayNullString: Any`
- `EnableDataValueEditing: Any`
- `EnableDrilldown: Any`
- `EnableFieldDialog: Any`
- `EnableFieldList: Any`
- `EnableWizard: Any`
- `EnableWriteback: Any`
- `ErrorString: Any`
- `FieldListSortAscending: Any`
- `GrandTotalName: Any`
- `HasAutoFormat: Any`
- `Hidden: Any`
- `HiddenFields: Any`
- `InGridDropZones: Any`
- `InnerDetail: Any`
- `LayoutRowDefault: XlLayoutRowType`
- `Location: Any`
- `ManualUpdate: Any`
- `MDX: Any`
- `MergeLabels: Any`
- `Name: Any`
- `NullString: Any`
- `PageFieldOrder: Any`
- `PageFields: Any`
- `PageFieldStyle: Any`
- `PageFieldWrapCount: Any`
- `PageRange: Range`
- `PageRangeCells: Range`
- `Parent: Any`
- `PivotChart: Shape`
- `PivotColumnAxis: PivotAxis`
- `PivotFormulas: PivotFormulas`
- `PivotRowAxis: PivotAxis`
- `PivotSelection: Any`
- `PivotSelectionStandard: Any`
- `PreserveFormatting: Any`
- `PrintDrillIndicators: Any`
- `PrintTitles: Any`
- `RefreshDate: Any`
- `RefreshName: Any`
- `RepeatItemsOnEachPrintedPage: Any`
- `RowFields: Any`
- `RowGrand: Any`
- `RowRange: Range`
- `SaveData: Any`
- `SelectionMode: XlPTSelectionMode`
- `ShowCellBackgroundFromOLAP: Any`
- `ShowDrillIndicators: Any`
- `ShowPageMultipleItemLabel: Any`
- `ShowTableStyleColumnHeaders: Any`
- `ShowTableStyleColumnStripes: Any`
- `ShowTableStyleLastColumn: Any`
- `ShowTableStyleRowHeaders: Any`
- `ShowTableStyleRowStripes: Any`
- `ShowValuesRow: Any`
- `Slicers: Slicers`
- `SmallGrid: Any`
- `SortUsingCustomLists: Any`
- `SourceData: Any`
- `SubtotalHiddenPageItems: Any`
- `Summary: Any`
- `TableRange1: Range`
- `TableRange2: Range`
- `TableStyle: Any`
- `TableStyle2: Any`
- `Tag: Any`
- `TotalsAnnotation: Any`
- `VacatedStyle: Any`
- `Value: Any`
- `Version: XlPivotTableVersionList`
- `ViewCalculatedMembers: Any`
- `VisibleFields: Any`
- `VisualTotals: Any`
- `VisualTotalsForSets: Any`

**Methods:**
- `__call__() -> Any`
- `_PivotSelect(Name: str, Mode: XlPTSelectionMode?) -> None`
- `AddDataField(Field: Dispatch, Caption?, Function?) -> PivotField`
- `AddFields(RowFields?, ColumnFields?, PageFields?, AddToTable?) -> Any`
- `AllocateChanges() -> None`
- `ApplyLayout() -> None`
- `CalculatedFields() -> CalculatedFields`
- `ChangeConnection(conn: WorkbookConnection) -> None`
- `ChangePivotCache(PivotCache) -> None`
- `ClearAllFilters() -> None`
- `ClearTable() -> None`
- `CommitChanges() -> None`
- `ConvertToFormulas(ConvertFilters: bool) -> None`
- `CreateCubeFile(File: str, Measures?, Levels?, Members?, Properties?) -> str`
- `DiscardChanges() -> None`
- `DrillDown(PivotItem: PivotItem, PivotLine?) -> None`
- `DrillTo(PivotItem: PivotItem, CubeField: CubeField, PivotLine?) -> None`
- `DrillUp(PivotItem: PivotItem, PivotLine?, LevelUniqueName?) -> None`
- `Format(Format: XlPivotFormatType) -> None`
- `GetData(Name: str) -> float`
- `GetPivotData(DataField?, Field1?, Item1?, Field2?, Item2?, Field3?, Item3?, Field4?, Item4?, Field5?, Item5?, Field6?, Item6?, Field7?, Item7?, Field8?, Item8?, Field9?, Item9?, Field10?, Item10?, Field11?, Item11?, Field12?, Item12?, Field13?, Item13?, Field14?, Item14?) -> Range`
- `ListFormulas() -> None`
- `PivotCache() -> PivotCache`
- `PivotFields(Index?) -> Dispatch`
- `PivotSelect(Name: str, Mode: XlPTSelectionMode?, UseStandardName?) -> None`
- `PivotTableWizard(SourceType?, SourceData?, TableDestination?, TableName?, RowGrand?, ColumnGrand?, SaveData?, HasAutoFormat?, AutoPage?, Reserved?, BackgroundQuery?, OptimizeCache?, PageFieldOrder?, PageFieldWrapCount?, ReadData?, Connection?) -> None`
- `PivotValueCell(rowline?, columnline?) -> PivotValueCell`
- `RefreshDataSourceValues() -> None`
- `RefreshTable() -> bool`
- `RepeatAllLabels(Repeat: XlPivotFieldRepeatLabels) -> None`
- `RowAxisLayout(RowLayout: XlLayoutRowType) -> None`
- `ShowPages(PageField?) -> Any`
- `SubtotalLocation(Location: XlSubtototalLocationType) -> None`
- `Update() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetColumnFields(Index?) -> Dispatch`
- `GetDataFields(Index?) -> Dispatch`
- `GetHiddenFields(Index?) -> Dispatch`
- `GetPageFields(Index?) -> Dispatch`
- `GetRowFields(Index?) -> Dispatch`
- `GetVisibleFields(Index?) -> Dispatch`

## PivotTables

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(PivotCache: PivotCache, TableDestination, TableName?, ReadData?, DefaultVersion?) -> PivotTable`
- `Item(Index) -> PivotTable`

## PivotValueCell

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `PivotCell: PivotCell`
- `ServerActions: Actions`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `ShowDetail() -> None`

## Slicer

**Properties:**
- `ActiveItem: SlicerItem`
- `Application: Application`
- `Caption: Any`
- `ColumnWidth: Any`
- `Creator: XlCreator`
- `DisableMoveResizeUI: Any`
- `DisplayHeader: Any`
- `Height: Any`
- `Left: Any`
- `Locked: Any`
- `Name: Any`
- `NumberOfColumns: Any`
- `Parent: Any`
- `RowHeight: Any`
- `Shape: Shape`
- `SlicerCache: SlicerCache`
- `SlicerCacheLevel: SlicerCacheLevel`
- `SlicerCacheType: XlSlicerCacheType`
- `Style: Any`
- `TimelineViewState: TimelineViewState`
- `Top: Any`
- `Width: Any`

**Methods:**
- `Copy() -> None`
- `Cut() -> None`
- `Delete() -> None`

## SlicerCache

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `CrossFilterType: XlSlicerCrossFilterType`
- `FilterCleared: Any`
- `Index: Any`
- `List: Any`
- `ListObject: ListObject`
- `Name: Any`
- `OLAP: Any`
- `Parent: Any`
- `PivotTables: SlicerPivotTables`
- `RequireManualUpdate: Any`
- `ShowAllItems: Any`
- `SlicerCacheLevels: SlicerCacheLevels`
- `SlicerCacheType: XlSlicerCacheType`
- `SlicerItems: SlicerItems`
- `Slicers: Slicers`
- `SortItems: XlSlicerSort`
- `SortUsingCustomLists: Any`
- `SourceName: Any`
- `SourceType: XlPivotTableSourceType`
- `TimelineState: TimelineState`
- `VisibleSlicerItems: SlicerItems`
- `VisibleSlicerItemsList: Any`
- `WorkbookConnection: WorkbookConnection`

**Methods:**
- `ClearAllFilters() -> None`
- `ClearDateFilter() -> None`
- `ClearManualFilter() -> None`
- `Delete() -> None`

## SlicerCacheLevel

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `CrossFilterType: XlSlicerCrossFilterType`
- `Name: Any`
- `Ordinal: Any`
- `Parent: Any`
- `SlicerItems: SlicerItems`
- `SortItems: XlSlicerSort`
- `VisibleSlicerItemsList: Any`

**Methods:**
- `__len__() -> Any`
- `__nonzero__() -> Any`

## SlicerCacheLevels

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Item: SlicerCacheLevel`
- `Parent: Any`

**Methods:**
- `__call__(Level?) -> SlicerCacheLevel`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `Get_Default(Level?) -> SlicerCacheLevel`
- `GetItem(Level?) -> SlicerCacheLevel`

## SlicerCaches

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> SlicerCache`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Source, SourceField, Name?) -> SlicerCache`
- `Add2(Source, SourceField, Name?, SlicerCacheType?) -> SlicerCache`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> SlicerCache`
- `Item(Index) -> SlicerCache`

## SlicerItem

**Properties:**
- `Application: Application`
- `Caption: Any`
- `Creator: XlCreator`
- `HasData: Any`
- `Name: Any`
- `Parent: SlicerCache`
- `Selected: Any`
- `SourceName: Any`
- `SourceNameStandard: Any`
- `Value: Any`

**Methods:**
- `__call__() -> Any`

## SlicerItems

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> SlicerItem`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> SlicerItem`
- `Item(Index) -> SlicerItem`

## SlicerPivotTables

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> PivotTable`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `AddPivotTable(PivotTable: PivotTable) -> None`
- `RemovePivotTable(PivotTable) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> PivotTable`
- `Item(Index) -> PivotTable`

## Slicers

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Slicer`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(SlicerDestination, Level?, Name?, Caption?, Top?, Left?, Width?, Height?) -> Slicer`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Slicer`
- `Item(Index) -> Slicer`

## TimelineState

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `EndDate: Any`
- `FilterType: XlPivotFilterType`
- `FilterValue1: Any`
- `FilterValue2: Any`
- `Parent: Any`
- `SingleRangeFilterState: Any`
- `StartDate: Any`

**Methods:**
- `SetFilterDateRange(StartDate, EndDate) -> XlFilterStatus`

## TimelineViewState

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Level: XlTimelineLevel`
- `Parent: Any`
- `ShowHeader: Any`
- `ShowHorizontalScrollbar: Any`
- `ShowSelectionLabel: Any`
- `ShowTimeLevel: Any`

