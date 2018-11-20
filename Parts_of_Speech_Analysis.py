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
#definitions of pos codes: https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
dictPOS = {}
dictTagSequences = {}
prev_tag = 0
for line in book:
    line = line.split(" ")
    tokens = []
    for word in line:
        word = word.lower()
        token = nltk.word_tokenize(word)
        tag = nltk.pos_tag(token)
        if(tag not in dictPOS):
            dictPOS[tag] = 0
        dictPOS[tag] += 1
        if(prev_tag):
            if(tag not in dictTagSequences):
                dictTagSequences[tag] = {}
                dictTagSequences[tag]["prev"] = {}
                dictTagSequences[tag]["post"] = {}
            dictTagSequences[tag]["prev"][prev_tag] +=1
            dictTagSequences[prev_tag]["post"][tag] +=1
        prev_tag = tag
