# Charts & Chart Objects

## Axes

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Type: XlAxisType, AxisGroup: XlAxisGroup?) -> Axis`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Type: XlAxisType, AxisGroup: XlAxisGroup?) -> Axis`
- `Item(Type: XlAxisType, AxisGroup: XlAxisGroup?) -> Axis`

## Axis

**Properties:**
- `Application: Application`
- `AxisBetweenCategories: Any`
- `AxisGroup: XlAxisGroup`
- `AxisTitle: AxisTitle`
- `BaseUnit: XlTimeUnit`
- `BaseUnitIsAuto: Any`
- `Border: Border`
- `CategoryNames: Any`
- `CategorySortOrder: XlCategorySortOrder`
- `CategoryType: XlCategoryType`
- `Creator: XlCreator`
- `Crosses: XlAxisCrosses`
- `CrossesAt: Any`
- `DisplayUnit: XlDisplayUnit`
- `DisplayUnitCustom: Any`
- `DisplayUnitLabel: DisplayUnitLabel`
- `Format: ChartFormat`
- `HasDisplayUnitLabel: Any`
- `HasMajorGridlines: Any`
- `HasMinorGridlines: Any`
- `HasTitle: Any`
- `Height: Any`
- `Left: Any`
- `LogBase: Any`
- `MajorGridlines: Gridlines`
- `MajorTickMark: XlTickMark`
- `MajorUnit: Any`
- `MajorUnitIsAuto: Any`
- `MajorUnitScale: XlTimeUnit`
- `MaximumScale: Any`
- `MaximumScaleIsAuto: Any`
- `MinimumScale: Any`
- `MinimumScaleIsAuto: Any`
- `MinorGridlines: Gridlines`
- `MinorTickMark: XlTickMark`
- `MinorUnit: Any`
- `MinorUnitIsAuto: Any`
- `MinorUnitScale: XlTimeUnit`
- `Parent: Any`
- `ReversePlotOrder: Any`
- `ScaleType: XlScaleType`
- `TickLabelPosition: XlTickLabelPosition`
- `TickLabels: TickLabels`
- `TickLabelSpacing: Any`
- `TickLabelSpacingIsAuto: Any`
- `TickMarkSpacing: Any`
- `Top: Any`
- `Type: XlAxisType`
- `Width: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## AxisTitle

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Border: Border`
- `Caption: Any`
- `Characters: Characters`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `Formula: Any`
- `FormulaLocal: Any`
- `FormulaR1C1: Any`
- `FormulaR1C1Local: Any`
- `Height: Any`
- `HorizontalAlignment: Any`
- `IncludeInLayout: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `Orientation: Any`
- `Parent: Any`
- `Position: XlChartElementPosition`
- `ReadingOrder: Any`
- `Shadow: Any`
- `Text: Any`
- `Top: Any`
- `VerticalAlignment: Any`
- `Width: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetCharacters(Start?, Length?) -> Characters`

## CategoryCollection

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> ChartCategory`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index) -> ChartCategory`
- `Item(Index) -> ChartCategory`

## ChartArea

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `Height: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `Parent: Any`
- `RoundedCorners: Any`
- `Shadow: Any`
- `Top: Any`
- `Width: Any`

**Methods:**
- `Clear() -> Any`
- `ClearContents() -> Any`
- `ClearFormats() -> Any`
- `Copy() -> Any`
- `Select() -> Any`

## ChartCategory

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `IsFiltered: Any`
- `Name: Any`
- `Parent: Any`

## ChartColorFormat

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `RGB: Any`
- `SchemeColor: Any`
- `Type: Any`

**Methods:**
- `__call__() -> Any`

## ChartFillFormat

**Properties:**
- `Application: Application`
- `BackColor: ChartColorFormat`
- `Creator: XlCreator`
- `ForeColor: ChartColorFormat`
- `GradientColorType: MsoGradientColorType`
- `GradientDegree: Any`
- `GradientStyle: MsoGradientStyle`
- `GradientVariant: Any`
- `Parent: Any`
- `Pattern: MsoPatternType`
- `PresetGradientType: MsoPresetGradientType`
- `PresetTexture: MsoPresetTexture`
- `TextureName: Any`
- `TextureType: MsoTextureType`
- `Type: MsoFillType`
- `Visible: MsoTriState`

