#! python3
#mcb.pyw- save and load pieces of text to clipboard

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('.\\PT\\mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]]= pyperclip.paste() 
    
#TODO: Delete key`
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    
# TODO: List keywords and load content.
elif len(sys.argv) == 2:
    #list keywords
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    #clear keys
    elif sys.argv[1].lower() == 'clear':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
mcbShelf.close()