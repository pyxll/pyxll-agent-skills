# Formatting

## AboveAverage

**Properties:**
- `AboveBelow: XlAboveBelow`
- `Application: Application`
- `AppliesTo: Range`
- `Borders: Borders`
- `CalcFor: XlCalcFor`
- `Creator: XlCreator`
- `Font: Font`
- `Interior: Interior`
- `NumberFormat: Any`
- `NumStdDev: Any`
- `Parent: Any`
- `Priority: Any`
- `PTCondition: Any`
- `ScopeType: XlPivotConditionScope`
- `StopIfTrue: Any`
- `Type: Any`

**Methods:**
- `Delete() -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

## Border

**Properties:**
- `Application: Application`
- `Color: Any`
- `ColorIndex: Any`
- `Creator: XlCreator`
- `LineStyle: Any`
- `Parent: Any`
- `ThemeColor: Any`
- `TintAndShade: Any`
- `Weight: Any`

## Borders

**Properties:**
- `Application: Application`
- `Color: Any`
- `ColorIndex: Any`
- `Count: Any`
- `Creator: XlCreator`
- `LineStyle: Any`
- `Parent: Any`
- `ThemeColor: Any`
- `TintAndShade: Any`
- `Value: Any`
- `Weight: Any`

**Methods:**
- `__call__(Index: XlBordersIndex) -> Border`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: XlBordersIndex) -> Border`
- `Item(Index: XlBordersIndex) -> Border`

## CellFormat

**Properties:**
- `AddIndent: Any`
- `Application: Application`
- `Borders: Borders`
- `Creator: XlCreator`
- `Font: Font`
- `FormulaHidden: Any`
- `HorizontalAlignment: Any`
- `IndentLevel: Any`
- `Interior: Interior`
- `Locked: Any`
- `MergeCells: Any`
- `NumberFormat: Any`
- `NumberFormatLocal: Any`
- `Orientation: Any`
- `Parent: Any`
- `ShrinkToFit: Any`
- `VerticalAlignment: Any`
- `WrapText: Any`

**Methods:**
- `Clear() -> None`

## Characters

**Properties:**
- `Application: Application`
- `Caption: Any`
- `Count: Any`
- `Creator: XlCreator`
- `Font: Font`
- `Parent: Any`
- `PhoneticCharacters: Any`
- `Text: Any`

**Methods:**
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Delete() -> Any`
- `Insert(String: str) -> Any`

## ColorScale

**Properties:**
- `Application: Application`
- `AppliesTo: Range`
- `ColorScaleCriteria: ColorScaleCriteria`
- `Creator: XlCreator`
- `Formula: Any`
- `Parent: Any`
- `Priority: Any`
- `PTCondition: Any`
- `ScopeType: XlPivotConditionScope`
- `StopIfTrue: Any`
- `Type: Any`

**Methods:**
- `Delete() -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

## ColorScaleCriteria

**Properties:**
- `Count: Any`

**Methods:**
- `__call__(Index) -> ColorScaleCriterion`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ColorScaleCriterion`
- `Item(Index) -> ColorScaleCriterion`

## ColorScaleCriterion

**Properties:**
- `FormatColor: FormatColor`
- `Index: Any`
- `Type: XlConditionValueTypes`
- `Value: Any`

**Methods:**
- `__call__() -> Any`

## ColorStop

**Properties:**
- `Application: Application`
- `Color: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `Position: Any`
- `ThemeColor: Any`
- `TintAndShade: Any`

**Methods:**
- `Delete() -> None`

## ColorStops

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ColorStop`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Position: float) -> ColorStop`
- `Clear() -> None`
- `Item(Index) -> ColorStop`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> ColorStop`

## ConditionValue

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `Type: XlConditionValueTypes`
- `Value: Any`

**Methods:**
- `__call__() -> Any`
- `Modify(newtype: XlConditionValueTypes, newvalue?) -> None`

## DataBarBorder

**Properties:**
- `Application: Application`
- `Color: Any`
- `Creator: XlCreator`
- `Parent: Any`
- `Type: XlDataBarBorderType`

## Databar

**Properties:**
- `Application: Application`
- `AppliesTo: Range`
- `AxisColor: Any`
- `AxisPosition: XlDataBarAxisPosition`
- `BarBorder: DataBarBorder`
- `BarColor: Any`
- `BarFillType: XlDataBarFillType`
- `Creator: XlCreator`
- `Direction: Any`
- `Formula: Any`
- `MaxPoint: ConditionValue`
- `MinPoint: ConditionValue`
- `NegativeBarFormat: NegativeBarFormat`
- `Parent: Any`
- `PercentMax: Any`
- `PercentMin: Any`
- `Priority: Any`
- `PTCondition: Any`
- `ScopeType: XlPivotConditionScope`
- `ShowValue: Any`
- `StopIfTrue: Any`
- `Type: Any`

**Methods:**
- `Delete() -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

