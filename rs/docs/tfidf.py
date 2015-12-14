import math
import jieba
import jieba.posseg
import jieba.analyse

from textblob import TextBlob as tb

class Tfidf:

    def __init__(self,news):

        self.news = news


    def derive_keyword_zh(self,keyword_num= 3):
        tags = []
        for s in self.news:

            item = jieba.analyse.extract_tags(s, topK=keyword_num, withWeight=False)

            tags.append(item)
        return tags

    def derive_keyword_english(self,keyword_num = 3):

        bloblist = []

        for doc in self.news:
            tb_words = tb(doc)
            bloblist.append(tb_words)

        for i, blob in enumerate(bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: self.tfidf(word, blob, bloblist) for word in blob.words}

            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[:keyword_num]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


    def tf(self,word, blob):
        return blob.words.count(word) / len(blob.words)

    def n_containing(self,word, bloblist):
        return sum(1 for blob in bloblist if word in blob)

    def idf(self,word, bloblist):
        return math.log(len(bloblist) / (1 + self.n_containing(word, bloblist)))

    def tfidf(self,word, blob, bloblist):
        return self.tf(word, blob) * self.idf(word, bloblist)



