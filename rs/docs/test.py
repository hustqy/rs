from doc import Documents
x = open('./user_click_data.txt','r')
for i in range(5):
    pass
#    print len(x.readline().strip().split())
x.close()
x = Documents('./user_click_data.txt');

x.parse()
print 'parse: ',x.get_all_info()[0].get_userid()
