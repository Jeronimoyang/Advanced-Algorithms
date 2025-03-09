import numpy as np
import hashlib

# 实现 MinHash 和局部敏感哈希（LSH）算法
# 估计集合之间的相似度
class MinHash:
    # 初始化 MinHash 类
    def __init__(self, b, r):
        self.b = b
        self.r = r

    # 静态方法，不依赖于类的实例 self
    @staticmethod
    # 对数据应用单一哈希函数进行处理，用来生成单一的 MinHash 值
    def singleHash(data, n):
        # 创建一个长度为 n 的序列
        seq = [i for i in range(n)]
        # 创建一个长度为 len(data) 的列表，用来存储 MinHash 值
        result = [n for _ in range(len(data))]
        # 生成一个随机排列的索引序列，相当于一个哈希函数
        seq = np.random.permutation(seq)
        # 遍历 data 中的每个集合，找到每个集合中的最小哈希值
        for i in range(len(result)):
            # 初始化 minhash 为 n 最大值
            minhash = n
            # 遍历集合中的每个元素
            for element in data[i]:
                # 如果元素的哈希值小于 minhash
                if seq[element] < minhash:
                    result[i] = element
                    minhash = seq[element]
        # 返回 MinHash 值
        return result

    # 计算 sigMatrix
    def sigMatrix(self, data, n_elements, n_hash_funcs):
        # 初始化结果列表
        result = []
        # 循环 n_hash_funcs 次，每次生成一个 MinHash 值列表
        for i in range(n_hash_funcs):
            # 生成一个 MinHash 值列表
            single = self.singleHash(data, n_elements)
            # 将 MinHash 值列表添加到结果列表中
            result.append(single)
        # 返回结果列表，转换为 NumPy 矩阵
        return np.array(result)

    # 计算 MinHash
    def minHash(self, data, n_elements):
        # 初始化哈希桶
        hashBuckets = {}
        # 表示MinHash值的数量，b是band的数量，r是每个band的行数
        n = self.b * self.r
        # 计算 sigMatrix，n 行，len(data)列，每行对应一个 MinHash 值
        sigMatrix = self.sigMatrix(data, n_elements, n)
        # 初始化 begin 和 end
        begin, end = 0, self.r
        count = 0
        # 遍历 sigMatrix 的每一行
        while end <= sigMatrix.shape[0]:
            count += 1
            # 遍历 sigMatrix 的每一列
            for colNum in range(sigMatrix.shape[1]):
                # 创建一个 MD5 哈希对象
                hashObj = hashlib.md5()
                # 
                band = str(sigMatrix[begin: begin + self.r, colNum]) + str(count)
                hashObj.update(band.encode())
                tag = hashObj.hexdigest()
                if tag not in hashBuckets:
                    hashBuckets[tag] = [colNum]
                elif colNum not in hashBuckets[tag]:
                    hashBuckets[tag].append(colNum)
            begin += self.r
            end += self.r

        return hashBuckets

    # 计算 MinHash + LSH，相似集合对的数量
    def run(self, data, n):
        # 调用 minHash 方法，计算 MinHash 值，并进行局部敏感哈希处理
        hashBucket = self.minHash(data, n)
        # 初始化结果列表，存储每个文档的相似文档集合
        result = [set() for _ in range(len(data))]
        # 遍历 hashBucket 中的每个哈希桶
        for key in hashBucket:
            # 遍历哈希桶中的所有文档编号col1
            for col1 in hashBucket[key]:
                # 遍历哈希桶中的所有文档编号col2
                for col2 in hashBucket[key]:
                    # 如果 col1 == col2，跳过
                    if col1 == col2:
                        break
                    # 将 col2 添加到 col1 的相似文档集合中
                    result[col1].add(col2)
        # 计算总相似配对数
        sum = 0
        for s in result:
            sum += len(s)
        # 返回相似配对数
        return sum