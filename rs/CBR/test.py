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

def test_cbr(target_reader_list = []):
    input_target_len = len(target_reader_list)
    #use training data to build user vector
    testing = Documents('user_click_data.txt',True)
    test_news = testing.get_AllNews()
    user_read_dict = dict()
    target_reader = []
    #you can specify the target_reader number here!!!!
    target_num = 5
    if input_target_len != 0:
        target_num = input_target_len
    get = 0
    while len(target_reader)<(target_num):
        utemp = test_news[get].get_userid()
        get += 1
        if not utemp in target_reader:
            target_reader.append(utemp)

    if input_target_len != 0:
        target_reader = target_reader_list
    training = Documents('user_click_data.txt',True)
    train_news = training.get_AllNews()
    cbr = CBR(train_news)
    cbr.build_user_vector(target_reader)
    cbr.transform_user_vector()

    for i in test_news:
        uid = i.get_userid()
        nid = i.get_newsid()
        if uid in target_reader:
            pass
        else:
            #print uid
            target_reader.append(uid)

        if uid in user_read_dict:
            user_read_dict[uid].append(nid)
        else:
            user_read_dict[uid] = []
            user_read_dict[uid].append(nid)

    #if you want to specify the target_readerlist, you can uncomment the folllwing line
    #target_reader = target_reader_list
    #print target_reader
    for i in range(target_num):
        recommend = cbr.get_recommendation_list(target_reader[i],test_news)
        #print 'recommend: ',recommend
        #print 'real: ',user_read_dict[target_reader[i]]
        temp = []
        for item in recommend:
            temp.append(item[0])
        
        count_read = 0
        count = 0
        for t in user_read_dict[target_reader[i]]:
            count_read += 1
            if t in temp:
                count += 1
        print 'reader ',target_reader[i],'  read:',len(user_read_dict[target_reader[i]]),'  accept: ',count
        

def test_sort():
    show_news_create_time()
    global x
    local_news = x.get_all_info()
    news = Documents.sort_news_by_time(local_news);
    print '____________________________________________________'
    for i in news:
        print i.get_create_time()#do not new.get here

test_cbr([5218791,52550])


