import numpy as np
# --------------- 生成不同分布的随机数数据集 --------------- #
class DataGenerator:
    # --------------- 构造函数，在对象创建时调用 --------------- #
    def __init__(self, n):
        # 生成n个均匀分布、正态分布和Zipf分布的随机数
        # 定义 self.dict 字典，存储三种分布的 n 个随机数
        # uniform：生成 n 个均匀分布的随机数，范围为 [1, 1000]
        # normal：生成 n 个正态分布的随机数，均值为 500，标准差为 200
        # zipf：生成 n 个 Zipf 分布的随机数，参数为 1.2
        self.dict = {"uniform": np.random.uniform(1, 1001, n).astype(int).tolist(),
                     "normal": np.random.normal(500, 200, n).astype(int).tolist(),
                     "zipf": np.random.zipf(1.2, n).astype(int).tolist()}
    # --------------- 加载函数 --------------- #
    def load(self):
        # 返回字典对象，存储三种分布的 n 个随机数
        return self.dict