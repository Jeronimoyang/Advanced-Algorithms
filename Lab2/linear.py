# 定义 Linear 类，实现线性时间选择算法
class Linear:
    # --------------- 构造函数 --------------- #
    def __init__(self, corpus, k):
        # 初始化数据集和 k 值
        self.corpus = corpus
        self.k = k

    # --------------- 静态方法 --------------- #
    @staticmethod
    # 交换数组中两个元素的位置
    def swap(a, i, j):
        # 如果 i 和 j 相等，直接返回
        if i == j:
            return
        # 否则交换 i 和 j 位置的元素
        temp = a[j]
        a[j] = a[i]
        a[i] = temp

    # --------------- 找到 a[l:r] 子数组的近似中位数 --------------- #
    def findMid(self, a, l, r):
        # 递归结束条件：如果区间只有一个元素，直接返回该索引
        if l == r:
            return l
        # 初始化 i 和 n
        i = l
        n = 0
        # 以步长为 5 遍历数组
        for i in range(l, r-4, 5):
            # 对每个步长为 5 的子数组进行排序
            a[i: i + 5] = sorted(a[i: i + 5])
            # 计算当前组的起始位置相对于 l 的偏移量
            n = i - l
            # 交换当前组的中位数和 a[l+n//5] 位置的元素
            self.swap(a, l + n // 5, i + 2)
        ## 处理剩余元素
        if r - 4 > l:
            i += 5
            n = i - l
        # 计算剩余元素的个数
        num = r - i
        # 如果剩余元素个数大于 0，对剩余元素进行排序
        if num > 0:
            a[i:i+num] = sorted(a[i:i+num])
            n = i - l
            # 交换剩余元素的中位数和 a[l+n//5] 位置的元素
            self.swap(a, l + n // 5, i + num // 2)
        # n 记录的是放置中位数的最后索引位置
        n //= 5
        # 如果 n 等于 l，直接返回 l
        if n == l:
            return l
        # 否则递归调用 findMid 函数，找到中位数的中位数
        return self.findMid(a, l, l + n)

    # --------------- partition 函数 --------------- #
    # 和快速排序的 partition 函数类似，将数组 a[l:r] 分为两部分
    def partition(self, a, l, r, p):
        # 交换 p 和 l 位置的元素
        self.swap(a, p, l)
        # 初始化 i 和 j
        i = l
        j = r - 1
        # 选取 pivot 为 a[l]
        pivot = a[l]
        # 使用快速排序的 partition 函数进行分区
        while i < j:
            # 如果 a[j] 大于等于 pivot，j 减 1，即向左移动
            while a[j] >= pivot and i < j:
                j -= 1
            # 如果 a[i] 小于等于 pivot，i 加 1，即向右移动
            while a[i] <= pivot and i < j:
                i += 1
            if i < j:
                # 交换 a[i] 和 a[j] 位置的元素
                self.swap(a, i, j)
        # 交换 a[l] 和 a[i] 位置的元素
        self.swap(a, l, i)
        # 返回 i，即 pivot 的位置索引
        return i

    # --------------- select 函数 --------------- #
    def select(self, a, l, r, k):
        # 找到中位数的中位数
        p = self.findMid(a, l, r)
        # 按该中位数划分数组
        i = self.partition(a, l, r, p)
        # 左半部分的元素个数
        m = i - l + 1
        # 如果左半部分的元素个数等于 k，直接返回 a[i]
        if m == k:
            # 找到第 k 小的元素
            return a[i]
        # 如果左半部分的元素个数大于 k，递归调用 select
        elif m > k:
            # 在左半部分继续查找
            return self.select(a, l, i, k)
        # 如果左半部分的元素个数小于 k，递归调用 select
        else:
            # 在右半部分继续查找
            return self.select(a, i + 1, r, k - m)

    # --------------- 运行函数 --------------- #
    def run(self, name_list):
        # 创建空字典，用于存储最终的 k 小值
        result = {}
        # 遍历数据类型集
        for name in name_list:
            # 复制一份数据集
            temp = self.corpus[name][:]
            # 找到第 k 小的元素，并存入 result 字典
            result[name] = self.select(temp, 0, len(temp), self.k)
        # 返回找到的 k 小值
        return result