**Methods:**
- `OneColorGradient(Style: MsoGradientStyle, Variant: int, Degree: float) -> None`
- `Patterned(Pattern: MsoPatternType) -> None`
- `PresetGradient(Style: MsoGradientStyle, Variant: int, PresetGradientType: MsoPresetGradientType) -> None`
- `PresetTextured(PresetTexture: MsoPresetTexture) -> None`
- `Solid() -> None`
- `TwoColorGradient(Style: MsoGradientStyle, Variant: int) -> None`
- `UserPicture(PictureFile?, PictureFormat?, PictureStackUnit?, PicturePlacement?) -> None`
- `UserTextured(TextureFile: str) -> None`

## ChartFormat

**Properties:**
- `Adjustments: Adjustments`
- `Application: Application`
- `AutoShapeType: MsoAutoShapeType`
- `Creator: XlCreator`
- `Fill: FillFormat`
- `Glow: GlowFormat`
- `Line: LineFormat`
- `Parent: Any`
- `PictureFormat: PictureFormat`
- `Shadow: ShadowFormat`
- `SoftEdge: SoftEdgeFormat`
- `TextFrame2: TextFrame2`
- `ThreeD: ThreeDFormat`

## ChartGroup

**Properties:**
- `Application: Application`
- `AxisGroup: XlAxisGroup`
- `BinsCountValue: Any`
- `BinsOverflowEnabled: Any`
- `BinsOverflowValue: Any`
- `BinsType: XlBinsType`
- `BinsUnderflowEnabled: Any`
- `BinsUnderflowValue: Any`
- `BinWidthValue: Any`
- `BubbleScale: Any`
- `Creator: XlCreator`
- `DoughnutHoleSize: Any`
- `DownBars: DownBars`
- `DropLines: DropLines`
- `FirstSliceAngle: Any`
- `GapWidth: Any`
- `Has3DShading: Any`
- `HasDropLines: Any`
- `HasHiLoLines: Any`
- `HasRadarAxisLabels: Any`
- `HasSeriesLines: Any`
- `HasUpDownBars: Any`
- `HiLoLines: HiLoLines`
- `Index: Any`
- `Overlap: Any`
- `Parent: Any`
- `RadarAxisLabels: TickLabels`
- `SecondPlotSize: Any`
- `SeriesLines: SeriesLines`
- `ShowNegativeBubbles: Any`
- `SizeRepresents: XlSizeRepresents`
- `SplitType: XlChartSplitType`
- `SplitValue: Any`
- `SubType: Any`
- `Type: Any`
- `UpBars: UpBars`
- `VaryByCategories: Any`

**Methods:**
- `CategoryCollection(Index?) -> Dispatch`
- `FullCategoryCollection(Index?) -> Dispatch`
- `SeriesCollection(Index?) -> Dispatch`

## ChartGroups

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `Item(Index) -> ChartGroup`

## ChartObject

**Properties:**
- `Application: Application`
- `Border: Border`
- `BottomRightCell: Range`
- `Chart: Chart`
- `Creator: XlCreator`
- `Enabled: Any`
- `Height: Any`
- `Index: Any`
- `Interior: Interior`
- `Left: Any`
- `Locked: Any`
- `Name: Any`
- `OnAction: Any`
- `Parent: Any`
- `Placement: Any`
- `PrintObject: Any`
- `ProtectChartObject: Any`
- `RoundedCorners: Any`
- `Shadow: Any`
- `ShapeRange: ShapeRange`
- `Top: Any`
- `TopLeftCell: Range`
- `Visible: Any`
- `Width: Any`
- `ZOrder: Any`

**Methods:**
- `_Copy() -> Any`
- `Activate() -> Any`
- `BringToFront() -> Any`
- `Copy() -> Any`
- `CopyPicture(Appearance: XlPictureAppearance?, Format: XlCopyPictureFormat?) -> Any`
- `Cut() -> Any`
- `Delete() -> Any`
- `Duplicate() -> Dispatch`
- `Select(Replace?) -> Any`
- `SendToBack() -> Any`

## ChartObjects

