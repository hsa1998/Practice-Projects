#! python3

import os, re

files = os.listdir(os.getcwd())

txtRegex = re.compile(r'[.*]txt$')

userSearch = input('Type in an expression that you wish to search:\n>>> ')
regex = re.compile(r'%s' % userSearch, re.I)

none = 0

for i in files:
    found = txtRegex.search(i)
    if found is not None:

        x = open(i, 'r')
        file = x.read()
        x.close()

        found = regex.findall(file)
        if len(found) > 0:
            print('%s was found in %s' % (userSearch, i))
            none = none + 1
if none == 0:
    print('There were no matches. Please try a different expression or try again. ')


