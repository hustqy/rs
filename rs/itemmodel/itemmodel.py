# -*- coding: utf-8 -*-
from numpy import *
from numpy import linalg as la


class ItemModel:

    def __init__(self,matrix,user):
        self.matrix = mat(matrix)
        self.user = user

    def svdEst(self,data_mat, user, simMeas):
        result = {}                  #{item : rating}
        n = shape(data_mat)[1]           #data_mat的列数
        # simTotal = 0.0
        U,Sigma,VT = la.svd(data_mat)
        Sig3 = mat(eye(3)*Sigma[:3]) #arrange Sig4 into a diagonal matrix
        xformedItems = dot(dot(data_mat.T,U[:,:3]), Sig3.I) #create transformed items
        for item in xrange(n):
            ratSimTotal = 0.0
            for j in range(n):
                userRating = data_mat[user,j]
                if userRating == 0 or j==item:
                    continue
                similarity = simMeas(xformedItems[item,:].T,\
                                     xformedItems[j,:].T)
                # print 'the %d and %d similarity is: %f' % (item, j, similarity)
                # simTotal += similarity
                ratSimTotal += similarity * userRating
            # print "the news %d rating is: %f" % (item,ratSimTotal)
            result[item] = ratSimTotal
        return result
        # if simTotal == 0:
        #     return 0
        # else:
        #     return ratSimTotal/simTotal


    #协同过滤算法
    #data_mat 用户数据 user 用户 simMeas 相似度计算方式 item 物品
    def standEst(self,data_mat, user, simMeas, item):
        n = shape(data_mat)[1] #计算列的数量，物品的数量
        simTotal = 0.0; ratSimTotal = 0.0
        for j in range(n):
            userRating = data_mat[user,j]
            print(data_mat[user,j])
            if userRating == 0:
                continue  #如果用户u没有对物品j进行打分，那么这个判断就可以跳过了
            overLap = nonzero(logical_and(data_mat[:,item].A>0, \
                                          data_mat[:,j].A>0))[0]    #找到对物品 j 和item都打过分的用户
            if len(overLap) == 0:
                similarity = 0
            else:
                # item_avl = sum(data_mat[overLap,item])/float(len(overLap))
                # j_avl = sum(data_mat[overLap,j])/float(len(overLap))
                similarity = simMeas(data_mat[overLap,item], data_mat[overLap,j])     #利用相似度计算两个物品之间的相似度

            print 'the %d and %d similarity is: %f' % (item, j, similarity)
            simTotal += similarity
            ratSimTotal += similarity * userRating  #待推荐物品与用户打过分的物品之间的相似度*用户对物品的打分
        if simTotal == 0:
            return 0
        else:
            return ratSimTotal/simTotal

    @staticmethod
    def ecludSim(inA,inB):
        return 1.0/(1.0 + la.norm(inA - inB))  #欧式距离

    @staticmethod
    def pearsSim(inA,inB):
        if len(inA) < 3 :
            return 1.0
        return 0.5+0.5*corrcoef(inA, inB, rowvar = 0)[0][1]  #corrcoef直接计算皮尔逊相关系

    @staticmethod
    def cosSim(inA,inB):
        num =inA.T*inB
        denom = la.norm(inA)*la.norm(inB)
        return 0.5+0.5*(num/denom)  #计算余弦相似度


    def get_best_news(self):

        src_rates = self.matrix[self.user]

        self.svdEst(self.matrix,self.user,self.pearsSim,)


if __name__ == "__main__":
    data = mat(  [[0,5,3,1,1],\
                  [4,5,3,0,2],\
                  [2,1,0,5,4],\
                  [0,2,3,0,3],\
                  [5,1,2,4,0]])

    obj = ItemModel(data,2)
    res = obj.svdEst(data,2,obj.cosSim)
    # print "user %d item  %d recommend rating is : %f " % (2,2,res)