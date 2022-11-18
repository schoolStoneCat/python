import re

regex = re.compile(r'^/d+$')
mo = regex.search('1999305')

if mo == None:
    print('no match found.')
else:
    print(mo.group())
    
mo = regex.search('99food234')

if mo == None:
    print('no match found.')
else:
    print(mo.group())