import re

stripChar = input('Strip Character: >> ')
context = input('String: >> ')
stripContext = None

def strip(char, string):

    if char == '':
        regsp = re.compile(r'^\s+|\s+|\s+$')
        stripContext = regsp.sub('', context)
        return stripContext
    else:
        regsp = re.compile(r'^(%s)+|(%s)+|(%s)+$'%(char,char,char))
        stripContext = regsp.sub('', context)
        return stripContext

print(strip(stripChar, context))

