import numpy as np
import hashlib

# 实现 MinHash 和局部敏感哈希（LSH）算法
# 估计集合之间的相似度
class MinHash:
    # --------------- 初始化 MinHash 类 --------------- #
    def __init__(self, b, r):
        self.b = b
        self.r = r

    # --------------- 静态方法，不依赖于类的实例 self --------------- #
    # 进行一次随机排列，打乱索引值，计算每个集合的 MinHash 值
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

    # --------------- 计算 sigMatrix --------------- #
    # 进行随机排列，打乱索引值，计算每个集合的 MinHash 值
    # 重复 n_hash_funcs 次，生成 sigMatrix，即签名矩阵
    # 签名矩阵的每一行对应一个 MinHash 值列表
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
        # 表示MinHash函数的数量，b是band的数量，r是每个band的行数
        n = self.b * self.r
        # 计算 sigMatrix，n 行，len(data)列，每行对应一个 MinHash 值
        sigMatrix = self.sigMatrix(data, n_elements, n)
        # 初始化 begin 和 end
        begin, end = 0, self.r
        count = 0
        # 遍历 sigMatrix 的每一行，sigMatrix.shape[0] 表示 sigMatrix 的行数
        while end <= sigMatrix.shape[0]:
            # 当前的 band 编号
            count += 1
            # 在每个 band 中，遍历 sigMatrix 的每一列
            for colNum in range(sigMatrix.shape[1]):
                # 创建一个 MD5 哈希对象
                hashObj = hashlib.md5()
                # 提取当前 band 的值，转换为字符串，计算哈希值
                band = str(sigMatrix[begin: begin + self.r, colNum]) + str(count)
                # 将 band 字符串编码成字节格式，接着更新哈希对象，加入要计算哈希的内容
                hashObj.update(band.encode())
                # 计算并返回 band 的哈希值
                tag = hashObj.hexdigest()
                # 检查哈希桶中是否存在这个哈希值 tag
                if tag not in hashBuckets:
                    # 如果不存在，创建一个新的哈希桶，tag，即哈希值，作为键；colNum，即集合编号，作为值
                    # 每个哈希值对应着一个或多个集合
                    hashBuckets[tag] = [colNum]
                # 如果哈希桶中已经存在这个哈希值 tag
                elif colNum not in hashBuckets[tag]:
                    # 将 colNum，即集合编号，添加到哈希桶中
                    hashBuckets[tag].append(colNum)
            # 更新 begin 和 end，进入下一个 band
            begin += self.r
            end += self.r
        # 返回哈希桶，即哈希值 tag 和集合编号 colNum 的映射
        return hashBuckets

    # --------------- 计算 MinHash + LSH，相似集合对的数量 --------------- #
    def run(self, data, n):
        # 调用 minHash 方法，返回哈希桶，每个哈希桶对应一个哈希值 tag 和集合编号 colNum 的映射
        hashBucket = self.minHash(data, n)
        # 初始化结果列表，存储每个集合的相似集合编号
        #result = [set() for _ in range(len(data))]
        # 初始化已处理过的配对
        processed_pairs = set()
        # 遍历每个哈希桶
        for key in hashBucket:
            # 遍历哈希桶中的所有文档编号col1
            for col1 in hashBucket[key]:
                # 遍历哈希桶中的所有文档编号col2
                for col2 in hashBucket[key]:
                    # 如果 col1 == col2，将集合本身排除
                    if col1 == col2:
                        continue
                    sorted_pair = tuple(sorted((col1, col2)))
                    if sorted_pair in processed_pairs:
                        continue
                    # 将 col2 添加到 col1 的相似文档集合中
                    # 因为在一个哈希桶中，相同的哈希值对应着相似的集合
                    #result[col1].add(col2)
                    #print(col1, col2)
                    #num = num + 1
                    # 将已处理过的配对添加到 processed_pairs 中
                    processed_pairs.add(sorted_pair)
        # 计算总相似配对数
        sum = len(processed_pairs)
        # 返回相似配对数
        return sum