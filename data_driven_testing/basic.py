from openpyxl import Workbook

"""
* Spreadsheet or workbook means: main file you are creating or working with.

* Worksheet or sheet: Sheet used to convert different kind of content withing the same spreadsheet. A `Spreadsheet` can 
can have one or more sheet.

* Column : Vertical line of sheet.

* Row: Horizontal line of sheet, represented by 1.

* Cell: Cell is combination of column and row.

"""

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"
workbook.save(filename="./hello_world.xlsx")
