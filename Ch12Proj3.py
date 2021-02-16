#! python 3
'''
1. will need to take 3 cmd args:
    a. 1st is which row to begin at
    b. how many rows to insert
    c. file name to apply row inserter to
2. open file
3. find the location at which rows want to be inserted
4. insert the rows requested
'''

import openpyxl
import sys

filename = sys.argv[3]
rowLoc = int(sys.argv[1])
rowCount = int(sys.argv[2])

wb = openpyxl.load_workbook(filename)
sheet = wb.active

sheet.insert_rows(rowLoc,rowCount)

wb.save(filename)
