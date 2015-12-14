

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

