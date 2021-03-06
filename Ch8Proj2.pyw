#! python3
# function: saves and loads pieces of text to clipboard
# Usage: py.exe Ch8Proj2.pyw save <keyword> - saves clipboard to keyword
#      : py.exe Ch8Proj2.pyw <keyword> - loads keyword to clipboard
#      : py.exe Ch8Proj2.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