## DisplayFormat

**Properties:**
- `AddIndent: Any`
- `Application: Application`
- `Borders: Borders`
- `Characters: Characters`
- `Creator: XlCreator`
- `Font: Font`
- `FormulaHidden: Any`
- `HorizontalAlignment: Any`
- `IndentLevel: Any`
- `Interior: Interior`
- `Locked: Any`
- `MergeCells: Any`
- `NumberFormat: Any`
- `NumberFormatLocal: Any`
- `Orientation: Any`
- `Parent: Any`
- `ReadingOrder: Any`
- `ShrinkToFit: Any`
- `Style: Any`
- `VerticalAlignment: Any`
- `WrapText: Any`

**Property Accessors** *(parameterized — must be called as method):*
- `GetCharacters(Start?, Length?) -> Characters`

## Font

**Properties:**
- `Application: Application`
- `Background: Any`
- `Bold: Any`
- `Color: Any`
- `ColorIndex: Any`
- `Creator: XlCreator`
- `FontStyle: Any`
- `Italic: Any`
- `Name: Any`
- `OutlineFont: Any`
- `Parent: Any`
- `Shadow: Any`
- `Size: Any`
- `Strikethrough: Any`
- `Subscript: Any`
- `Superscript: Any`
- `ThemeColor: Any`
- `ThemeFont: XlThemeFont`
- `TintAndShade: Any`
- `Underline: Any`

## FormatColor

**Properties:**
- `Application: Application`
- `Color: Any`
- `ColorIndex: XlColorIndex`
- `Creator: XlCreator`
- `Parent: Any`
- `ThemeColor: Any`
- `TintAndShade: Any`

## FormatCondition

**Properties:**
- `Application: Application`
- `AppliesTo: Range`
- `Borders: Borders`
- `Creator: XlCreator`
- `DateOperator: XlTimePeriods`
- `Font: Font`
- `Formula1: Any`
- `Formula2: Any`
- `Interior: Interior`
- `NumberFormat: Any`
- `Operator: Any`
- `Parent: Any`
- `Priority: Any`
- `PTCondition: Any`
- `ScopeType: XlPivotConditionScope`
- `StopIfTrue: Any`
- `Text: Any`
- `TextOperator: XlContainsOperator`
- `Type: Any`

**Methods:**
- `_Modify(Type: XlFormatConditionType, Operator?, Formula1?, Formula2?) -> None`
- `Delete() -> None`
- `Modify(Type: XlFormatConditionType, Operator?, Formula1?, Formula2?, String?, Operator2?) -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

## FormatConditions

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
- `Add(Type: XlFormatConditionType, Operator?, Formula1?, Formula2?, String?, TextOperator?, DateOperator?, ScopeType?) -> Dispatch`
- `AddAboveAverage() -> Dispatch`
- `AddColorScale(ColorScaleType: int) -> Dispatch`
- `AddDatabar() -> Dispatch`
- `AddIconSetCondition() -> Dispatch`
- `AddTop10() -> Dispatch`
- `AddUniqueValues() -> Dispatch`
- `Delete() -> None`
- `Item(Index) -> Dispatch`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`

## Icon

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Index: Any`
- `Parent: IconSet`

## IconCriteria

**Properties:**
- `Count: Any`

**Methods:**
- `__call__(Index) -> IconCriterion`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> IconCriterion`
- `Item(Index) -> IconCriterion`

## IconCriterion

**Properties:**
- `Icon: XlIcon`
- `Index: Any`
- `Operator: Any`
- `Type: XlConditionValueTypes`
- `Value: Any`

**Methods:**
- `__call__() -> Any`

## IconSet

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `ID: XlIconSet`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Icon`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Icon`
- `Item(Index) -> Icon`

## IconSetCondition

**Properties:**
- `Application: Application`
- `AppliesTo: Range`
- `Creator: XlCreator`
- `Formula: Any`
- `IconCriteria: IconCriteria`
- `IconSet: Any`
- `Parent: Any`
- `PercentileValues: Any`
- `Priority: Any`
- `PTCondition: Any`
- `ReverseOrder: Any`
- `ScopeType: XlPivotConditionScope`
- `ShowIconOnly: Any`
- `StopIfTrue: Any`
- `Type: Any`

