#! python3
import os, shutil

folder = os.path.abspath('C:\\Users\\afrid\\Desktop\\Python\\Python Bootcamp')
newFolder = folder + '\\pyFiles'
os.chdir(folder)

if newFolder[len(newFolder)-7:len(newFolder)] not in os.listdir(folder):
    os.makedirs(newFolder)

for i in os.listdir(folder):
    if i.endswith('.py'):
        shutil.copy(i, newFolder)
    else:
        continue
