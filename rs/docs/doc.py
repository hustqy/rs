# -*- coding: utf-8 -*-
from news import News
from tfidf import Tfidf
import codecs
import utility
class Documents:
    def __init__(self, path,is_tfidf=False):
        self.path = path
        self.isTfidf = is_tfidf
        self.AllNews = []

    def parse(self):
        all_content = []
        with codecs.open(self.path,'r','utf-8-sig') as lines:
            for lin in lines:
                create_time = utility.split_data_by_date(lin)
                lin = lin.strip().split()    
                userid,newsid,scan_time,title,create_time_ = lin[0],lin[1],lin[2],lin[3],lin[-1]
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
    @staticmethod
    def sort_news_by_time(in_news_list):
        assert(len(in_news_list) >= 1)
        return sorted(in_news_list,cmp = Documents.f)
    @staticmethod    
    def f(in_news1,in_news2):
        t1 = in_news1.get_create_time()
        t2 = in_news2.get_create_time()
        assert(len(t1) == len(t2))
        assert(len(t1[3]) == len(t2[3]))
        if t1[0] > t2[0]:
            return 1
        elif t1[0] < t2[0]:
            return -1
        else:#in the same year
            if t1[1] > t2[1]:
                return 1
            elif t1[1] < t2[1]:
                return -1
            else:#in the same month
                if t1[2] > t2[2]:
                    return 1
                elif t1[2] < t2[2]:
                    return -1
                else:#in the same day
                    if t1[3][0] > t2[3][0]:
                        return 1
                    elif t1[3][0] < t2[3][0]:
                        return -1
                    else:#in the same hour
                        if t1[3][1] > t2[3][1]:
                            return 1
                        elif t1[3][1] < t2[3][1]:
                            return -1
                        else:
                            return 0



        





