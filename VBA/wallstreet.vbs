' VBA Coding for the WallStreet Assignment
Sub Ticker()

  'Define variables
  Dim Sht As Integer
  Dim SheetCount As Integer
  Dim LastRow As Double
  Dim RowCount As Double
  Dim TickerCount As Long
  Dim Symbol As String
  Dim LastSymbol As String
  Dim Opened As Double
  Dim Closed As Double
  Dim LastClosed As Double
  Dim Change As Double
  Dim PctChange As Double
  Dim Volume As Double
  Dim IncSymbol As String
  Dim IncPct As Double
  Dim DecSymbol As String
  Dim DecPct As Double
  Dim Totsymbol As String
  Dim Totvolume As Double
  
  
  Application.ScreenUpdating = False
  
  SheetCount = ActiveWorkbook.Worksheets.Count

   'For each sheet in the workbook
    For Sht = 1 To SheetCount
        'Activate the sheet
        Sheets(Sht).Activate
        
        'Figure out the number of rows in the sheet and set values
        LastRow = Cells.SpecialCells(xlCellTypeLastCell).Row
        TickerCount = 1
        LastSymbol = ""
        IncSymbol = ""
        DecSymbol = ""
        Totsymbol = ""
        IncPct = 0
        DecPct = 0
        Totvolume = 0
        
        'Insert Headers into the summary section
        Cells(1, 9).Value = "Ticker"
        Cells(1, 10).Value = "Yearly Change"
        Cells(1, 11).Value = "Pct Change"
        Cells(1, 12).Value = "Total Stock Volume"
        
        Cells(2, 14).Value = "Greatest % Increase"
        Cells(3, 14).Value = "Greatest % Decrease"
        Cells(4, 14).Value = "Greatest Total Volume"
        
        Cells(1, 15).Value = "Ticker"
        Cells(1, 16).Value = "Value"
        
        'Loop through all the rows to the end
        For RowCount = 2 To LastRow
           
           'Pull in symbol and check if it is new
           Symbol = Cells(RowCount, 1).Value
           If Symbol <> LastSymbol Then
           
           'Put in prior symbol's row into the summary (except first time)
           If TickerCount <> 1 Then
                'Calculate the changes
                Change = Closed - Opened
                If Opened = 0 Then PctChange = 0 Else PctChange = Round(Change / Opened, 5)
                Cells(TickerCount, 9).Value = LastSymbol
                Cells(TickerCount, 10).Value = Change
                Cells(TickerCount, 11).Value = PctChange
                Cells(TickerCount, 11).NumberFormat = "0.00%"
                Cells(TickerCount, 12).Value = Volume
                'Check if highest volume
                If Volume > Totvolume Then
                  Totvolume = Volume
                  Totsymbol = LastSymbol
                End If
                'color the change field and check if greatest or least
                If Change >= 0 Then
                  Cells(TickerCount, 10).Interior.ColorIndex = 4
                  If PctChange > IncPct Then
                    IncPct = PctChange
                    IncSymbol = LastSymbol
                  End If
                  
                Else
                  Cells(TickerCount, 10).Interior.ColorIndex = 3
                  If PctChange < DecPct Then
                    DecPct = PctChange
                    DecSymbol = LastSymbol
                  End If
                End If
           End If
           
           'Add to the count
           TickerCount = TickerCount + 1
           'Pull in Opening and closing and Start running Volume again
            Opened = Cells(RowCount, 3).Value
            Closed = Cells(RowCount, 6).Value
            Volume = Cells(RowCount, 7).Value
          Else
            'Add to the running total and grab new closed data
            Closed = Cells(RowCount, 6).Value
            Volume = Volume + Cells(RowCount, 7).Value
          End If
        
        'Reset Last Symbol
        LastSymbol = Symbol
        
        Next RowCount
        
        
        'Add final summary row
        Change = Opened - Closed
        PctChange = Change / Opened
        Cells(TickerCount, 9).Value = LastSymbol
        Cells(TickerCount, 10).Value = Change
        Cells(TickerCount, 11).Value = PctChange
        Cells(TickerCount, 11).NumberFormat = "0.00%"
        Cells(TickerCount, 12).Value = Volume
        'Check if highest volume
        If Volume > Totvolume Then
          Totvolume = Volume
          Totsymbol = LastSymbol
        End If
        'color the change field and check if greatest or least
        If Change >= 0 Then
          Cells(TickerCount, 10).Interior.ColorIndex = 4
          If PctChange > IncPct Then
            IncPct = PctChange
            IncSymbol = LastSymbol
          End If
        Else
          Cells(TickerCount, 10).Interior.ColorIndex = 3
          If PctChange < DecPct Then
            DecPct = PctChange
            DecSymbol = LastSymbol
          End If
        End If
 
     'Put in the values for greatest increase, decrease, and volume
    Cells(2, 15).Value = IncSymbol
    Cells(2, 16).Value = IncPct
    Cells(2, 16).NumberFormat = "0.00%"
    Cells(3, 15).Value = DecSymbol
    Cells(3, 16).Value = DecPct
    Cells(3, 16).NumberFormat = "0.00%"
    Cells(4, 15).Value = Totsymbol
    Cells(4, 16).Value = Totvolume
        
    Next Sht


Application.ScreenUpdating = True
  
End Sub
