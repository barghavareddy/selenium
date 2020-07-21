import openpyxl
path="C:\exeldata\Financial Sample.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active
for i in range(1,5):
    for j in range(1,5):
        sheet.cell(row=i,column=j).value="welcome"
        #print(sheet.cell(row=i,column=j).value)
workbook.save(path)
