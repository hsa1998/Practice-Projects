#! python3
# Will find exceptionally large files in a given folder

import os

folder = os.path.abspath(os.getcwd())
size = 100

for i in os.listdir(folder):
    fileSize = os.path.getsize(i)
    if fileSize > 100:
        print('%s is %d MB and should be deleted.' % (i, fileSize))
