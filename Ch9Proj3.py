#! python3
# undone!

import os, re, shutil

folder = os.path.abspath(os.getcwd())

def getFilesWithPrefix(folder, prefix):                     # returns a sorted list of files that match the regex
    regex = re.compile(prefix + r'((\d{1,})(.\w+))')
    fileList = sorted([file for file in os.listdir(folder) if regex.match(file)])
    return fileList

def fillGaps(folder, prefix):
    fileList = getFilesWithPrefix(folder, prefix)           # sorted file list from getFilesWithPrefix
    regex = re.compile(prefix + r'(\d{1,})(.\w+)')

    start = int(regex.search(fileList[0].group[1]))         # starting with smallest number in list
    count = start                                           # creating a count to be used for gaps
    max_length = len(regex.search(fileList[-1].group(1)))   # max length to filter down any gaps

    for file in fileList:

        mo = regex.search(file)
        fileNum = int(mo.group(1))

        if fileNum != count:
            newFileName = prefix + '0'*(max_length-len(str(fileNum))) + str(count) + mo.group(2)
                        # creates new file name for first in sequence
            shutil.move(os.path.abspath(file), os.path.abspath(newFileName))
                        # renames old file to new file


        count += 1
