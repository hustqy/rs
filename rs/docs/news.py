'''
    in the original data provided, each line has six features:
    userid, newsid, scan_time, title,tags=[](content),create_time. We build this class to store one line of infomation
'''
class News:

    def __init__(self,userid, newsid, scan_time, title, tags=[], create_time=None):
        self.userid = int(userid)
        self.newsid = newsid
        self.title = title
        self.tags = tags
        self.scan_time = scan_time
        self.create_time = create_time

    def get_tags(self):
        return self.tags
    def get_scan_time(self):
        return self.scan_time
    def get_userid(self):
        return self.userid
    def get_newsid(self):
        return self.newsid
    def get_title(self):
        return self.title
    def get_create_time(self):
        return self.create_time
