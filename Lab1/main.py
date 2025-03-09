from dataloader import DataLoader
from naive import Naive
from minHash import MinHash
import random
import time
# --------------- 参数设置 --------------- #
n_samples = 500 # 采样数
b = 5           # MinHash 方法的 band 数量
r = 4           # MinHash 方法的 row 数量
# 记录最优 band 和 row 的参数
best = {"b": None, "r": None, "result": None, "value": 100000}
c = 0.8         # Naive 方法的阈值
FILE_PATH = './data/E1_AOL-out.txt' # 数据集路径

# --------------- 数据加载 --------------- #
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
def preProcess(corpus):
    print('Preprocess...')
    time_start = time.time()

    data1 = []
    data2 = []
    flag = 0
    for i in range(0, len(corpus) - 1, 2):
        data1.append(list(set(corpus[i]).union(set(corpus[i + 1]))))
    if len(corpus) % 2 != 0:
        data1.append(list(set(corpus[-1])))
    while True:
        if flag == 0:
            for j in range(0, len(data1) - 1, 2):
                data2.append(list(set(data1[j]).union(set(data1[j + 1]))))
            if len(data1) % 2 != 0:
                data2.append(list(set(data1[-1])))
            if len(data2) == 1:
                random.shuffle(data2[0])
                values = data2[0]
                break
            data1 = []
            flag = 1
        if flag == 1:
            for j in range(0, len(data2) - 1, 2):
                data1.append(list(set(data2[j]).union(set(data2[j + 1]))))
            if len(data2) % 2 != 0:
                data1.append(list(set(data2[-1])))
            if len(data1) == 1:
                random.shuffle(data1[0])
                values = data1[0]
                break
            data2 = []
            flag = 0

    values = sorted(list(values))
    value2index = dict()
    for i, element in enumerate(values):
        value2index[element] = i
    data = [[] for _ in range(len(corpus))]
    for i in range(len(corpus)):
        for element in corpus[i]:
            data[i].append(value2index[element])

    time_end = time.time()
    print('Done!')
    print(f'Time: {time_end - time_start}s')
    return data, len(values)

# --------------- MinHash 方法 --------------- #
def minHashMethod(samples, n, b, r, naive_result):
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
    corpus = data(FILE_PATH)
    # 采样
    samples = sample(corpus, n_samples)
    # Naive 方法
    naive_result = naiveMethod(samples, c)
    # 数据预处理
    processed, n_elements = preProcess(samples)
    # MinHash 方法
    minHashMethod(processed, n_elements, b, r, naive_result)

if __name__ == '__main__':
    main()