**Properties:**
- `Application: Application`
- `Border: Border`
- `Count: Any`
- `Creator: XlCreator`
- `Enabled: Any`
- `Height: Any`
- `Interior: Interior`
- `Left: Any`
- `Locked: Any`
- `OnAction: Any`
- `Parent: Any`
- `Placement: Any`
- `PrintObject: Any`
- `ProtectChartObject: Any`
- `RoundedCorners: Any`
- `Shadow: Any`
- `ShapeRange: ShapeRange`
- `Top: Any`
- `Visible: Any`
- `Width: Any`

**Methods:**
- `__call__(Index) -> Dispatch`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Copy() -> Any`
- `_Default(Index) -> Dispatch`
- `Add(Left: float, Top: float, Width: float, Height: float) -> ChartObject`
- `BringToFront() -> Any`
- `Copy() -> Any`
- `CopyPicture(Appearance: XlPictureAppearance?, Format: XlCopyPictureFormat?) -> Any`
- `Cut() -> Any`
- `Delete() -> Any`
- `Duplicate() -> Dispatch`
- `Group() -> GroupObject`
- `Item(Index) -> Dispatch`
- `Select(Replace?) -> Any`
- `SendToBack() -> Any`

## ChartSeriesGradientStopData

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `StopColor: SeriesGradientStopColorFormat`
- `StopPositionType: XlGradientStopPositionType`
- `StopValue: Any`

## ChartTitle

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Border: Border`
- `Caption: Any`
- `Characters: Characters`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `Formula: Any`
- `FormulaLocal: Any`
- `FormulaR1C1: Any`
- `FormulaR1C1Local: Any`
- `Height: Any`
- `HorizontalAlignment: Any`
- `IncludeInLayout: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `Orientation: Any`
- `Parent: Any`
- `Position: XlChartElementPosition`
- `ReadingOrder: Any`
- `Shadow: Any`
- `Text: Any`
- `Top: Any`
- `VerticalAlignment: Any`
- `Width: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetCharacters(Start?, Length?) -> Characters`

## ChartView

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Parent: Any`
- `Sheet: Any`

## Charts

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
- `Add(Before?, After?, Count?) -> Chart`
- `Add2(Before?, After?, Count?, NewLayout?) -> Chart`
- `Copy(Before?, After?) -> None`
- `Delete() -> None`
- `Move(Before?, After?) -> None`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Select(Replace?) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `_Default(Index) -> Dispatch`
- `Item(Index) -> Dispatch`

## Corners

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Select() -> Any`

## DataLabel

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `AutoText: Any`
- `Border: Border`
- `Caption: Any`
- `Characters: Characters`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `Formula: Any`
- `FormulaLocal: Any`
- `FormulaR1C1: Any`
- `FormulaR1C1Local: Any`
- `Height: Any`
- `HorizontalAlignment: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `NumberFormat: Any`
- `NumberFormatLinked: Any`
- `NumberFormatLocal: Any`
- `Orientation: Any`
- `Parent: Any`
- `Position: XlDataLabelPosition`
- `ReadingOrder: Any`
- `Separator: Any`
- `Shadow: Any`
- `ShowBubbleSize: Any`
- `ShowCategoryName: Any`
- `ShowLegendKey: Any`
- `ShowPercentage: Any`
- `ShowRange: Any`
- `ShowSeriesName: Any`
- `ShowValue: Any`
- `Text: Any`
- `Top: Any`
- `Type: Any`
- `VerticalAlignment: Any`
- `Width: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetCharacters(Start?, Length?) -> Characters`

## DataLabels

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `AutoText: Any`
- `Border: Border`
- `Count: Any`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `HorizontalAlignment: Any`
- `Interior: Interior`
- `Name: Any`
- `NumberFormat: Any`
- `NumberFormatLinked: Any`
- `NumberFormatLocal: Any`
- `Orientation: Any`
- `Parent: Any`
- `Position: XlDataLabelPosition`
- `ReadingOrder: Any`
- `Separator: Any`
- `Shadow: Any`
- `ShowBubbleSize: Any`
- `ShowCategoryName: Any`
- `ShowLegendKey: Any`
- `ShowPercentage: Any`
- `ShowRange: Any`
- `ShowSeriesName: Any`
- `ShowValue: Any`
- `Type: Any`
- `VerticalAlignment: Any`

