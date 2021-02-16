#! python3
# Function: This program will input a text file and then create a mad lib based on inputs
# Usage: py.exe Ch8Proj3.py - will use a preexisting file and create a user-generated madlib

import re

blanktxt = open('ml.txt')
madLib = blanktxt.read() #this is the full text as a string
content = madLib.split() #this is the madlib indexed into its individual parts
blanktxt.close()

count = 0 # we need a counter to run through each of the individual indexes within content
for i in content: #this will loop through each of the strings in the indexed variable
    if 'ADJECTIVE' in i:
        regex = re.compile(r'ADJECTIVE')
        content[count] = regex.sub(input('Choose an Adjective:\n>>> '), i)
    elif 'VERB' in i:
        regex = re.compile(r'VERB')
        content[count] = regex.sub(input('Choose a Verb:\n>>> '), i)
    elif 'NOUN' in i:
        regex = re.compile(r'NOUN')
        content[count] = regex.sub(input('Choose a Noun:\n>>> '), i)
    elif 'ADVERB' in i:
        regex = re.compile(r'ADVERB')
        content[count] = regex.sub(input('Choose an adverb:\n>>> '), i)
    count = count + 1

newMadLib = ' '.join(content)
print(newMadLib)

newFile = open('CompletedMadLib', 'w')
newFile.write(newMadLib)
newFile.close()
