import nltk
def dot(dict1,dict2):
        ret = 0
        if(len(dict1)<=len(dict2)):
            for key in dict1.keys():
                if(key in dict2):
                    ret += dict1[key]["tfidf"]*dict2[key]["tfidf"]
        else:
            for key in dict2.keys():
                if(key in dict1):
                    ret += dict1[key]["tfidf"]*dict2[key]["tfidf"]
        return ret
set_words = set([])
#for file in directory:
for file in ["gulliver.txt"]:
    #create text's dictionaries
    dictWords = {} #words to occurences
    #read in file
    f = open(file, 'rt', encoding = "UTF-8")
    text = f.readlines() #list of all lines
    #get rid of beginning header (for now! it has meaning in future!)
    begin = 0
    indic = True
    while (begin < len(text) and indic):
        line = text[begin]
        begin += 1
        if(len(line)>8):
            if(line[0:8] == "***START"):
                indic = False
    book = text[begin:]
    #get all words in text
    stopTags = set(["CC","CD","DT","IN", "LS", "MD", "PDT", "POS", "PRP$", "TO","EX","UH"])
    #SHOULD GET RID OF STOPWORDS.NLTK FOR OVERALL STATS
    stopWords = set(nltk.corpus.stopwords.words("english")).union(set(["-","’","‘", "_",";","(",")","<",">",",","''","``","”",'“',".","?",":","%",", "," ","n","=",",  ","#","$","@","{","}","[","]"]))
    for line in text:
        tokens = nltk.word_tokenize(line)
        #SHOULD PROBABLY STEM HERE, FOR MOST DOCUMENT COMPARISON
        #CAN ELIMINATE TOO COMMON WORDS: lines = [word[0].lower() for word in nltk.pos_tag(tokens) if word[1] not in stopTags and word[0] not in stopWords]
        refined = [word[0].lower() for word in nltk.pos_tag(tokens) if word[0] not in stopWords]
        for word in refined:
            if(word not in dictWords):
                dictWords[word] = [1,0] #first is tf, second is tf*idf
            else:
                dictWords[word][0] +=1
            set_words.add(word)
for item in sorted(dictWords.items(),key = lambda ite: ite[1][0]):
    print(item)
    #put dictWords into a library by title
#create IDF
# dictIDF = {}
# for word in list(set_words):
#     for book in library:
#     if(word in text)



    #while ind < len(text):
        #need to get rid of

    #parse to the beginning of the book, recording author + date + etc

# def initial_process_files(directory):
#     for file in directory:
#         create
