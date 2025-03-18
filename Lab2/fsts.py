from sort import MergeSort

# 使用归并排序对不用类型的数据进行排序，并找出第k小的元素
class Fsts:
    # --------------- 构造函数 --------------- #
    def __init__(self, corpus, k):
        # 初始化数据集和 k 值
        self.corpus = corpus
        self.k = k

    # --------------- 运行函数 --------------- #
    # 遍历数据集中的每种数据类型，对数据进行排序，并找出第 k 小的元素
    def run(self, name_list):
        # 创建空字典，用于存储最终的 k 小值
        result = {}
        # 创建 MergeSort 实例，用于执行归并排序
        merge = MergeSort()
        # 遍历数据类型集
        for name in name_list:
            # 对每类数据进行归并排序，得到一个升序排列的列表
            temp = merge.run(self.corpus[name])
            # 找到排序后的第 k 小值，并存入 result 字典
            result[name] = temp[self.k-1]
        # 返回找到的 k 小值
        return result