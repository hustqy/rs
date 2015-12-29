from numpy import *
from docs import Documents
from numpy import linalg as la
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

            news = Documents(self.train_path, is_tfidf=False, type=2)
            user_item_m = news.get_user_item_matrix()
            item_news_m = news.get_item_user_m()           #item_news_m[newsid] represents users who saw newsid

            test = Documents(self.test_path, is_tfidf=False, type=2)
            test_user_item = test.get_user_item_matrix()
            recom_items = test.get_items()

            users = self.get_sample_users(user_item_m,100)
            for i_user in users:
                if i_user not in test_user_item:
                    continue
                test_user_seen = test_user_item[i_user].keys()
                user_seen = user_item_m[i_user].keys()      #items that specified user has seen

                results = {}
                for it in recom_items:
                    if it in user_seen:
                        user_seen.remove(it)
                    rating = 0
                    for seen in user_seen:
                        similarity = self.sim(item_news_m[it],item_news_m[seen])
                        rating += user_item_m[i_user][seen] * similarity
                    results[it] = rating
                    # print "item %d rating is %f" % (it, rating)
                res = sorted(results.items(),key = lambda k:k[1],reverse=True)[0:10]
                predict_seen = [it[0] for it in res]
                # print "predict user %d will see " %i_user, predict_seen

                # for (key,val) in res:
                #     print "item %d rating is %f" % (key, val)
                acc,hit_items = self.cal_accuracy(test_user_seen,predict_seen)
                # print "mark user %d see news in test " %i_user , test_user_seen
                # print "prediction accuracy is %f" % acc
                # print "hit news are", hit_items
                print "%d %f "% (i_user,acc),hit_items

    def get_sample_users(self,user_item_m, num):
        res = []
        count = 0
        for (user,items) in user_item_m.items():
            if len(items) > 8:
                res.append(user)
                count +=1
            if count >= num:
                break
        return res

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
        return 0.5*num

    @staticmethod
    def cal_accuracy(mark,prediction):
        count = 0
        res=[]
        for i in prediction:
            if i in mark:
                count +=1
                res.append(i)
        return 1.0*count/len(mark),res