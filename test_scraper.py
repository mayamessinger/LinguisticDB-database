import os
import re
import glob
import xml.etree.ElementTree as ET

def getBook(file):
	return open(file, "r").read()

def getTitle(file):
	file = file.split("/")[3].split(".")[0]
	tree = ET.parse("/home/maya.messinger/database/cache/epub/" + file + "/pg" + file + ".rdf")
	namespaces = {"dcterms": "http://purl.org/dc/terms/",
					"pgterms": "http://www.gutenberg.org/2009/pgterms/",
					"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}

	return tree.getroot().find("pgterms:ebook/dcterms:title", namespaces).text.encode("utf-8")

def getAuthor(file):
	file = file.split("/")[3].split(".")[0]
	tree = ET.parse("/home/maya.messinger/database/cache/epub/" + file + "/pg" + file + ".rdf")
	namespaces = {"dcterms": "http://purl.org/dc/terms/",
					"pgterms": "http://www.gutenberg.org/2009/pgterms/",
					"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}

	if (tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:name", namespaces) is None):
		return "unknown"
	else:
		return tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:name", namespaces).text.encode("utf-8")

def numWords(file):
	return len(file.split())

def numSentences(file):
	return len(file.split('.'))

def numLines(file):
	return len(file.splitlines())

def wps(file):
	return numWords(file)/numSentences(file)

def populate():
	headerSize = 1305

	# for file in glob.glob("/home/books/*.txt"):
	for file in glob.glob("/home/books/4*.txt"):
		curr = getBook(file)
		print "%s|%s|%s|%d|%d|%d|%d" %(file.split("/")[3].split(".")[0], getTitle(file), getAuthor(file), \
			numWords(curr) - headerSize, numLines(curr), numSentences(curr),wps(curr))