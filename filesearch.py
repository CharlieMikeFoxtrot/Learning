import re, os
term = input('Search Term: ')
regex = re.compile(term)

found = 0
flist = []
for f in os.listdir('.'):
    if f.endswith('.txt'):
        text = open('.\\'+ f)
        text = text.read()
        if regex.search(text) != None:
            found += 1
            flist += [f]
        open('.\\'+ f).close()
if found > 0:
    if found == 1:
        print('Found search term "%s" in the following document:' %(term))
    else:
        print('Found search term "%s" in the following %s document(s):' %(term, str(found)))
    print(flist)
else:
    print("No instance of search term found.")