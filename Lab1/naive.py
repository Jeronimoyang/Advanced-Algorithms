# 使用 naive 方法实现集合相似性计算
class Naive:
    # 初始化方法，不做任何事情
    def __init__(self):
        pass
    
    # 静态方法，不依赖于类的实例 self
    @staticmethod
    # 计算两个列表之间的交集大小，即相同元素的个数
    def intersection(list1, list2):
        sum = 0
        for element1 in list1:
            for element2 in list2:
                if element1 == element2:
                    sum += 1
        return sum
    
    # 找到 corpus 中相似度大于 c 的集合对
    def run(self, corpus, c: float):
        # 创建一个空集合
        ans = set()
        # 遍历 corpus 中的所有集合
        for i in range(len(corpus)-1):
            for j in range(i+1, len(corpus)):
                # 计算两个集合的交集大小
                inter = self.intersection(corpus[i], corpus[j]) 
                # 计算两个集合的并集大小
                union = len(corpus[i]) + len(corpus[j]) - inter 
                # 如果交集大小除以并集大小大于等于 c
                if inter >= c * union:
                    # 将这两个集合的索引加入到集合 ans 中
                    ans.add((i, j))
        # 返回满足条件的集合对
        return ans