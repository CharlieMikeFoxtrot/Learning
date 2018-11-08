import re
text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
#regex = re.compile(r'(NOUN)')
#mo = regex.search(tstr)
#print(regex.sub('TEST',tstr))




regex = re.compile(r'ADJECTIVE|NOUN|VERB')


for i in regex.findall(text):
    inp_text = input('Enter the substitute for %s: ' %i)
    text = regex.sub(inp_text, text, 1)

print(text)