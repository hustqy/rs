
from news import News
from tfidf import Tfidf

import codecs
class Documents:

    def __init__(self, path):
        self.path = path
        self.AllNews = []


    def parse(self):

        all_content = []
        with codecs.open(self.path,'r') as lines:

            for lin in lines:
                lin = lin.split()

                userid,newsid,scan_time,title,create_time = lin[0],lin[1],lin[2],lin[3],lin[-1]


                news = News(int(userid), newsid, title, scan_time, [], create_time)

                self.AllNews.append(news)

                content = "".join(lin[4:-1])

                all_content.append(content)

        tags = Tfidf(all_content).derive_keyword_zh(keyword_num=5)

        for index in xrange(len(tags)):
            self.AllNews[index].tags = tags[index]

        return self.AllNews






