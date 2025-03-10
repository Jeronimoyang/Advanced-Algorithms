from dataloader import DataLoader
from naive import Naive
from minHash import MinHash
import random
import time


# --------------- 参数设置 --------------- #
n_samples = 500 # 采样数
b = 10           # MinHash 方法的 band 数量
r = 10           # MinHash 方法的 row 数量
# 记录最优 band 和 row 的参数
best = {"b": None, "r": None, "result": None, "value": 100000}
c = 0.9         # Naive 方法的阈值
FILE_PATH = './data/E1_kosarak_100k.txt' # 数据集路径

# --------------- 数据加载 --------------- #
# 读取数据集，将相同标号的元素放在一个集合中
# 最终将整个数据集，用若干个集合表示
def data(file_path):
    # 打印数据加载信息
    print('Data Loading...')
    # 设置时间起点
    time_start = time.time()
    # 调用 DataLoader 类的 load 方法加载数据
    corpus = DataLoader(file_path).load()
    # 设置时间终点
    time_end = time.time()
    # 打印数据加载信息
    print('Data Loaded!')
    # 打印数据集大小和加载时间
    print(f'Number of Set: {len(corpus)}')
    print(f'Time: {time_end - time_start}s')
    # 返回列表 corpus，每个元素是一个集合
    return corpus

# --------------- 采样 --------------- #
# 从若干个集合中随机采样 n_samples 个集合
def sample(corpus, n_samples):
    # 打印采样信息
    print('Random Sampling...')
    # 设置时间起点
    time_start = time.time()
    # 使用 random.sample 方法从 corpus 中随机采样 n_samples 个样本
    samples = random.sample(corpus, n_samples)
    # 设置时间终点
    time_end = time.time()
    # 打印采样信息
    print(f'Number of Samples: {n_samples}')
    print('Sampling Done!')
    print(f'Time: {time_end - time_start}s')
    # 返回列表 samples，每个元素是一个集合
    return samples

# --------------- navie 方法 --------------- #
# 使用暴力方法计算相似集合对的数量
def naiveMethod(samples, c):
    # 打印 Naive 方法信息
    print('Naive Method Running...')
    # 设置时间起点
    time_start = time.time()
    # 调用 Naive 类的 run 方法
    naive = Naive()
    naive_result = naive.run(samples, c)
    # 设置时间终点
    time_end = time.time()
    # 打印 Naive 方法信息
    print(f'Naive Method Result: {len(naive_result)}')
    print(f'Time: {time_end - time_start}s')
    # 返回相似集合对的数量
    return len(naive_result)

# --------------- 数据预处理 --------------- #
# 汇总所有集合的元素种类，并将元素进行排序，生成对应的索引，
# 再用索引值代替元素，表示集合的特征
# 最终返回：用索引值表示的集合数据；元素种类的数量
def preProcess(corpus):
    # 设置时间起点
    print('Preprocess...')
    time_start = time.time()
    # data1 和 data2 用于存储合并后的数据集，flag 用于控制数据合并的轮次
    data1 = []
    data2 = []
    flag = 0
    # 将 corpus 中的集合两两合并，并去重，合并后的集合添加到 data1 中
    for i in range(0, len(corpus) - 1, 2):
        data1.append(list(set(corpus[i]).union(set(corpus[i + 1]))))
    # 如果 corpus 的长度为奇数，将最后一个集合添加到 data1 中
    if len(corpus) % 2 != 0:
        data1.append(list(set(corpus[-1])))
    # 对合并后的集合进行处理，直到只剩下一个集合
    while True:
        # 如果 flag 为 0
        if flag == 0:
            # 遍历 data1 中的集合，两两合并，并去重，合并后的集合添加到 data2 中
            for j in range(0, len(data1) - 1, 2):
                data2.append(list(set(data1[j]).union(set(data1[j + 1]))))
            # 如果 data1 的长度为奇数，将最后一个集合添加到 data2 中
            if len(data1) % 2 != 0:
                data2.append(list(set(data1[-1])))
            # 如果 data2 的长度为 1
            if len(data2) == 1:
                # 打乱 data2 中的元素顺序
                random.shuffle(data2[0])
                # 将 data2 中的元素赋值给 values
                values = data2[0]
                # 跳出循环
                break
            # 将 data1 置空
            data1 = []
            # 将 flag 设置为 1
            flag = 1
        # 如果 flag 为 1
        if flag == 1:
            # 遍历 data2 中的集合，两两合并，并去重，合并后的集合添加到 data1 中
            for j in range(0, len(data2) - 1, 2):
                data1.append(list(set(data2[j]).union(set(data2[j + 1]))))
            # 如果 data2 的长度为奇数，将最后一个集合添加到 data1 中
            if len(data2) % 2 != 0:
                data1.append(list(set(data2[-1])))
            # 如果 data1 的长度为 1
            if len(data1) == 1:
                # 打乱 data1 中的元素顺序
                random.shuffle(data1[0])
                # 将 data1 中的元素赋值给 values
                values = data1[0]
                # 跳出循环
                break
            # 将 data2 置空
            data2 = []
            # 将 flag 设置为 0
            flag = 0
    # 将 values 中的元素进行排序
    values = sorted(list(values))
    # 创建字典 value2index，用于存储 values 中的元素和其对应的索引
    value2index = dict()
    # 遍历 values 中的元素，将元素和其索引添加到 value2index 中
    for i, element in enumerate(values):
        value2index[element] = i
    # 创建列表 data，用于存储处理后的数据集
    data = [[] for _ in range(len(corpus))]
    # 遍历 corpus 中的集合，将集合中的元素转换为其在 values 中的索引
    for i in range(len(corpus)):
        for element in corpus[i]:
            data[i].append(value2index[element])
    # 设置时间终点
    time_end = time.time()
    print('Done!')
    print(f'Time: {time_end - time_start}s')
    # 返回处理后的数据集 data 和 values 的长度
    return data, len(values)

# --------------- MinHash 方法 --------------- #
def minHashMethod(samples, n, b, r):
    # 打印 MinHash 方法信息
    print('MinHash Method Running...')
    # 设置时间起点
    time_start = time.time()
    # 调用 MinHash 类的 run 方法
    minHash = MinHash(b, r)
    minHash_result = minHash.run(samples, n)
    # 设置时间终点
    time_end = time.time()
    # 打印 Min
    print(f'b = {b} r = {r}')
    print(f'MinHash Method Result: {minHash_result}')
    print(f'Time: {time_end - time_start}s')

# --------------- 参数设置 --------------- #
def main():
    # 加载数据
    print('............................................................')
    corpus = data(FILE_PATH)
    # 采样
    print('............................................................')
    #samples = sample(corpus, n_samples)
    # Naive 方法
    print('............................................................')
    #naive_result = naiveMethod(corpus, c)
    #naive_result = naiveMethod(samples, c)
    # 数据预处理
    print('............................................................')
    #processed, n_elements = preProcess(samples)
    processed, n_elements = preProcess(corpus)
    # MinHash 方法
    print('............................................................')
    minHashMethod(processed, n_elements, b, r)

if __name__ == '__main__':
    main()