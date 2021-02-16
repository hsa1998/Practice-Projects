#! python3
# Function: a extension of Ch8Proj2 but includes delete functions
# Usage: py.exe Ch8Proj2-1.pyw save <keyword> - saves clipboard to keyword
#      : py.exe Ch8Proj2-1.pyw <keyword> - loads keyword to clipboard
#      : py.exe Ch8Proj2-1.pyw list - loads all keywords to clipboard
#      : py.exe Ch8Proj2-1.pyw delete <keyword> - deletes keyword from saves
#      : py.exe Ch8Proj2-1.pyw delete - deletes all

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf.remove(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
