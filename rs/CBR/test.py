# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('./..')

from docs import Documents
from CBR import CBR

def show_news_create_time():
    global x
    local_news = x.get_all_info()
    for line in local_news:
        print line.get_create_time()

def test_encoding():
    s='2014年03月08日12:31'
    print s.split('年')
    

'''
for i in range(10):    
    print 'parse: ',x.get_all_info()[i].get_userid()
    print 'parse: ',x.get_all_info()[i].get_newsid()
    print 'parse: ',x.get_all_info()[i].get_title()
    print 'parse: ',x.get_all_info()[i].get_tags()

'''
def test_cbr():
    mydoc = Documents('user_click_data.txt',True)
    news = mydoc.get_AllNews()
    cbr = CBR(news)
    cbr.build_user_vector()
    cbr.transform_user_vector()
    cbr.compare_user_item_similarity_two(5218791,news[1].get_tags())

def test_sort():
    show_news_create_time()
    global x
    local_news = x.get_all_info()
    news = Documents.sort_news_by_time(local_news);
    print '____________________________________________________'
    for i in news:
        print i.get_create_time()#do not new.get here

test_cbr()


