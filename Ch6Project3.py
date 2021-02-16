import pprint

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
colWidths = [0] * len(tableData)


def printTable():

    for i in range(len(tableData)):
        listi = tableData[i]
        a = i
        maxlen = 0
        for i in range(len(listi)):
            if len(listi[i]) > maxlen:
                maxlen = len(listi[i])
        colWidths[a] = maxlen

    justifiedData = []

    for i in range(len(tableData)):
        interim = colWidths[i]
        listi = tableData[i]
        for i in range(len(listi)):
            listi[i] = listi[i].rjust(interim)


    for x in range(0,4):
        for y in range(0,3):
            print(tableData[y][x], end=" ")
        print()


