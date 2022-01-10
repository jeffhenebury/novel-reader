import string
import re

fhand = open('novel.txt',  encoding="utf8")
lineCount = 0
uniqueWordList = []
wordLib = dict()
for line in fhand :
    line = line.rstrip().lower()
    lineCount += 1
   # print(line)
    # get rid of any punctuation
    lineNoPunct = re.sub(r'[^\w\s]', '', line)
    words = lineNoPunct.split()
    #print(words)
    for word in words:
        #word.translate(None, string.punctuation)   #doesnt work
       # wordNoPunct = re.sub(r'[^\w\s]', '', word) #trying it earlier

       #below is for doing it by list, which i don't think is going to work
       #  if word not in uniqueWordList:
       #      #check for punctuation
       #      uniqueWordList.append(word)
       #      print(word + ' has been added to the word list.')
        if word not in wordLib:
            wordLib[word] = 1
            print('TEST: A unique word has been added to the list:', word)
        else:
            wordLib[word] += 1
            print('TEST: the word ... ', word, 'has been used again.' )

print('Line Count:', lineCount)
#print(('How many unique words you used: ' + str(len(uniqueWordList))))
print(wordLib)