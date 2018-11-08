#check order

import re, os
regex = re.compile('(0*)(\d+)')
previous = 0

for file in os.listdir('.//spam'):
    if regex.search(file) == None:
        continue
    else:
        if int(regex.search(file).group(2)) - int(previous) == 1:
            previous = int(regex.search(file).group(2))
        else: 
            previous +=1
            if int(regex.search(file).group(2)) > 9 and previous < 10:
                os.rename('.//spam//'+file,'.//spam//'+regex.sub(r'\g<1>0' + str(previous) ,file))
            else:
                os.rename('.//spam//'+file,'.//spam//'+regex.sub(r'\g<1>' + str(previous) ,file))