import os
import re
import glob

#  python -c 'import bookwordaggregates_loader; bookwordaggregates_loader.populate()' > bookword.csv

def getBook(file):
	return open(file, "r").read()

def numWords(file):
	return len(file.split())

def numSentences(file):
	return len(file.split('[.!?]'))

def wps(file):
	return numWords(file)/numSentences(file)

def wordLength(file):
	words = file.split()
	return sum(len(word) for word in words) / len(words)

def populate():
	headerSize = 1305

	# for file in glob.glob("/home/books/[0-9]*.txt"):
	for file in glob.glob("/home/books/4*.txt"):
		curr = getBook(file)
		print "%s|%d|%d|%d" %(file.split("/")[3].split(".")[0], wps(curr), \
			numWords(curr) - headerSize, wordLength(curr))