**Methods:**
- `__call__(Index) -> DataLabel`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index) -> DataLabel`
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Item(Index) -> DataLabel`
- `Propagate(Index) -> None`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## DataTable

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Border: Border`
- `Creator: XlCreator`
- `Font: Font`
- `Format: ChartFormat`
- `HasBorderHorizontal: Any`
- `HasBorderOutline: Any`
- `HasBorderVertical: Any`
- `Parent: Any`
- `ShowLegendKey: Any`

**Methods:**
- `Delete() -> None`
- `Select() -> None`

## DisplayUnitLabel

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Border: Border`
- `Caption: Any`
- `Characters: Characters`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `Formula: Any`
- `FormulaLocal: Any`
- `FormulaR1C1: Any`
- `FormulaR1C1Local: Any`
- `Height: Any`
- `HorizontalAlignment: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `Orientation: Any`
- `Parent: Any`
- `Position: XlChartElementPosition`
- `ReadingOrder: Any`
- `Shadow: Any`
- `Text: Any`
- `Top: Any`
- `VerticalAlignment: Any`
- `Width: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

**Property Accessors** *(parameterized — must be called as method):*
- `GetCharacters(Start?, Length?) -> Characters`

## DownBars

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Interior: Interior`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## DropLines

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Format: ChartFormat`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `Select() -> Any`

## ErrorBars

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `EndStyle: XlEndStyleCap`
- `Format: ChartFormat`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `ClearFormats() -> Any`
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## Floor

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Interior: Interior`
- `Name: Any`
- `Parent: Any`
- `PictureType: Any`
- `Thickness: Any`

**Methods:**
- `ClearFormats() -> Any`
- `Paste() -> None`
- `Select() -> Any`

## FullSeriesCollection

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Series`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index) -> Series`
- `Item(Index) -> Series`

## Gridlines

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Format: ChartFormat`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## HiLoLines

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Format: ChartFormat`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `Select() -> Any`

## LeaderLines

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Format: ChartFormat`
- `Parent: Any`

**Methods:**
- `Delete() -> None`
- `Select() -> None`

## Legend

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Font: Font`
- `Format: ChartFormat`
- `Height: Any`
- `IncludeInLayout: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `Parent: Any`
- `Position: XlLegendPosition`
- `Shadow: Any`
- `Top: Any`
- `Width: Any`

**Methods:**
- `Clear() -> Any`
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `LegendEntries(Index?) -> Dispatch`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## LegendEntries

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> LegendEntry`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index) -> LegendEntry`
- `Item(Index) -> LegendEntry`

## LegendEntry

**Properties:**
- `Application: Application`
- `AutoScaleFont: Any`
- `Creator: XlCreator`
- `Font: Font`
- `Format: ChartFormat`
- `Height: Any`
- `Index: Any`
- `Left: Any`
- `LegendKey: LegendKey`
- `Parent: Any`
- `Top: Any`
- `Width: Any`

**Methods:**
- `Delete() -> Any`
- `Select() -> Any`

## LegendKey

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Height: Any`
- `Interior: Interior`
- `InvertIfNegative: Any`
- `Left: Any`
- `MarkerBackgroundColor: Any`
- `MarkerBackgroundColorIndex: XlColorIndex`
- `MarkerForegroundColor: Any`
- `MarkerForegroundColorIndex: XlColorIndex`
- `MarkerSize: Any`
- `MarkerStyle: XlMarkerStyle`
- `Parent: Any`
- `PictureType: Any`
- `PictureUnit: Any`
- `PictureUnit2: Any`
- `Shadow: Any`
- `Smooth: Any`
- `Top: Any`
- `Width: Any`

**Methods:**
- `ClearFormats() -> Any`
- `Delete() -> Any`
- `Select() -> Any`

## PlotArea

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Height: Any`
- `InsideHeight: Any`
- `InsideLeft: Any`
- `InsideTop: Any`
- `InsideWidth: Any`
- `Interior: Interior`
- `Left: Any`
- `Name: Any`
- `Parent: Any`
- `Position: XlChartElementPosition`
- `Top: Any`
- `Width: Any`

