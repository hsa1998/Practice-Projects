#! python3

'''
1. import files to be converted onto excel
2. open an excel doc
3. assign readlines() to a variable that can be transposed onto a spreadsheet
4. save excel doc
'''

import sys
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

for doc in range(len(sys.argv[0:-1])):
    file = open(sys.argv[doc+1], 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        sheet.cell(row=i+1,column=doc+1).value = lines[i]

wb.save('testDoc.xlsx')

