
from news import News
from tfidf import Tfidf

import codecs
class Documents:

    def __init__(self, path,is_tfidf=False):
        self.path = path
        self.isTfidf = is_tfidf
        self.AllNews = []


    def parse(self):

        all_content = []
        with codecs.open(self.path,'r','utf-8-sig') as lines:

            for lin in lines:
                lin = lin.strip().split()

                userid,newsid,scan_time,title,create_time = lin[0],lin[1],lin[2],lin[3],lin[-1]


                news = News(int(userid), int(newsid), title, scan_time, [], create_time)

                self.AllNews.append(news)

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