**Methods:**
- `ClearFormats() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## Point

**Properties:**
- `Application: Application`
- `ApplyPictToEnd: Any`
- `ApplyPictToFront: Any`
- `ApplyPictToSides: Any`
- `Border: Border`
- `Creator: XlCreator`
- `DataLabel: DataLabel`
- `Explosion: Any`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Has3DEffect: Any`
- `HasDataLabel: Any`
- `Height: Any`
- `Interior: Interior`
- `InvertIfNegative: Any`
- `IsTotal: Any`
- `Left: Any`
- `MarkerBackgroundColor: Any`
- `MarkerBackgroundColorIndex: XlColorIndex`
- `MarkerForegroundColor: Any`
- `MarkerForegroundColorIndex: XlColorIndex`
- `MarkerSize: Any`
- `MarkerStyle: XlMarkerStyle`
- `Name: Any`
- `Parent: Any`
- `PictureType: XlChartPictureType`
- `PictureUnit: Any`
- `PictureUnit2: Any`
- `SecondaryPlot: Any`
- `Shadow: Any`
- `Top: Any`
- `Width: Any`

**Methods:**
- `_ApplyDataLabels(Type: XlDataLabelsType?, LegendKey?, AutoText?, HasLeaderLines?) -> Any`
- `ApplyDataLabels(Type: XlDataLabelsType?, LegendKey?, AutoText?, HasLeaderLines?, ShowSeriesName?, ShowCategoryName?, ShowValue?, ShowPercentage?, ShowBubbleSize?, Separator?) -> Any`
- `ClearFormats() -> Any`
- `Copy() -> Any`
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Paste() -> Any`
- `PieSliceLocation(loc: XlPieSliceLocation, Index: XlPieSliceIndex?) -> float`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## Points

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index: int) -> Point`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index: int) -> Point`
- `Item(Index: int) -> Point`

## Series

**Properties:**
- `Application: Application`
- `ApplyPictToEnd: Any`
- `ApplyPictToFront: Any`
- `ApplyPictToSides: Any`
- `AxisGroup: XlAxisGroup`
- `BarShape: XlBarShape`
- `Border: Border`
- `BubbleSizes: Any`
- `ChartType: XlChartType`
- `Creator: XlCreator`
- `ErrorBars: ErrorBars`
- `Explosion: Any`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Formula: Any`
- `FormulaLocal: Any`
- `FormulaR1C1: Any`
- `FormulaR1C1Local: Any`
- `GeoMappingLevel: XlGeoMappingLevel`
- `GeoProjectionType: XlGeoProjectionType`
- `Has3DEffect: Any`
- `HasDataLabels: Any`
- `HasErrorBars: Any`
- `HasLeaderLines: Any`
- `Interior: Interior`
- `InvertColor: Any`
- `InvertColorIndex: Any`
- `InvertIfNegative: Any`
- `IsFiltered: Any`
- `LeaderLines: LeaderLines`
- `MarkerBackgroundColor: Any`
- `MarkerBackgroundColorIndex: XlColorIndex`
- `MarkerForegroundColor: Any`
- `MarkerForegroundColorIndex: XlColorIndex`
- `MarkerSize: Any`
- `MarkerStyle: XlMarkerStyle`
- `Name: Any`
- `Parent: Any`
- `ParentDataLabelOption: XlParentDataLabelOptions`
- `PictureType: XlChartPictureType`
- `PictureUnit: Any`
- `PictureUnit2: Any`
- `PlotColorIndex: Any`
- `PlotOrder: Any`
- `QuartileCalculationInclusiveMedian: Any`
- `RegionLabelOption: XlRegionLabelOptions`
- `SeriesColorGradientStyle: XlSeriesColorGradientStyle`
- `SeriesColorMaxGradientStop: ChartSeriesGradientStopData`
- `SeriesColorMidGradientStop: ChartSeriesGradientStopData`
- `SeriesColorMinGradientStop: ChartSeriesGradientStopData`
- `Shadow: Any`
- `Smooth: Any`
- `Type: Any`
- `Values: Any`
- `ValueSortOrder: XlValueSortOrder`
- `XValues: Any`

