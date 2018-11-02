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
