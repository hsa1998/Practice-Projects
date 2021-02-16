#! python3

'''
need to create a multiplication table from a user inputted integer
1. collect user input
2. create a workbook
3. loop over rows and columns for n number of times to find the multiplication table
3. save workbook
'''

import sys, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
num = 5
#num = sys.argv[1]

for row in range(1, num+2):
    for col in range(1, num+2):
        if row == 1 and col == 1:
            sheet.cell(row=row, column=col).value = ''
        elif row == 1:
            sheet.cell(row=row, column=col).value = col-1
        elif col == 1:
            sheet.cell(row=row, column=col).value = row-1
        else:
            sheet.cell(row=row, column=col).value = (row-1)*(col-1)

wb.save('MultTable%s.xlsx' % str(num))
