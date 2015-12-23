
from docs import Documents

from usermodel import UserModel

class Core:

    def __init__(self,args):

        self.path = args.filename
        self.type = args.method
        self.user = args.userid



    def recommend(self):
        news = Documents(self.path, is_tfidf=False)
        news.parse()
        m = news.get_user_item_matrix()

        if self.type == 0:
            UserModel(m)
            self.print_matrix(m)
        if self.type == 1:
            pass
        if self.type == 2:
            pass

    def print_matrix(self,m):

        for (user,item) in m.items():
            print user
            print item.keys()