**Methods:**
- `Delete() -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

## IconSets

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

## Interior

**Properties:**
- `Application: Application`
- `Color: Any`
- `ColorIndex: Any`
- `Creator: XlCreator`
- `Gradient: Any`
- `InvertIfNegative: Any`
- `Parent: Any`
- `Pattern: Any`
- `PatternColor: Any`
- `PatternColorIndex: Any`
- `PatternThemeColor: Any`
- `PatternTintAndShade: Any`
- `ThemeColor: Any`
- `TintAndShade: Any`

## LinearGradient

**Properties:**
- `Application: Application`
- `ColorStops: ColorStops`
- `Creator: XlCreator`
- `Degree: Any`
- `Parent: Any`

## NegativeBarFormat

**Properties:**
- `Application: Application`
- `BorderColor: Any`
- `BorderColorType: XlDataBarNegativeColorType`
- `Color: Any`
- `ColorType: XlDataBarNegativeColorType`
- `Creator: XlCreator`
- `Parent: Any`

## RectangularGradient

**Properties:**
- `Application: Application`
- `ColorStops: ColorStops`
- `Creator: XlCreator`
- `Parent: Any`
- `RectangleBottom: Any`
- `RectangleLeft: Any`
- `RectangleRight: Any`
- `RectangleTop: Any`

## Style

**Properties:**
- `AddIndent: Any`
- `Application: Application`
- `Borders: Borders`
- `BuiltIn: Any`
- `Creator: XlCreator`
- `Font: Font`
- `FormulaHidden: Any`
- `HorizontalAlignment: XlHAlign`
- `IncludeAlignment: Any`
- `IncludeBorder: Any`
- `IncludeFont: Any`
- `IncludeNumber: Any`
- `IncludePatterns: Any`
- `IncludeProtection: Any`
- `IndentLevel: Any`
- `Interior: Interior`
- `Locked: Any`
- `MergeCells: Any`
- `Name: Any`
- `NameLocal: Any`
- `NumberFormat: Any`
- `NumberFormatLocal: Any`
- `Orientation: XlOrientation`
- `Parent: Any`
- `ReadingOrder: Any`
- `ShrinkToFit: Any`
- `Value: Any`
- `VerticalAlignment: XlVAlign`
- `WrapText: Any`

**Methods:**
- `__call__() -> Any`
- `Delete() -> Any`

## Styles

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Style`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(Name: str, BasedOn?) -> Style`
- `Merge(Workbook) -> Any`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Style`
- `Item(Index) -> Style`

## TableStyle

**Properties:**
- `Application: Application`
- `BuiltIn: Any`
- `Creator: XlCreator`
- `Name: Any`
- `NameLocal: Any`
- `Parent: Any`
- `ShowAsAvailablePivotTableStyle: Any`
- `ShowAsAvailableSlicerStyle: Any`
- `ShowAsAvailableTableStyle: Any`
- `ShowAsAvailableTimelineStyle: Any`
- `TableStyleElements: TableStyleElements`

**Methods:**
- `__call__() -> Any`
- `Delete() -> None`
- `Duplicate(NewTableStyleName?) -> TableStyle`

## TableStyleElement

**Properties:**
- `Application: Application`
- `Borders: Borders`
- `Creator: XlCreator`
- `Font: Font`
- `HasFormat: Any`
- `Interior: Interior`
- `Parent: Any`
- `StripeSize: Any`

**Methods:**
- `Clear() -> None`

## TableStyleElements

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: XlTableStyleElementType) -> TableStyleElement`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index: XlTableStyleElementType) -> TableStyleElement`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index: XlTableStyleElementType) -> TableStyleElement`

## TableStyles

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> TableStyle`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Add(TableStyleName: str) -> TableStyle`
- `Item(Index) -> TableStyle`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> TableStyle`

## Top10

**Properties:**
- `Application: Application`
- `AppliesTo: Range`
- `Borders: Borders`
- `CalcFor: XlCalcFor`
- `Creator: XlCreator`
- `Font: Font`
- `Interior: Interior`
- `NumberFormat: Any`
- `Parent: Any`
- `Percent: Any`
- `Priority: Any`
- `PTCondition: Any`
- `Rank: Any`
- `ScopeType: XlPivotConditionScope`
- `StopIfTrue: Any`
- `TopBottom: XlTopBottom`
- `Type: Any`

**Methods:**
- `Delete() -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

## UniqueValues

**Properties:**
- `Application: Application`
- `AppliesTo: Range`
- `Borders: Borders`
- `Creator: XlCreator`
- `DupeUnique: XlDupeUnique`
- `Font: Font`
- `Interior: Interior`
- `NumberFormat: Any`
- `Parent: Any`
- `Priority: Any`
- `PTCondition: Any`
- `ScopeType: XlPivotConditionScope`
- `StopIfTrue: Any`
- `Type: Any`

**Methods:**
- `Delete() -> None`
- `ModifyAppliesToRange(Range: Range) -> None`
- `SetFirstPriority() -> None`
- `SetLastPriority() -> None`

