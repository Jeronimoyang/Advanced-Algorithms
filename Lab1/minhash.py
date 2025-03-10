import numpy as np
import matplotlib.pyplot as plt
# 使用 minhash 算法计算集合之间的相似度
class MinHash:
    # --------------- 初始化方法，不做任何事情 --------------- #
    def __init__(self):
        pass
    
    # --------------- 静态方法，不依赖于类的实例 self --------------- #
    @staticmethod
    # 计算相似集合对
    def minhash_work(n_element,sample,c):
        # 创建一个空列表，用于存储相似集合对
        R=set()
        # 创建长度为500*500的列表，用于存储相似集合对的数量
        ans=[0 for i in range(500*500)]
        # 采用多次哈希 50次
        for _ in range(50):
            # 生成长度为 n_element 的索引列表
            per=[i for i in range(n_element)]
            # 对索引列表进行随机排列
            per=np.random.permutation(per)
            # 创建长度为 n_element 的列表，用于存储索引
            pos=[0 for i in range(n_element)]
            # 遍历索引列表
            for i in range(n_element):
                # 记录元素在新的排列的位置
                pos[per[i]]=i
            # 创建长度为 len(sample) 的列表，用于存储最小哈希值
            res=[10**8 for i in range(len(sample))]
            # 遍历所有集合
            for i in range(len(sample)):
                # 创建一个变量，用于存储当前集合的最小哈希值
                mn=10**8
                # 遍历集合中的元素
                for j in range(len(sample[i])):
                    # 如果当前元素的哈希值小于当前集合的最小哈希值
                    if pos[sample[i][j]]<mn:
                        # 更新当前集合的最小哈希值
                        mn=pos[sample[i][j]] 
                # 将当前集合的最小哈希值存入列表中
                res[i]=mn
            # 遍历所有集合
            for i in range(len(sample)-1):
                # 遍历所有集合
                for j in range(i+1,len(sample)):
                    # 如果两个集合的最小哈希值相等
                    if res[i]==res[j]:
                        # 记录相似集合对(i,j)
                        ans[(i-1)*len(sample)+j]=ans[(i-1)*len(sample)+j]+1
        # 遍历所有集合
        for i in range(len(sample)-1):
            # 遍历所有集合
            for j in range(i+1,len(sample)):
                # 如果两个集合的相似度大于阈值
                if(ans[(i-1)*len(sample)+j]>=c*50):
                    # 记录相似集合对(i,j)
                    R.add((i,j))
        # 返回相似集合对
        return R

