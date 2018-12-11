

# -*- coding: utf-8 -*-
"""
@author: Ryan Piersma
"""

from nltk.tokenize import RegexpTokenizer
import os, fnmatch
#Some code from:
#https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer

#data structure for holding sequences:
# Dictionary where key = a word, value = a pair consisting of
# a word that follows it and the number of times that it has
# occurred after that word

def createWordSequences(corpus):
    seqDict = {}
    startRead = False
    tokenizer = RegexpTokenizer(r'\w+')
    lastWordLastLine = "dummyword"
    for line in corpus.readlines():
        if line.find("FOOTNOTES") != -1:
            break
        if startRead:
            tokenized = tokenizer.tokenize(line)
            words = [w.lower() for w in tokenized]
            
            #Handle the sequence between last word of one line and first word
            #of next line
            if len(words) > 0:
                firstWordCurLine = words[0]
                if not lastWordLastLine == "dummyword":
                    if lastWordLastLine in seqDict:
                        if not any(firstWordCurLine in d for d in seqDict[lastWordLastLine]):
                            seqDict[lastWordLastLine].append({firstWordCurLine : 1})
                        else:
                            wordIndex = -1
                            for d in seqDict[lastWordLastLine]:
                                if firstWordCurLine in d:
                                    wordIndex = seqDict[lastWordLastLine].index(d)
                                    seqDict[lastWordLastLine][wordIndex][firstWordCurLine] += 1
                    else:
                        seqDict[lastWordLastLine] = [{firstWordCurLine : 1}] 
            
            #Handle sequences that happen on a single line
            for i in range(len(words) - 1):
                if words[i] in seqDict:
                    if not any(words[i+1] in d for d in seqDict[words[i]]):
                        seqDict[words[i]].append({words[i+1] : 1})
                    else:
                        wordIndex = -1
                        for d in seqDict[words[i]]:
                            if words[i+1] in d:
                                wordIndex = seqDict[words[i]].index(d)
                        seqDict[words[i]][wordIndex][words[i+1]] += 1
                else:
                   seqDict[words[i]] = [{words[i+1] : 1}] 
                   
            #Store the last word on the line
            if (len(words) > 0):
                lastWordLastLine = words[len(words) - 1]
            
        if line.find("START OF THE PROJECT GUTENBERG EBOOK"):
            startRead = True
    #print(seqDict)
    return seqDict
     
#Source for this function: https://stackoverflow.com/questions/13299731/python-need-to-loop-through-directories-looking-for-txt-files
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)
            
def convertToList(listDict, bookID):
    listTuples = []
    beforeWord = ""
    for key,dictList in listDict.items():
        beforeWord = key
        for dict in dictList:
            for afterWord,timesFound in dict.items():
                listTuples.append(tuple([beforeWord, bookID, afterWord, timesFound]))
    return listTuples
   
def main():
    tupleLists = []
    csvWrite = open("sequences.csv","w+")
    #put path here
    directory = "C:/Users/ryanp/Desktop/Duke/Fall 2018/CS 316- Databases/Final Project/LingusticDB-database/books/books"
    for filename in findFiles(directory, "[0-9]*.txt"):
        print(filename)
        filenamePartition = filename.rsplit("\\") #change for Linux I think
        bookId = filenamePartition[-1][:-4]
        f = open(filename,"r",encoding = "ISO-8859-1")
        createSequences = createWordSequences(f)
        addThisToTupleList = convertToList(createSequences, bookId)
        for tuple in addThisToTupleList:
            csvWrite.write(tuple[0] + "|" + tuple[1] + "|" + tuple[2] + "|" + str(tuple[3]) + "\n")
    csvWrite.close()
    return tupleLists
   
main()