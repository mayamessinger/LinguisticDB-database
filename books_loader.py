import os
import re
import glob
import xml.etree.ElementTree as ET

#  python -c 'import books_loader; books_loader.populate()' > books.csv

def getBook(file):
	return open(file, "r").read()

def getTitle(file):
	file = file.split("/")[3].split(".")[0]
	tree = ET.parse("/home/repo/cache/epub/" + file + "/pg" + file + ".rdf")
	namespaces = {"dcterms": "http://purl.org/dc/terms/",
					"pgterms": "http://www.gutenberg.org/2009/pgterms/",
					"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}

	return tree.getroot().find("pgterms:ebook/dcterms:title", namespaces).text.encode("utf-8")

def getPublished(file):
	file = file.split("/")[3].split(".")[0]
	tree = ET.parse("/home/repo/cache/epub/" + file + "/pg" + file + ".rdf")
	namespaces = {"dcterms": "http://purl.org/dc/terms/",
					"pgterms": "http://www.gutenberg.org/2009/pgterms/",
					"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}

	return tree.getroot().find("pgterms:ebook/dcterms:issued", namespaces).text.encode("utf-8")

def getLink(file):
	file = file.split("/")[3].split(".")[0]
	return "http://www.gutenberg.org/files/" + file + "/" + file + ".txt"

def populate():
	headerSize = 1305

	# for file in glob.glob("/home/books/[0-9]*.txt"):
	for file in glob.glob("/home/books/4*.txt"):
		curr = getBook(file)
		print "%s|%s|%s|%s" %(file.split("/")[3].split(".")[0], getTitle(file), \
		getPublished(file), getLink(file))