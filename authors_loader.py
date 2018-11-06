import os
import re
import glob
import xml.etree.ElementTree as ET

#  python -c 'import authors_loader; authors_loader.populate()'> authors.csv

def getAuthor(file):
	file = file.split("/")[3].split(".")[0]
	tree = ET.parse("/home/repo/cache/epub/" + file + "/pg" + file + ".rdf")
	namespaces = {"dcterms": "http://purl.org/dc/terms/",
					"pgterms": "http://www.gutenberg.org/2009/pgterms/",
					"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}

	if (tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:name", namespaces) is None):
		return "unknown"
	else:
		return tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:name", namespaces).text.encode("utf-8")

def getBirthdate(file):
	file = file.split("/")[3].split(".")[0]
	tree = ET.parse("/home/repo/cache/epub/" + file + "/pg" + file + ".rdf")
	namespaces = {"dcterms": "http://purl.org/dc/terms/",
					"pgterms": "http://www.gutenberg.org/2009/pgterms/",
					"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}

	if (tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:birthdate", namespaces) is None):
		return "NULL"
	else:
		return tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:birthdate", namespaces).text.encode("utf-8")

def populate():
	# for file in glob.glob("/home/books/[0-9]*.txt"):
	for file in glob.glob("/home/books/4*.txt"):
		print "%s|%s" %(getAuthor(file), getBirthdate(file))