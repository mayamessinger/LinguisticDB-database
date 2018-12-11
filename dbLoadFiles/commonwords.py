# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""
@author: Ryan Piersma
"""

from nltk.tokenize import RegexpTokenizer
import os, fnmatch


def createWordCounts(corpus):
    commonDict = {}
    startRead = False
    tokenizer = RegexpTokenizer(r'\w+')
    for line in corpus.readlines():
        if line.find("FOOTNOTES") != -1:
            break
        if startRead:
            tokenized = tokenizer.tokenize(line)
            words = [w.lower() for w in tokenized]
            for word in words:
                if word in commonDict:
                    commonDict[word] += 1
                else:
                    commonDict[word] = 1
        if line.find("START OF THE PROJECT GUTENBERG EBOOK"):
            startRead = True
    #print(seqDict)
    return commonDict
     
#Source for this function: https://stackoverflow.com/questions/13299731/python-need-to-loop-through-directories-looking-for-txt-files
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)
            
def generateTuples(dict, bookID):
    tuples = []
    for word,frequency in dict.items():
        tuples.append(tuple([bookID, word, frequency]))
    return tuples

def tupleFilter(tuples):
    tuples = [i for i in tuples if len(i[1]) > 3]
    tuples.sort(key=lambda tup: tup[2], reverse = True)
    tuples = tuples[0:300]
    return tuples
        

def main():
    filteredTuples = []
    csvWrite = open("commonwords.csv","w+")
    #put path here
    directory = "C:/Users/ryanp/Desktop/Duke/Fall 2018/CS 316- Databases/Final Project/LingusticDB-database/books/books"
    for filename in findFiles(directory, "[0-9]*.txt"):
        filenamePartition = filename.rsplit("\\") #change for Linux I think
        bookId = filenamePartition[-1][:-4]
        print(bookId)
        f = open(filename,"rt",encoding = "ISO-8859-1")
        createWords = createWordCounts(f)
        createTuples = generateTuples(createWords, bookId)
        filteredTuples = tupleFilter(createTuples)
        for tup in filteredTuples:
            csvWrite.write(tup[0] + "|" + tup[1] + "|" + str(tup[2]) + "\n")
    csvWrite.close()     
    
main()