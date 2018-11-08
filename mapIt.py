#! python3
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()
    
webbrowser.open('http://www.google.com/maps/place/' + adress)