#This model implements the content based recomendation 
#It expects the input of a list of news objects. each news has userId, time, tag[],etc..
class CBR:
    def __init__(self):
        pass
        self.user_vector = dict()
    def __init__(self, news):
        self.news = news
        self.user_vector = dict()# userid:set of items
    
    #build a dict in such a form: key = userid, value = [item1, item2, item3]
    def build_user_vector(self):
        assert(len(self.news) != 0)
           #we traverse the news list to build user vectors. one user per vector
        for line in self.news:
            id = line.get_userid()
            tags = line.get_tags()#that is the vector for each news
            assert(len(tags)>=1)
            if id in self.user_vector:
                for item in tags:
                    self.user_vector[id].append(item)
            else:
                self.user_vector[id] = list()
                for item in tags:
                    self.user_vector[id].append(item)
        self.transform_user_vector()

    #transform the uservector so the it has such form: key = userid, value={items1:count,item2:count....}
    def transform_user_vector(self):
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

    def compare_user_item_similarity(self,user_id,item_vector):
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
