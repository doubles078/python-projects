import openpyxl



wb = openpyxl.load_workbook('randomnums.xlsx')
sheet = wb.get_sheet_by_name('randomnums')

for i in range(1, 255):
    sheet.cell(row=i, column=1).value = str(sheet.cell(row=i, column=1).value) + ', '

wb.save("comma_output.xlsx")
