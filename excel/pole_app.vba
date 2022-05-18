' by Eve. This macro sorts and places the desired year's records onto TCA Year Summary

Sub CopyRow2()
'Declare variables
    Dim sheetNo20 As Worksheet
    Dim sheetNo25 As Worksheet
    Dim FinalRow As Long
    Dim Cell As Range
'Set variables
    Set sheetNo1 = Sheets("NHPoleCatalog")
    Set sheetNo2 = Sheets("TCA Year Summary")
'Clear destination sheet
    sheetNo2.Cells.Clear
'Type a command to select the entire row
    Selection.EntireRow.Select
' Define destination sheets to move row
    FinalRow1 = sheetNo1.Range("A" & sheetNo1.Rows.Count).End(xlUp).Row
    FinalRow2 = sheetNo2.Range("A" & sheetNo2.Rows.Count).End(xlUp).Row
    With sheetNo1
'Apply loop for column E until last cell with value
    For Each Cell In .Range("B1:B" & .Cells(.Rows.Count, "B").End(xlUp).Row)
'Apply condition to match the "Sold" value
        If Cell.Value = "2022" Or Cell.Value = "YEAR" Then
'Command to Copy and move to a destination Sheet "Sold2"
            .Rows(Cell.Row).Copy Destination:=sheetNo2.Rows(FinalRow2 + 1)
            FinalRow2 = FinalRow2 + 1
'Apply condition to match the "Unsold" value
        Else
        End If
     Next Cell
    End With
End Sub
