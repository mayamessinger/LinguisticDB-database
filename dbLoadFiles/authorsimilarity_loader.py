import os
import re
import glob
import xml.etree.ElementTree as ET
import nltk
import math
import time
import os
# import queue
import csv
#  python -c 'import authorsimilarity_loader; authorsimilarity_loader.populate()'> authorsimilarity.csv
#AUTHORSIMILARITY WAS MODIFIED TO USE COSINESIMILARITY OF BOOKS!!!
def populate():
    dictAuth = {}
    dictBooks = {}
    with open('writes.csv', 'rb') as csvfile:
        writesreader = csv.reader(csvfile, delimiter='|')
        for row in writesreader:
            if(row[0] not in dictBooks):
                dictBooks[row[0]] = row[1] #stores author
            if(row[1] not in dictAuth):
                dictAuth[row[1]] = {} #readies comparisons
    with open('cosinesimilarity.csv', 'rb') as csvfile:
        writesreader = csv.reader(csvfile, delimiter='|')
        for row in writesreader:
            if(row[0]==row[1]):
                continue
            auth1 = dictBooks[row[0]]
            auth2 = dictBooks[row[1]]
            sim = row[2]
            #calc for auth1
            if(auth2 not in dictAuth[auth1]):
                dictAuth[auth1][auth2] = [0,0]
            x = dictAuth[auth1][auth2]
            dictAuth[auth1][auth2][1] += 1
            dictAuth[auth1][auth2][0] = (sim + dictAuth[auth1][auth2][0]*x)/(x+1)
            #calc for auth2
            if(auth1 not in dictAuth[auth2]):
                dictAuth[auth2][auth1] = [0,0]
            x = dictAuth[auth2][auth1]
            dictAuth[auth2][auth1][1] += 1
            dictAuth[auth2][auth1][0] = (sim + dictAuth[auth2][auth1][0]*x)/(x+1)
    for auth1 in dictAuth:
        for auth2 in dictAuth[auth1]:
            tup = (auth1,auth2,dictAuth[auth1][auth2][0],0)
            print("%s|%s|%f|%i"%(tup[0],tup[1],tup[2],tup[3]))


