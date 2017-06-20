import openpyxl

wb = openpyxl.load_workbook('adding_commas.xlsx')
sheet = wb.get_sheet_by_name('randomnums')
output_sheet = wb.create_sheet('randomnums_with_commas')

for i in range(1, 200):
    output_sheet.cell(row=i, column=1).value = str(sheet.cell(row=i, column=1).value) + ', '

wb.save("adding_commas.xlsx")
