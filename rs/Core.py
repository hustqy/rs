
from docs import Documents

from usermodel import UserModel

class Core:

    def __init__(self,args):

        self.path = args.filename
        self.type = args.method
        self.user = args.userid



    def recommend(self):
        news = Documents(self.path)
        matrix = news.parse()

        for item in matrix:
            if item.userid == self.user:
                print item.tags

        if self.type == 0:
            pass
        if self.type == 1:
            pass
        if self.type == 2:
            pass
