
from news import News
from tfidf import Tfidf
import numpy

import codecs
class Documents:

    def __init__(self, path,is_tfidf=False,is_svd=False):
        self.path = path
        self.isTfidf = is_tfidf
        self.isSvd = is_svd
        self.AllNews = []
        self.user_dict = {}
        self.item_dict = {}
        self.parse()



    def parse(self):

        all_content = []

        with codecs.open(self.path,'r','utf-8-sig') as lines:

            for lin in lines:
                lin = lin.strip().split()

                userid,newsid,scan_time,title,create_time = int(lin[0]),int(lin[1]),lin[2],lin[3],lin[-1]

                news = News(userid, newsid, title, scan_time, [], create_time)

                self.AllNews.append(news)


                #fill user_dict and item_dict
                if self.isSvd:
                    if userid not in self.user_dict:
                        self.user_dict[userid] = len(self.user_dict)

                    if newsid not in self.item_dict:
                        self.item_dict[newsid] = len(self.item_dict)

                content = "".join(lin[4:-1])

                all_content.append(content)

        if self.isTfidf:
            tags = Tfidf(all_content).derive_keyword_zh(keyword_num=5)

            for index in xrange(len(tags)):
                self.AllNews[index].tags = tags[index]



    def get_user_item_matrix(self):
        m = dict()
        for item in self.AllNews:
            userid = item.userid
            newsid = item.newsid
            if m.has_key(userid):   # {userid : {newsid: num, newsid2:num2 }}
                if m[userid].has_key(newsid):
                    m[userid][newsid] += 1
                else:
                    m[userid][newsid] = 1
            else:
                m[userid] = {newsid: 1}
        return m

    def get_all_info(self):
        return self.AllNews

    def get_svd_matrix(self):
        m = numpy.zeros( (len(self.user_dict) , len(self.item_dict)))

        for it in self.AllNews:
            x= self.user_dict[it.userid]
            y= self.item_dict[it.newsid]
            m[x][y] += 1

        return m