**Methods:**
- `_ApplyDataLabels(Type: XlDataLabelsType?, LegendKey?, AutoText?, HasLeaderLines?) -> Any`
- `ApplyCustomType(ChartType: XlChartType) -> None`
- `ApplyDataLabels(Type: XlDataLabelsType?, LegendKey?, AutoText?, HasLeaderLines?, ShowSeriesName?, ShowCategoryName?, ShowValue?, ShowPercentage?, ShowBubbleSize?, Separator?) -> Any`
- `ClearFormats() -> Any`
- `Copy() -> Any`
- `DataLabels(Index?) -> Dispatch`
- `Delete() -> Any`
- `ErrorBar(Direction: XlErrorBarDirection, Include: XlErrorBarInclude, Type: XlErrorBarType, Amount?, MinusValues?) -> Any`
- `GetProperty(ID: str) -> Any`
- `Paste() -> Any`
- `Points(Index?) -> Dispatch`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`
- `Trendlines(Index?) -> Dispatch`

## SeriesCollection

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index) -> Series`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index) -> Series`
- `Add(Source, Rowcol: XlRowCol?, SeriesLabels?, CategoryLabels?, Replace?) -> Series`
- `Extend(Source, Rowcol?, CategoryLabels?) -> Any`
- `Item(Index) -> Series`
- `NewSeries() -> Series`
- `Paste(Rowcol: XlRowCol?, SeriesLabels?, CategoryLabels?, Replace?, NewSeries?) -> Any`

## SeriesGradientStopColorFormat

**Properties:**
- `Application: Application`
- `Creator: XlCreator`
- `ObjectThemeColor: MsoThemeColorIndex`
- `Parent: Any`
- `RGB: Any`
- `TintAndShade: Any`
- `Transparency: Any`
- `Type: MsoColorType`

## SeriesLines

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Format: ChartFormat`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## TickLabels

**Properties:**
- `Alignment: Any`
- `Application: Application`
- `AutoScaleFont: Any`
- `Creator: XlCreator`
- `Depth: Any`
- `Font: Font`
- `Format: ChartFormat`
- `MultiLevel: Any`
- `Name: Any`
- `NumberFormat: Any`
- `NumberFormatLinked: Any`
- `NumberFormatLocal: Any`
- `Offset: Any`
- `Orientation: XlTickLabelOrientation`
- `Parent: Any`
- `ReadingOrder: Any`

**Methods:**
- `Delete() -> Any`
- `Select() -> Any`

## Trendline

**Properties:**
- `Application: Application`
- `Backward: Any`
- `Backward2: Any`
- `Border: Border`
- `Creator: XlCreator`
- `DataLabel: DataLabel`
- `DisplayEquation: Any`
- `DisplayRSquared: Any`
- `Format: ChartFormat`
- `Forward: Any`
- `Forward2: Any`
- `Index: Any`
- `Intercept: Any`
- `InterceptIsAuto: Any`
- `Name: Any`
- `NameIsAuto: Any`
- `Order: Any`
- `Parent: Any`
- `Period: Any`
- `Type: XlTrendlineType`

**Methods:**
- `ClearFormats() -> Any`
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## Trendlines

**Properties:**
- `Application: Application`
- `Count: Any`
- `Creator: XlCreator`
- `Parent: Any`

**Methods:**
- `__call__(Index?) -> Trendline`
- `__getitem__(key) -> Any`
- `__len__() -> Any`
- `__nonzero__() -> Any`
- `_Default(Index?) -> Trendline`
- `Add(Type: XlTrendlineType?, Order?, Period?, Forward?, Backward?, Intercept?, DisplayEquation?, DisplayRSquared?, Name?) -> Trendline`
- `Item(Index?) -> Trendline`

