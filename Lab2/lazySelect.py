from sort import MergeSort
import numpy as np
import math

# 定义 LazySelect 类，实现懒惰选择算法，用于在数据集中选择第 k 小的元素
class LazySelect:
    # --------------- 构造函数 --------------- #
    def __init__(self, corpus, k):
        # 初始化数据集和 k 值
        self.corpus = corpus
        self.k = k

    # --------------- 静态函数 --------------- #
    @staticmethod
    # 从数据集中随机选择 n^0.75 个元素
    def randomSelect(data):
        return np.random.choice(data, int(pow(len(data), 0.75)), replace=True).tolist()

    # --------------- 构造函数 --------------- #
    @staticmethod
    # 计算元素在列表中的排名，即有多少个元素比它小
    def rank(list, element):
        # 确保元素在列表中
        assert element in list
        # 初始化计数器
        count = 0
        # 遍历列表中的每个元素
        for _ in list:
            # 如果当前元素小于目标元素
            if _ < element:
                # 计数器加一
                count += 1
        # 返回排名
        return count + 1

    # --------------- 构造函数 --------------- #
    def run(self, name_list):
        # 创建空字典，用于存储最终的 k 小值
        result = {}
        # 遍历数据类型集
        for name in name_list:
            # 复制一份数据集
            temp = self.corpus[name][:]
            # 记录数据集长度
            n = len(temp)
            # 初始化迭代次数
            epoch = 0

            # 迭代寻找第 k 小的元素
            while True:
                # 迭代次数加一
                epoch += 1
                # 从数据集中随机选择 n^0.75 个元素
                samples = self.randomSelect(temp)
                # 对样本进行归并排序
                merge = MergeSort()
                samples = merge.run(samples)

                # 计算 x 的值，大致估计第 k 小的元素的位置
                x = int(self.k * pow(n, -0.25))
                # 计算 l 和 r 的值，确保在数据集范围内
                l = max(0, int(x - math.sqrt(n)))
                r = min(int(pow(n, 0.75)), int(x + math.sqrt(n)))
                # 计算筛选区间的下界
                L = samples[max(1, l - 1)]
                # 计算筛选区间的上界
                H = samples[r - 1]
                # 计算 L 和 H 在原数据中的排名
                LP = self.rank(list=temp, element=L)
                HP = self.rank(list=temp, element=H)
                # 初始化 p 列表，用于存储在筛选区间内的元素
                p = []
                # 遍历样本集
                for num in temp:
                    # 如果 num 在筛选区间内
                    if L <= num <= H:
                        # 将 num 添加到 p 列表
                        p.append(num)

                # 如果满足以下条件，结束迭代
                # 1. 第 k 小元素在筛选区间内
                # 2. 筛选后的 p 足够小，即长度小于等于 4 * n^0.75 + 1
                if LP <= self.k <= HP and len(p) <= 4 * pow(n, 0.75) + 1:
                    # 对 p 进行归并排序
                    p = merge.run(p)
                    # 将第 k 小的元素存入 result 字典，计算相对排名
                    result[name] = p[self.k-LP]
                    # 记录迭代次数
                    result[name+"_epochs"] = epoch
                    # 结束迭代
                    break
        # 返回 result 字典
        return result