import nltk
import math
import time
import os
def dot(dict1,dict2):
        ret = 0
        if(len(dict1)<=len(dict2)):
            for key in dict1.keys():
                if(key in dict2):
                    ret += dict1[key][1]*dict2[key][1]
        else:
            for key in dict2.keys():
                if(key in dict1):
                    ret += dict1[key][1]*dict2[key][1]
        return ret
import os
f_list = []
for file in os.listdir("./"):
    if file.endswith(".txt"):
        f_list+=[file]
#for file in directory:
dictDF = {}
books = {}
start = time.time()
dictTokens = {}
dictAuth = {}
for file in f_list:
    #create text's dictionaries
    dictWords = {} #words to occurences
    #read in file
    f = open(file, 'rt', encoding = "UTF-8")
    text = f.readlines() #list of all lines
    #get rid of beginning header (for now! it has meaning in future!)
    begin = 0
    indic = True
    file = file[:-4]
    books[file] = {}
    while (begin < len(text) and indic):
        line = text[begin]
        begin += 1
        if(len(line)>=7):
            if(line[0:6]=="Title:"):
                sep = line.split(" ")
                sep[-1] = sep[-1][0:-1]
                title = tuple(sep[1:])
                books[file]["title"] = title
            if(line[0:7]=="Author:"):
                sep = line.split(" ")
                sep[-1] = sep[-1][0:-1]
                author = tuple(sep[1:])
                books[file]["author"] = author
        if(len(line)>9):
            if(line[0:8] == "***START" or line[0:9] == "*** START"):
                indic = False
    book = text[begin:]

    #get all words in text
    #stopTags = set(["CC","CD","DT","IN", "LS", "MD", "PDT", "POS", "PRP$", "TO","EX","UH"])
    #SHOULD GET RID OF STOPWORDS.NLTK FOR OVERALL STATS
    #stopWords = set(nltk.corpus.stopwords.words("english"))
    stopWords = set("bcdefghjklmnopqrstuvwxyzBCDEFGHJKLMNOPQRSTUVWXYZ").union(set(["'s","*","-","’","‘", "_",";","(",")","<",">",",","''","``","”",'“',".","?",":","%",", "," ","n","=",",  ","#","$","@","{","}","[","]"]))
    for line in book:
        line = line.split(" ")
        tokens = []
        for word in line:
            word = word.lower()
            if(word not in dictTokens):
                tok = nltk.word_tokenize(word)
                dictTokens[word] = tok
                tokens += tok
            else:
                tokens += dictTokens[word]
        #SHOULD PROBABLY STEM HERE, FOR MOST DOCUMENT COMPARISON; COULD STEM FOR SIMILARITY BUT NOT FOR COMMON WORDS
        #CAN ELIMINATE TOO COMMON WORDS: lines = [word[0].lower() for word in nltk.pos_tag(tokens) if word[1] not in stopTags and word[0] not in stopWords]
        #refined = [word[0].lower() for word in nltk.pos_tag(tokens) if word[0] not in stopWords]
        refined = [word for word in tokens if word not in stopWords]
        for word in refined:
            if(word not in dictWords):
                dictWords[word] = [1,0] #first is tf, second is tf*idf
                if(word not in dictDF): #normalize all the counts
                    dictDF[word] = 1
                else:
                    dictDF[word] += 1
            else:
                dictWords[word][0] +=1
    books[file]["word_freq"] = dictWords
    #build author data
    if(author not in dictAuth):
        dictAuth[author] = {}
        dictAuth[author]["books"] = []
        dictAuth[author]["sim_vect"] = {}
    dictAuth[author]["books"]+=[file]
#put dictWords into a library by title
#create IDF
dictIDF = {}
for word in dictDF:
    dictIDF[word] = math.log(len(books)/dictDF[word])+.000001
for book in books.keys(): #book is such a strange word...2 O's...
    word_dict = books[book]["word_freq"]
    for word in word_dict:
        word_dict[word][1] = word_dict[word][0]*dictIDF[word]
    a = math.sqrt(dot(word_dict,word_dict))
    books[book]["magnitude"] = a
    if(a == 0):
        print("magnitude is 0!!!")
        print(book)
# dictSimilarities = {}
#book_list = list(books.keys())
#iter_books = book_list[0:(len(book_list)//2+1)]
bookTopSim = []
ind = 0
for book1 in books:
    w_d1 = books[book1]["word_freq"]
    sim_list = []
    for book2 in books:
        if(book1==book2):
            continue
        w_d2 = books[book2]["word_freq"]
        sim = dot(w_d1,w_d2)/(books[book1]["magnitude"]*books[book2]["magnitude"])
        sim_list += [[book1,book2,sim]]
    sim_list = sorted(sim_list, key = lambda elem: elem[2], reverse=True)
    i=0
    while i < 500 and i < len(sim_list):
        bookTopSim += [sim_list[i]+[i+1]]
        i+=1
    ind+=1
#author similarity calculation
for author in dictAuth:
    #incorporate each book into the author's vector
    for book in dictAuth[author]["books"]:
        book_vector = books[book]["word_freq"]
        for word in book_vector:
            if(word not in dictAuth[author]["sim_vect"]):
                dictAuth[author]["sim_vect"][word] = book_vector[word]
            else:
                dictAuth[author]["sim_vect"][word][0] += book_vector[word][0]
                dictAuth[author]["sim_vect"][word][1] += book_vector[word][1]
for author in dictAuth:
    vec = dictAuth[author]["sim_vect"]
    dictAuth[author]["magnitude"] = math.sqrt(dot(vec,vec))
#show top most similar authors
authTopSim = []
ind = 0
for auth1 in dictAuth :
    auth1_v = dictAuth[auth1]["sim_vect"]
    sim_list = []
    for auth2 in dictAuth:
        if(auth1==auth2):
            continue
        auth2_v  = dictAuth[auth2]["sim_vect"]
        sim = dot(auth1_v,auth2_v)/(dictAuth[auth1]["magnitude"]*dictAuth[auth2]["magnitude"])
        sim_list += [[auth1,auth2,sim]]
    sim_list = sorted(sim_list, key = lambda elem: elem[2], reverse=True)
    i=0
    while i < 500 and i < len(sim_list):
        authTopSim += [sim_list[i]+[i+1]]
        i+=1
    ind+=1



print(time.time()-start)
print(bookTopSim[0:10])
print(authTopSim[0:10])


#Common Words
from operator import itemgetter
for book in books:
    words = list(books[book]["word_freq"].items())
    lst = sorted(words,key=lambda elem: elem[1][1], reverse=True)
    words = list(books[book]["word_freq"].items())
    lst1 = sorted(words,key=lambda elem: elem[1][0], reverse=True)
    # print(books[book]["title"])
    # print("highest tfidf: %s"%lst[0:10])
    # print("highest frequencies: %s"%lst1[0:10])
# def initial_process_files(directory):
#     for file in directory:
#         create
