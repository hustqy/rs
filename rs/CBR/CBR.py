#This model implements the content based recomendation 
#It expects the input of a list of news objects. each news has userId, time, tag[],etc..
class CBR:
    def __init__(self):
        pass
        self.user_vector = dict()
    #user a list of news to build user profile
    def __init__(self, news):
        self.news = news
        self.user_vector = dict()# userid:set of items
    
    #build a dict in such a form: key = userid, value = [item1, item2, item3]
    def build_user_vector(self,build_vector = []):
        print 'start building user vector .........'
        assert(len(self.news) != 0)
           #we traverse the news list to build user vectors. one user per vector
        count_line = 0
        count_continue =0
        for line in self.news:
            count_line += 1
            id = line.get_userid()
            if not id in build_vector:
                count_continue += 1
                #print id, build_vector
                continue
            tags = line.get_tags()#that is the vector for each news
            #assert(len(tags)>=1)
            if (len(tags)!= 5):
                continue
            if id in self.user_vector:
                for item in tags:
                    self.user_vector[id].append(item)
            else:
                self.user_vector[id] = list()
                for item in tags:
                    self.user_vector[id].append(item)
        assert(count_line < 100000)
        print 'count_continue: ',count_continue
        self.transform_user_vector()

    #transform the uservector so the it has such form: key = userid, value={items1:count,item2:count....}
    def transform_user_vector(self):
        print 'start transforming user vector........'
        assert(len(self.user_vector)!=0)
        for key,value in self.user_vector.items():
            temp = dict()
            for item in value:
                if item in temp:
                    temp[item]+=1
                else:
                    temp[item] = 1
            self.user_vector[key] = temp

    def print_user_vector(self):
        for i, j in self.user_vector.items():
            print 'key: ',i,'value: ',j

    def print_user_vector_len(self):
        for i,j in self.user_vector.items():
            print 'key: ',i,'value len: ',len(j)

    def compare_user_item_similarity_one(self,user_id,item_vector):
        len_user = -1
        len_item = len(item_vector)
        sim = 0
        if user_id in self.user_vector:
            user_set = self.user_vector[user_id]
            len_user = len(user_set)
            for item in item_vector:
                if item in user_set:
                    sim += 1
        else:
            print 'unknow user.....'
            return -1,-1,-1
        return len_user,len_item,sim

    #compare the similarity based on the transformed data
    def compare_user_item_similarity_two(self,user_id,item_vector):
        len_user = -1
        len_item = len(item_vector)
        assert(len_item >= 3)
        sim = 0
        if user_id in self.user_vector:
            user_dict = self.user_vector[user_id]
            len_user = len(user_dict)
            for item in item_vector:
                if item in user_dict:
                    sim += user_dict[item]
        else:
            print 'unknown user'
        return len_user,len_item,sim

    def get_recommendation_list(self,user_id,in_list):
        news_rate = dict()
        for news_item in in_list:
            nid = news_item.get_newsid()
            ntag = news_item.get_tags()
            a,b,c = self.compare_user_item_similarity_two(user_id,ntag)
            if nid in news_rate:
                pass
            else:
                news_rate[nid] = c
        news_list = []
        for key,value in news_rate.items():
            news_list.append((key,value))
        news_list.sort(key = lambda x:x[1],reverse = True)
        return news_list[1:10]

