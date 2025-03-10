from Dataloader import DataLoader
from naive import Naive
from minhash import MinHash
import random
import time

n_samples=500
c=0.9
FILE_PATH='./data/E1_kosarak_100k.txt'

def data(file_path):
    print('Data Loading...')
    time_start=time.time()
    corpus=DataLoader(file_path).load()
    time_end=time.time()
    print('Data Loaded!')
    print(f'Number of Set:{len(corpus)}')
    print(f'Time:{time_end-time_start}s')
    return corpus

def sample(corpus,n_samples):
    print('Random Sampling...')
    time_start=time.time()
    samples=random.sample(corpus, n_samples)
    time_end=time.time()
    print(f'Number of Samples:{n_samples}')
    print('Sampling Done!')
    print(f'Time:{time_end-time_start}s')
    return samples

def naiveMethod(samples,c):
    print('Naive Method Running...')
    time_start=time.time()
    naive=Naive()
    naive_result=naive.run(samples,c)
    time_end=time.time()
    print(f'Naive Method Result:{len(naive_result)}')
    print(f'Time:{time_end-time_start}s')
    return len(naive_result)

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

def MinHashMethod(tot,sample,c):
    print('MinHash Method Running...')
    # 设置时间起点
    time_start=time.time()
    mh=MinHash()
    mh_result=mh.minhash_work(tot,sample,c)
    # 设置时间终点
    time_end=time.time()
    print(f'MinHash Method Result:{len(mh_result)}')
    print(f'Time:{time_end-time_start}s')
    return len(mh_result)

if __name__=='__main__':
    corpus=data(FILE_PATH)
    samples=sample(corpus,n_samples)
    samples,tot=create_data(samples)
    naive_result=naiveMethod(samples,c)
    mh_result=MinHashMethod(tot,samples,c)