## UpBars

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Interior: Interior`
- `Name: Any`
- `Parent: Any`

**Methods:**
- `Delete() -> Any`
- `GetProperty(ID: str) -> Any`
- `Select() -> Any`
- `SetProperty(ID: str, Value) -> None`

## Walls

**Properties:**
- `Application: Application`
- `Border: Border`
- `Creator: XlCreator`
- `Fill: ChartFillFormat`
- `Format: ChartFormat`
- `Interior: Interior`
- `Name: Any`
- `Parent: Any`
- `PictureType: Any`
- `PictureUnit: Any`
- `Thickness: Any`

**Methods:**
- `ClearFormats() -> Any`
- `Paste() -> None`
- `Select() -> Any`

## Chart
*Bases: _Chart*

## _Chart

**Properties:**
- `Application: Application`
- `Area3DGroup: ChartGroup`
- `AutoScaling: Any`
- `BackWall: Walls`
- `Bar3DGroup: ChartGroup`
- `BarShape: XlBarShape`
- `CategoryLabelLevel: XlCategoryLabelLevel`
- `ChartArea: ChartArea`
- `ChartColor: Any`
- `ChartStyle: Any`
- `ChartTitle: ChartTitle`
- `ChartType: XlChartType`
- `CodeName: Any`
- `Column3DGroup: ChartGroup`
- `Corners: Corners`
- `Creator: XlCreator`
- `DataTable: DataTable`
- `DepthPercent: Any`
- `DisplayBlanksAs: XlDisplayBlanksAs`
- `DisplayValueNotAvailableAsBlank: Any`
- `Elevation: Any`
- `Floor: Floor`
- `GapDepth: Any`
- `HasAxis: Any`
- `HasDataTable: Any`
- `HasHiddenContent: Any`
- `HasLegend: Any`
- `HasPivotFields: Any`
- `HasTitle: Any`
- `HeightPercent: Any`
- `Hyperlinks: Hyperlinks`
- `Index: Any`
- `Legend: Legend`
- `Line3DGroup: ChartGroup`
- `MailEnvelope: MsoEnvelope`
- `Name: Any`
- `Next: Any`
- `OnDoubleClick: Any`
- `OnSheetActivate: Any`
- `OnSheetDeactivate: Any`
- `PageSetup: PageSetup`
- `Parent: Any`
- `Perspective: Any`
- `Pie3DGroup: ChartGroup`
- `PivotLayout: PivotLayout`
- `PlotArea: PlotArea`
- `PlotBy: XlRowCol`
- `PlotVisibleOnly: Any`
- `Previous: Any`
- `PrintedCommentPages: Any`
- `ProtectContents: Any`
- `ProtectData: Any`
- `ProtectDrawingObjects: Any`
- `ProtectFormatting: Any`
- `ProtectGoalSeek: Any`
- `ProtectionMode: Any`
- `ProtectSelection: Any`
- `RightAngleAxes: Any`
- `Rotation: Any`
- `Scripts: Scripts`
- `SeriesNameLevel: XlSeriesNameLevel`
- `Shapes: Shapes`
- `ShowAllFieldButtons: Any`
- `ShowAxisFieldButtons: Any`
- `ShowDataLabelsOverMaximum: Any`
- `ShowExpandCollapseEntireFieldButtons: Any`
- `ShowLegendFieldButtons: Any`
- `ShowReportFilterFieldButtons: Any`
- `ShowValueFieldButtons: Any`
- `ShowWindow: Any`
- `SideWall: Walls`
- `SizeWithWindow: Any`
- `SubType: Any`
- `SurfaceGroup: ChartGroup`
- `Tab: Tab`
- `Type: Any`
- `Visible: XlSheetVisibility`
- `Walls: Walls`
- `WallsAndGridlines2D: Any`

**Methods:**
- `_ApplyDataLabels(Type: XlDataLabelsType?, LegendKey?, AutoText?, HasLeaderLines?) -> None`
- `_Evaluate(Name) -> Any`
- `_ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?) -> None`
- `_PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `_PrintOut_(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?) -> None`
- `_Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?) -> None`
- `_SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `_SaveAs_(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?) -> None`
- `Activate() -> None`
- `ApplyChartTemplate(Filename: str) -> None`
- `ApplyCustomType(ChartType: XlChartType, TypeName?) -> None`
- `ApplyDataLabels(Type: XlDataLabelsType?, LegendKey?, AutoText?, HasLeaderLines?, ShowSeriesName?, ShowCategoryName?, ShowValue?, ShowPercentage?, ShowBubbleSize?, Separator?) -> None`
- `ApplyLayout(Layout: int, ChartType?) -> None`
- `Arcs(Index?) -> Dispatch`
- `AreaGroups(Index?) -> Dispatch`
- `AutoFormat(Gallery: int, Format?) -> None`
- `Axes(Type, AxisGroup: XlAxisGroup?) -> Dispatch`
- `BarGroups(Index?) -> Dispatch`
- `Buttons(Index?) -> Dispatch`
- `ChartGroups(Index?) -> Dispatch`
- `ChartObjects(Index?) -> Dispatch`
- `ChartWizard(Source?, Gallery?, Format?, PlotBy?, CategoryLabels?, SeriesLabels?, HasLegend?, Title?, CategoryTitle?, ValueTitle?, ExtraTitle?) -> None`
- `CheckBoxes(Index?) -> Dispatch`
- `CheckSpelling(CustomDictionary?, IgnoreUppercase?, AlwaysSuggest?, SpellLang?) -> None`
- `ClearToMatchColorStyle() -> None`
- `ClearToMatchStyle() -> None`
- `ColumnGroups(Index?) -> Dispatch`
- `Copy(Before?, After?) -> None`
- `CopyChartBuild() -> None`
- `CopyPicture(Appearance: XlPictureAppearance?, Format: XlCopyPictureFormat?, Size: XlPictureAppearance?) -> None`
- `CreatePublisher(Edition, Appearance: XlPictureAppearance?, Size: XlPictureAppearance?, ContainsPICT?, ContainsBIFF?, ContainsRTF?, ContainsVALU?) -> None`
- `Delete() -> None`
- `DeleteHiddenContent() -> None`
- `Deselect() -> None`
- `DoughnutGroups(Index?) -> Dispatch`
- `DrawingObjects(Index?) -> Dispatch`
- `Drawings(Index?) -> Dispatch`
- `DropDowns(Index?) -> Dispatch`
- `Evaluate(Name) -> Any`
- `Export(Filename: str, FilterName?, Interactive?) -> bool`
- `ExportAsFixedFormat(Type: XlFixedFormatType, Filename?, Quality?, IncludeDocProperties?, IgnorePrintAreas?, From?, To?, OpenAfterPublish?, FixedFormatExtClassPtr?, WorkIdentity?) -> None`
- `FullSeriesCollection(Index?) -> Dispatch`
- `GetChartElement(x: int, y: int, ElementID: int, Arg1: int, Arg2: int) -> None`
- `GetProperty(ID: str) -> Any`
- `GroupBoxes(Index?) -> Dispatch`
- `GroupObjects(Index?) -> Dispatch`
- `Labels(Index?) -> Dispatch`
- `LineGroups(Index?) -> Dispatch`
- `Lines(Index?) -> Dispatch`
- `ListBoxes(Index?) -> Dispatch`
- `Location(Where: XlChartLocation, Name?) -> Chart`
- `Move(Before?, After?) -> None`
- `OLEObjects(Index?) -> Dispatch`
- `OptionButtons(Index?) -> Dispatch`
- `Ovals(Index?) -> Dispatch`
- `Paste(Type?) -> None`
- `Pictures(Index?) -> Dispatch`
- `PieGroups(Index?) -> Dispatch`
- `PrintOut(From?, To?, Copies?, Preview?, ActivePrinter?, PrintToFile?, Collate?, PrToFileName?) -> None`
- `PrintPreview(EnableChanges?) -> None`
- `Protect(Password?, DrawingObjects?, Contents?, Scenarios?, UserInterfaceOnly?) -> None`
- `RadarGroups(Index?) -> Dispatch`
- `Rectangles(Index?) -> Dispatch`
- `Refresh() -> None`
- `SaveAs(Filename: str, FileFormat?, Password?, WriteResPassword?, ReadOnlyRecommended?, CreateBackup?, AddToMru?, TextCodepage?, TextVisualLayout?, Local?) -> None`
- `SaveChartTemplate(Filename: str) -> None`
- `ScrollBars(Index?) -> Dispatch`
- `Select(Replace?) -> None`
- `SeriesCollection(Index?) -> Dispatch`
- `SetBackgroundPicture(Filename: str) -> None`
- `SetDefaultChart(Name) -> None`
- `SetElement(Element: MsoChartElementType) -> None`
- `SetProperty(ID: str, Value) -> None`
- `SetSourceData(Source: Range, PlotBy?) -> None`
- `Spinners(Index?) -> Dispatch`
- `TextBoxes(Index?) -> Dispatch`
- `Unprotect(Password?) -> None`
- `XYGroups(Index?) -> Dispatch`

**Property Accessors** *(parameterized — must be called as method):*
- `GetHasAxis(Index1?, Index2?) -> Any`
- `SetHasAxis(Index1, Index2?, arg2) -> None`

