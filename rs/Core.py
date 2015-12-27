from numpy import *
from docs import Documents

from usermodel import UserModel

from itemmodel import ItemModel
class Core:

    def __init__(self,args):

        self.train_path = args.trainfile
        self.test_path = args.testfile
        self.type = args.method
        self.user = args.userid

    def recommend(self):

        if self.type == 0:
            news = Documents(self.train_path, is_tfidf=False)
            m = news.get_user_item_matrix()
            UserModel(m)
            self.print_matrix(m)
        if self.type == 1:
            pass
        if self.type == 2:
            results = {}
            news = Documents(self.train_path, is_tfidf=False, type=2)
            user_item_m = news.get_user_item_matrix()
            user_seen = user_item_m[self.user].keys()      #items that specified user has seen
            item_news_m = news.get_item_user_m()           #item_news_m[newsid] represents users who saw newsid

            test = Documents(self.test_path, is_tfidf=False, type=2)
            recom_items = test.get_items()

            for it in recom_items:
                if it in user_seen:
                    user_seen.remove(it)
                rating = 0
                for seen in user_seen:
                    similarity = self.sim(item_news_m[it],item_news_m[seen])
                    rating += user_item_m[self.user][seen] * similarity
                results[it] = rating
                # print "item %d rating is %f" % (it, rating)
            res = sorted(results.items(),key = lambda k:k[1],reverse=True)[0:20]
            for (key,val) in res:
                print "item %d rating is %f" % (key, val)

    def print_matrix(self,m):

        for (key,val) in m.items():
            print key
            print val.keys()

    def sim(self,inA,inB):
        users1 = inA.keys()
        users2 =  inB.keys()
        users = list(set(users1+users2))
        array1 = [0] * len(users)
        array2 = [0] * len(users)
        for i in xrange(len(users)) :
            if users[i] in users1:
                array1[i] = 1
        for i in xrange(len(users)) :
            if users[i] in users2:
                array2[i] = 1
        return self.cosSim(mat(array1), mat(array2))

    @staticmethod
    def cosSim(inA,inB):
        num =inA*inB.T
        # denom = la.norm(inA)*la.norm(inB)
        return 0.5+0.5*num

