#! python3

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|(\d{3}))?                           # area code
    (\s|-|\.)                               # seperator
    (\d{3})                                     # phone number
    (\s|-|\.)                               # seperator
    (\d{4})                                     # phone number
    (\s*(ext|x|ext.)\s*(\d{2,5}))?               # extension code
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # first part
    @                   # @
    [a-zA-Z0_9.-]+      # 
    (\.[a-zA-Z]{2,4})   
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[4], groups[6]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
#647.825.2498
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found in copied text.')
