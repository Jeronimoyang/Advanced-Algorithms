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
        num = r - i
        if num > 0:
            a[i:i+num] = sorted(a[i:i+num])
            n = i - l
            self.swap(a, l + n // 5, i + num // 2)
        n //= 5
        if n == l:
            return l
        return self.findMid(a, l, l + n)

    def partition(self, a, l, r, p):
        self.swap(a, p, l)
        i = l
        j = r - 1
        pivot = a[l]
        while i < j:
            while a[j] >= pivot and i < j:
                j -= 1
            a[i] = a[j]
            while a[i] <= pivot and i < j:
                i += 1
            a[j] = a[i]
        a[i] = pivot
        return i

    def select(self, a, l, r, k):
        p = self.findMid(a, l, r)
        i = self.partition(a, l, r, p)
        m = i - l + 1
        if m == k:
            return a[i]
        elif m > k:
            return self.select(a, l, i, k)
        else:
            return self.select(a, i + 1, r, k - m)

    def run(self, name_list):
        result = {}
        for name in name_list:
            temp = self.corpus[name][:]
            result[name] = self.select(temp, 0, len(temp), self.k)
        return result