#
# def getAuthor(file):
#     # file = file.split("/")[3].split(".")[0]
#     tree = ET.parse("/home/database/cache/epub/" + file + "/pg" + file + ".rdf")
#     namespaces = {"dcterms": "http://purl.org/dc/terms/",
#     "pgterms": "http://www.gutenberg.org/2009/pgterms/",
#     "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}
#
#     if (tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:name", namespaces) is None):
#         return "unknown"
#     else:
#         return tree.getroot().find("pgterms:ebook/dcterms:creator/pgterms:agent/pgterms:name", namespaces).text.encode("utf-8")
# def dot(dict1,dict2):
#     ret = 0
#     if(len(dict1)<=len(dict2)):
#         for key in dict1.keys():
#             if(key in dict2):
#                 ret += dict1[key][1]*dict2[key][1]
#     else:
#         for key in dict2.keys():
#             if(key in dict1):
#                 ret += dict1[key][1]*dict2[key][1]
#     return ret
# def populate():
#     #orig_f_list = f_list.copy()
#     def addToCSV(f_lst):
#         dictDF = {}
#         books = {}
#         start = time.time()
#         dictTokens = {}
#         dictAuth = {}
#         for file in f_lst:
#             #create text's dictionaries
#             dictWords = {} #words to occurences
#             #read in file
#             #f = open(file, 'rt', encoding = "UTF-8")
#             f = open(file, 'rt', encoding = "ISO-8859-1")
#             text = f.readlines() #list of all lines
#             #get rid of beginning header (for now! it has meaning in future!)
#             begin = 0
#             indic = True
#             file1 = file.split("/")[3][:-4] #uid for the book
#             # file = file.split("/")[3].split(".")[0]
#
#             books[file1] = {}
#             while (begin < len(text) and indic):
#                 line = text[begin]
#                 begin += 1
#                 if(len(line)>=7):
#                     if(line[0:6]=="Title:"):
#                         sep = line.split(" ")
#                         sep[-1] = sep[-1][0:-1]
#                         title = tuple(sep[1:])
#                         books[file1]["title"] = title
#                     if(line[0:7]=="Author:"):
#                         author = getAuthor(file1)
#                         books[file1]["author"] = author
#                 if(len(line)>9):
#                     if(line[0:8] == "***START" or line[0:9] == "*** START"):
#                         indic = False
#             book = text[begin:]
#
#             #stopTags = set(["CC","CD","DT","IN", "LS", "MD", "PDT", "POS", "PRP$", "TO","EX","UH"])
#             #SHOULD GET RID OF STOPWORDS.NLTK FOR OVERALL STATS
#             #stopWords = set(nltk.corpus.stopwords.words("english"))
#             stopWords = set("bcdefghjklmnopqrstuvwxyzBCDEFGHJKLMNOPQRSTUVWXYZ").union(set(["'s","*","-","’","‘", "_",";","(",")","<",">",",","''","``","”",'“',".","?",":","%",", "," ","n","=",",  ","#","$","@","{","}","[","]"]))
#             for line in book:
#                 line = line.split(" ")
#                 tokens = []
#                 for word in line:
#                     word = word.lower()
#                     if(word not in dictTokens):
#                         tok = nltk.word_tokenize(word)
#                         dictTokens[word] = tok
#                         tokens += tok
#                     else:
#                         tokens += dictTokens[word]
#                 #refined = [word[0].lower() for word in nltk.pos_tag(tokens) if word[0] not in stopWords]
#                 refined = [word for word in tokens if word not in stopWords]
#                 for word in refined:
#                     if(word not in dictWords):
#                         dictWords[word] = [1,0] #first is tf, second is tf*idf
#                         if(word not in dictDF): #normalize all the counts
#                             dictDF[word] = 1
#                         else:
#                             dictDF[word] += 1
#                     else:
#                         dictWords[word][0] +=1
#             books[file1]["word_freq"] = dictWords
#             #build author data
#             if(author not in dictAuth):
#                 dictAuth[author] = {}
#                 dictAuth[author]["books"] = []
#                 dictAuth[author]["sim_vect"] = {}
#             dictAuth[author]["books"]+=[file1]
#         #put dictWords into a library by title
#         #create IDF
#         dictIDF = {}
#         for word in dictDF:
#             dictIDF[word] = math.log(len(books)/dictDF[word])+.000001
#         book_l = list(books.keys())
#         for book in book_l: #book is such a strange word...2 O's...
#             word_dict = books[book]["word_freq"]
#             for word in word_dict:
#                 word_dict[word][1] = word_dict[word][0]*dictIDF[word]
#             a = math.sqrt(dot(word_dict,word_dict))
#             books[book]["magnitude"] = a
#             if(a==0):
#                 books.pop(book)
#         #author similarity calculation
#         for author in dictAuth:
#             #incorporate each book into the author's vector
#             for book in dictAuth[author]["books"]:
#                 book_vector = books[book]["word_freq"]
#                 for word in book_vector:
#                     if(word not in dictAuth[author]["sim_vect"]):
#                         dictAuth[author]["sim_vect"][word] = book_vector[word]
#                     else:
#                         dictAuth[author]["sim_vect"][word][0] += book_vector[word][0]
#                         dictAuth[author]["sim_vect"][word][1] += book_vector[word][1]
#         for author in dictAuth:
#             vec = dictAuth[author]["sim_vect"]
#             dictAuth[author]["magnitude"] = math.sqrt(dot(vec,vec))
#         #show top most similar authors
#         authTopSim = []
#         ind = 0
#         auth_l = dictAuth.keys()
#         k = len(auth_l)
#         for y in range(80):
#             f_list = []
#             j = math.ceil(k*(y/80 + 1/80))
#             i = (k*y)//80
#             auth_comp = auth_l[i,j]
#             for auth1 in auth_comp:
#                 auth1_v = dictAuth[auth1]["sim_vect"]
#                 sim_list = []
#                 for auth2 in auth_comp:
#                     if(auth1==auth2):
#                         continue
#                     auth2_v  = dictAuth[auth2]["sim_vect"]
#                     sim = dot(auth1_v,auth2_v)/(dictAuth[auth1]["magnitude"]*dictAuth[auth2]["magnitude"])
#                     sim_list += [[auth1,auth2,sim]]
#                 sim_list = sorted(sim_list, key = lambda elem: elem[2], reverse=True)
#                 i=0
#                 while i < 500 and i < len(sim_list):
#                     authTopSim += [sim_list[i]+[i+1]]
#                     i+=1
#                 ind+=1
#             for tup in authTopSim:
#                 print("%s|%s|%f|%i"%(tup[0],tup[1],tup[2],tup[3]))
#     # done = set() #next optimization
#     f_list = []
#     for file in glob.glob("/home/books/[0-9]*.txt"):
#     # for file in glob.glob("/home/books/[0-9]*.txt"):
#         f_list+=[file]
#     addToCSV(f_list)
