# -*- coding: utf-8 -*-
#accept a line of news and return the time in the form of a tuple
import news

def split_data_by_date(line):
		temp = line.strip().split()
		temp = temp[-1]
#                print 'temp: ',temp
#                temp = '2014年03月08日12:31'
                assert(len(temp) > 5)
		year, temp = temp.split('年')
		month, temp = temp.split('月')
		temp = temp.split('日')
		if len(temp) > 1:
			day = temp[0]
			hour,min = temp[1].split(':')
			time = (int(hour),int(min))
		else:
			day = temp[0]
			time = (-1,-1)
	        return	(int(year),int(month),int(day),time)

#this function will generate two files, training.txt and testing.txt
#the input file should be user_click_data_sorted.txt
def generate_training_testing(infile):
    assert(infile == 'user_click_data_sorted.txt')
    z = open(infile,'r')
    threshhold = 5
    x = open('training.txt','a')
    y = open('testing.txt','a')
    user = dict()
    for line in z:
        u = line.strip().split()[0]
        if u in user:
            user[u] +=1
            if user[u] > 5:
                y.write(line)
            else:
                x.write(line)
        else:
            user[u] = 1
            x.write(line+'\n')

#an other version for generating training and testing data. with dynamic threshhold
def generate_training_testing_1(infile):
    assert(infile == 'user_click_data_sorted.txt')
    z = open(infile,'r')
    threshhold = 5
    x = open('training.txt','a')
    y = open('testing.txt','a')
    user = dict()
    for line in z:
        u = line.strip().split()[0]
        if u in user:
            user[u] +=1
        else:
            user[u] = 1
    z.close()
    z = open(infile,'r')
    user2 = dict()
    for i,j in user.items():
        user2[i] = 0
    for line in z:
        u = line.strip().split()[0]
        assert(u in user)
        dy_threshhold = user[u]*0.8
        user2[u] += 1
        if user2[u] > dy_threshhold and user2[u] > threshhold:
            y.write(line)
        else:
            x.write(line)

#this function is called by create_sorted_by_time_file(); the parameter infile is specified in create_sorted_by_time_file(),the default value should be 'user_click_data_final.txt'
def generate_sorted_data(infile):
    x = open(infile,'r')
    L = []
    for line in x:
        line = line.strip()
        L.append(line)
    return sorted(L,cmp=f)

#function for comparetion
def f(x,y):
    t1 = x.split()[-1]
    t2 = y.split()[-1]
    x = None
    y = None
    t1 = split_data_by_date(t1)
    t2 = split_data_by_date(t2)
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

#intended to by called by generate_sorted_data
def split_data_by_date(line):
        temp = line.strip().split()
        temp = temp[-1]
        assert(len(temp) > 5)
        year, temp = temp.split('年')
        month, temp = temp.split('月')
        temp = temp.split('日')
        if len(temp) > 1:
            day = temp[0]
            hour, min = -1, -1
            if len(temp[1])>2:
                temp = temp[1].split(':')
                assert (len(temp) == 2)
                hour , min = temp[0],temp[1]
            time = (int(hour),int(min))
        else:
            day = temp[0]
            time = (-1,-1)
        return	(int(year),int(month),int(day),time)

#open the oringinal data file, and create a new file user_click_data_sorted, which is a file needed by other functions.
def create_sorted_by_time_file():
	x = generate_sorted_data('user_click_data_final.txt')
	y = open('user_click_data_sorted.txt','a')
	for i in x:
	    y.write(i+'\n')            
