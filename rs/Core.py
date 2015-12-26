
from docs import Documents

from usermodel import UserModel

from itemmodel import ItemModel
class Core:

    def __init__(self,args):

        self.path = args.filename
        self.type = args.method
        self.user = args.userid


    def recommend(self):

        if self.type == 0:
            news = Documents(self.path, is_tfidf=False)
            m = news.get_user_item_matrix()
            UserModel(m)
            self.print_matrix(m)
        if self.type == 1:
            pass
        if self.type == 2:
            news = Documents(self.path, is_tfidf=False, type=2)
            svd_matrix = news.get_svd_matrix()
            new_userid = news.user_dict[int(self.user)]
            item_obj = ItemModel(svd_matrix,new_userid)
            res = item_obj.svdEst(svd_matrix,new_userid,item_obj.pearsSim)

            item_dict = news.item_dict
            news_ids = [(v, k) for k, v in item_dict.items()]
            news_ids.sort()
            news_ids = dict(news_ids)

            res_sorted = sorted(res.items(),key = lambda k:k[1],reverse=True)[0:20]
            print "user %d top 20 ratings at following News :" % (int(self.user))
            for (item,val) in res_sorted:
                print "News %d rating is %f" %(news_ids[item],val)

    def print_matrix(self,m):

        for (user,item) in m.items():
            print user
            print item.keys()