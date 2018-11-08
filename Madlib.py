import re

def libInput(x):
    x = x.lower()
    if x == 'adjective':
        print('Enter an %s:'% (x), end = '')
        return input()
    else:
        print('Enter a %s:'% (x), end = '')
        return input()
    
def madlibreplacer(x):
    madlibSentence = x
    #ADJECTIVE, NOUN, ADVERB, or VERB
    regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    mo = regex.search(madlibSentence)
    while mo != None:
        foundTerm = mo.group() #found term = first instance found
        newTerm = libInput(foundTerm) #libinput first instance found
        wordReplace = re.compile(foundTerm) #wordreplace = search for found term
        madlibSentence = wordReplace.sub(newTerm , madlibSentence, 1) #replace term in madlibSentence
        mo = regex.search(madlibSentence) #search madlib
        print(madlibSentence)

txtfile = open('.//PT//madlib.txt')
text = txtfile.read()
madlibreplacer(text)
txtfile.close()


#WAY WAY WAY BETTER
#regex = re.compile(r'ADJECTIVE|NOUN|VERB')
#
#
#for i in regex.findall(text):
#    inp_text = input('Enter the substitute for %s: ' %i)
#    text = regex.sub(inp_text, text, 1)
#
#print(text)