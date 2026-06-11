# Data Model

## Model

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DataModelConnection: WorkbookConnection`
- `ModelFormatBoolean: ModelFormatBoolean`
- `ModelFormatCurrency: ModelFormatCurrency`
- `ModelFormatDate: ModelFormatDate`
- `ModelFormatDecimalNumber: ModelFormatDecimalNumber`
- `ModelFormatGeneral: ModelFormatGeneral`
- `ModelFormatPercentageNumber: ModelFormatPercentageNumber`
- `ModelFormatScientificNumber: ModelFormatScientificNumber`
- `ModelFormatWholeNumber: ModelFormatWholeNumber`
- `ModelMeasures: ModelMeasures`
- `ModelRelationships: ModelRelationships`
- `ModelTables: ModelTables`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `AddConnection(ConnectionToDataSource: WorkbookConnection) -> WorkbookConnection`
- `CreateModelWorkbookConnection(ModelTable) -> WorkbookConnection`
- `Initialize() -> None`
- `Refresh() -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetModelFormatCurrency(Symbol?, DecimalPlaces?) -> ModelFormatCurrency`
- `GetModelFormatDate(FormatString?) -> ModelFormatDate`
- `GetModelFormatDecimalNumber(UseThousandSeparator?, DecimalPlaces?) -> ModelFormatDecimalNumber`
- `GetModelFormatPercentageNumber(UseThousandSeparator?, DecimalPlaces?) -> ModelFormatPercentageNumber`
- `GetModelFormatScientificNumber(DecimalPlaces?) -> ModelFormatScientificNumber`
- `GetModelFormatWholeNumber(UseThousandSeparator?) -> ModelFormatWholeNumber`

## ModelChanges

**Properties:**
- `Application: Application`
- `ColumnsAdded: ModelColumnNames`
- `ColumnsChanged: ModelColumnChanges`
- `ColumnsDeleted: ModelColumnNames`
- `Creator: XlCreator`
- `MeasuresAdded: ModelMeasureNames`
- `Parent: Any`
- `RelationshipChange: Any`
- `Source: XlModelChangeSource`
- `TableNamesChanged: ModelTableNameChanges`
- `TablesAdded: ModelTableNames`
- `TablesDeleted: ModelTableNames`
- `TablesModified: ModelTableNames`
- `UnknownChange: Any`

## ModelColumnChange

**Properties:**
- `Application: Application`
- `ColumnName: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `TableName: Any`

## ModelColumnChanges

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelColumnChange`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ModelColumnChange`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelColumnChange`

## ModelColumnName

**Properties:**
- `Application: Application`
- `ColumnName: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `TableName: Any`

## ModelColumnNames

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelColumnName`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ModelColumnName`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelColumnName`

## ModelConnection

**Properties:**
- `ADOConnection: Any`
- `Application: Application`
- `CalculatedMembers: CalculatedMembers`
- `CommandText: Any`
- `CommandType: XlCmdType`
- `Creator: XlCreator`
- `Parent: Any`

## ModelFormatBoolean

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`

## ModelFormatCurrency

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DecimalPlaces: Any`
- `Parent: Any`
- `Symbol: Any`

## ModelFormatDate

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `FormatString: Any`
- `Parent: Any`

## ModelFormatDecimalNumber

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DecimalPlaces: Any`
- `Parent: Any`
- `UseThousandSeparator: Any`

## ModelFormatGeneral

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`

## ModelFormatPercentageNumber

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DecimalPlaces: Any`
- `Parent: Any`
- `UseThousandSeparator: Any`

## ModelFormatScientificNumber

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DecimalPlaces: Any`
- `Parent: Any`

## ModelFormatWholeNumber

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `UseThousandSeparator: Any`

## ModelMeasure

**Properties:**
- `Application: Application`
- `AssociatedTable: ModelTable`
- `Creator: XlCreator`
- `Description: Any`
- `FormatInformation: Any`
- `Formula: Any`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> None`

## ModelMeasureName

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `MeasureName: Any`
- `Parent: Any`
- `TableName: Any`

## ModelMeasureNames

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelMeasureName`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ModelMeasureName`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelMeasureName`

## ModelMeasures

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelMeasure`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(MeasureName: str, AssociatedTable: ModelTable, Formula: str, FormatInformation, Description?) -> ModelMeasure`
- `Item(Index) -> ModelMeasure`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelMeasure`

## ModelRelationship

**Properties:**
- `Active: Any`
- `Application: Application`
- `Creator: XlCreator`
- `ForeignKeyColumn: ModelTableColumn`
- `ForeignKeyTable: ModelTable`
- `Parent: Any`
- `PrimaryKeyColumn: ModelTableColumn`
- `PrimaryKeyTable: ModelTable`

**Methods:**
- `Delete() -> None`

## ModelRelationships

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelRelationship`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(ForeignKeyColumn: ModelTableColumn, PrimaryKeyColumn: ModelTableColumn) -> ModelRelationship`
- `DetectRelationships(PivotTable: PivotTable) -> None`
- `Item(Index) -> ModelRelationship`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelRelationship`

## ModelTable

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `ModelTableColumns: ModelTableColumns`
- `Name: Any`
- `Parent: Any`
- `RecordCount: Any`
- `SourceName: Any`
- `SourceWorkbookConnection: WorkbookConnection`

**Methods:**
- `Refresh() -> None`

## ModelTableColumn

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `DataType: Any`
- `Name: Any`
- `Parent: Any`

## ModelTableColumns

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelTableColumn`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ModelTableColumn`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelTableColumn`

## ModelTableNameChange

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `TableNameNew: Any`
- `TableNameOld: Any`

## ModelTableNameChanges

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelTableNameChange`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ModelTableNameChange`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelTableNameChange`

## ModelTableNames

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> str`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> str`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> str`

## ModelTables

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ModelTable`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ModelTable`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ModelTable`

## RTD

**Properties:**
- `ThrottleInterval: Any`

**Methods:**
- `RefreshData() -> None`
- `RestartServers() -> None`

