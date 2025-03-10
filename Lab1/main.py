from Dataloader import DataLoader
from naive import Naive
from minhash import MinHash
import random
import time
# --------------- 参数设置 --------------- #
n_samples=500   # 采样数量
c=0.9           # Naive 方法的阈值
FILE_PATH='./data/E1_kosarak_100k.txt'  # 数据集路径

# --------------- 数据加载 --------------- #
# 读取数据集，将相同标号的元素放在一个集合中
# 最终将整个数据集，用若干个集合表示
def data(file_path):
    # 打印数据加载信息
    print('Data Loading...')
    # 设置时间起点
    time_start=time.time()
    # 调用 DataLoader 类的 load 方法加载数据
    corpus=DataLoader(file_path).load()
    # 设置时间终点
    time_end=time.time()
    # 打印数据加载信息
    print('Data Loaded!')
    print(f'Number of Set:{len(corpus)}')
    print(f'Time:{time_end-time_start}s')
    # 返回列表 corpus，每个元素是一个集合
    return corpus

# --------------- 采样 --------------- #
# 从若干个集合中随机采样 n_samples 个集合
def sample(corpus,n_samples):
    # 打印采样信息
    print('Random Sampling...')
    # 设置时间起点
    time_start=time.time()
    # 使用 random.sample 方法从 corpus 中随机采样 n_samples 个样本
    samples=random.sample(corpus, n_samples)
    # 设置时间终点
    time_end=time.time()
    # 打印采样信息
    print(f'Number of Samples:{n_samples}')
    print('Sampling Done!')
    print(f'Time:{time_end-time_start}s')
    # 返回列表 samples，每个元素是一个集合
    return samples

# --------------- 数据预处理 --------------- #
# 汇总所有集合的元素种类，生成对应的索引，
# 再用索引值代替元素，表示集合的特征
# 最终返回：用索引值表示的集合数据；元素种类的数量
def create_data(sample):
    print('Discretization Running...')
    # 设置时间起点
    time_start=time.time()
    # 创建一个空集合
    S=set()
    # 遍历所有集合
    for i in range(len(sample)):
        # 遍历集合中的元素
        for j in range(len(sample[i])):
            # 将集合中的元素加入到集合S中，集合S中的元素不会重复
            S.add(sample[i][j]) 
    # 将集合S中的元素转换成列表
    num=list(S)
    # 遍历所有集合
    for i in range(len(sample)):
        # 遍历集合中的元素
        for j in range(len(sample[i])):
            # 遍历 num 列表，找到当前元素对应的索引
            for k in range(len(num)):
                # 如果当前元素等于 num 中的元素
                if sample[i][j]==num[k]:
                    # 将当前元素替换成 num 中的索引
                    sample[i][j]=k;
    # 设置时间终点
    time_end=time.time()
    print(f'Time:{time_end-time_start}s')
    print('Discretization Done')
    # 返回用索引表示的集合和元素种类数
    return sample,len(num)

# --------------- navie 方法 --------------- #
# 使用暴力方法计算相似集合对的数量
def naiveMethod(samples,c):
    # 打印 Naive 方法信息
    print('Naive Method Running...')
    # 设置时间起点
    time_start=time.time()
    # 调用 Naive 类的 run 方法
    naive=Naive()
    naive_result=naive.run(samples,c)
    # 设置时间终点
    time_end=time.time()
    # 打印 Naive 方法信息
    print(f'Naive Method Result:{len(naive_result)}')
    print(f'Time:{time_end-time_start}s')
    # 返回相似集合对的数量
    return len(naive_result)

# --------------- minHash 方法 --------------- #
# 使用 minHash 方法计算相似集合对的数量
def MinHashMethod(tot,sample,c):
    # 打印 MinHash 方法信息
    print('MinHash Method Running...')
    # 设置时间起点
    time_start=time.time()
    # 调用 MinHash 类的 minhash_work 方法
    mh=MinHash()
    mh_result=mh.minhash_work(tot,sample,c)
    # 设置时间终点
    time_end=time.time()
    # 打印 minHash 方法信息
    print(f'MinHash Method Result:{len(mh_result)}')
    print(f'Time:{time_end-time_start}s')
    # 返回相似集合对的数量
    return len(mh_result)

# --------------- 主函数 --------------- #
# 1. 加载数据
# 2. 采样
# 3. 数据预处理
# 4. Naive 方法
# 5. MinHash 方法
def main():
    corpus=data(FILE_PATH)
    samples=sample(corpus,n_samples)
    samples,tot=create_data(samples)
    naive_result=naiveMethod(samples,c)
    mh_result=MinHashMethod(tot,samples,c)

if __name__=='__main__':
    main()


