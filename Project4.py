import copy

spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(len(spam)):
    if i != len(spam) - 1:
        print(spam[i], end = " and ")
    elif i == len(spam) - 1:
        print(spam[i] + '.')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for x in range(0,6):
    for y in range(0,9):
        print(grid[y][x], end='')
    print()
