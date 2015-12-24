# -*- coding: utf-8 -*-
from numpy import *
from numpy import linalg as la


def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]           #datamat的列数
    simTotal = 0.0
    ratSimTotal = 0.0
    U,Sigma,VT = la.svd(dataMat)
    Sig3 = mat(eye(3)*Sigma[:3]) #arrange Sig4 into a diagonal matrix
    xformedItems = dot(dot(dataMat.T,U[:,:3]), Sig3.I) #create transformed items
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 or j==item:
            continue
        similarity = simMeas(xformedItems[item,:].T,\
                             xformedItems[j,:].T)
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal/simTotal

#协同过滤算法
#dataMat 用户数据 user 用户 simMeas 相似度计算方式 item 物品
def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1] #计算列的数量，物品的数量
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        print(dataMat[user,j])
        if userRating == 0:
            continue  #如果用户u没有对物品j进行打分，那么这个判断就可以跳过了
        overLap = nonzero(logical_and(dataMat[:,item].A>0, \
                                      dataMat[:,j].A>0))[0]    #找到对物品 j 和item都打过分的用户
        if len(overLap) == 0:
            similarity = 0
        else:
            # item_avl = sum(dataMat[overLap,item])/float(len(overLap))
            # j_avl = sum(dataMat[overLap,j])/float(len(overLap))
            similarity = simMeas(dataMat[overLap,item], dataMat[overLap,j])     #利用相似度计算两个物品之间的相似度

        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating  #待推荐物品与用户打过分的物品之间的相似度*用户对物品的打分
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal/simTotal

def ecludSim(inA,inB):
    return 1.0/(1.0 + la.norm(inA - inB))  #欧式距离


def pearsSim(inA,inB):
    if len(inA) < 3 :
        return 1.0
    return 0.5+0.5*corrcoef(inA, inB, rowvar = 0)[0][1]  #corrcoef直接计算皮尔逊相关系

def cosSim(inA,inB):
    num =inA.T*inB
    denom = la.norm(inA)*la.norm(inB)
    return 0.5+0.5*(num/denom)  #计算余弦相似度


if __name__ == "__main__":
    data = mat(  [[0,5,3,1,1],\
                  [4,5,3,0,2],\
                  [2,1,0,5,4],\
                  [0,2,3,0,3],\
                  [5,1,2,4,0]])

    res = svdEst(data,2,cosSim,2)
    print "user %d item  %d recommend rating is : %f " % (2,2,res)