import nltk
def createPartSpeechTags(corpus,dictMeters):
    dictPartSpeechTags = {}
    for word in corpus:
        if(word not in dictMeters):
            continue
        token = nltk.word_tokenize(word)
        tag = nltk.pos_tag(token)
        dictPartSpeechTags[word] = tag[0][1]
    return dictPartSpeechTags
pos_list = ["CC","CD","DT","EX","FW","IN","JJ","JJR","JJS", "LS","MD","NN","NNS","NNP","NNPS", \
                "PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","TO","UH","VB","VBD","VBG","VBN","VBP", \
                "VBZ","WDT","WP","WP$","WRB"]
