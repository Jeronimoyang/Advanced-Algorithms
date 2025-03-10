# 加载数据集
class DataLoader:
    # --------------- 初始化数据 --------------- #
    def __init__(self, file_path):
        # 定义字典，同于存储每个key对应的集合
        self.dict = dict()
        # 逐行读取文件
        for line in open(file_path):
            # 去除首尾空格，并按制表符分割
            line = line.strip().split('\t')
            # 如果字典中没有这个key，则添加一个新的key-value
            if not self.dict.get(int(line[0])):
                self.dict[int(line[0])] = {int(line[1])}
            # 如果字典中有这个key，则添加一个新的value
            else:
                self.dict[int(line[0])].add(int(line[1]))
        # 将字典中的value转换为list，并存储到corpus中
        self.corpus = []
        for value in self.dict.values():
            self.corpus.append(list(value))
    # --------------- 加载数据 --------------- #
    def load(self):
        # 返回corpus，即所有集合的列表
        return self.corpus