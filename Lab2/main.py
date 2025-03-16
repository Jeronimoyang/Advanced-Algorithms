from createData import DataGenerator
from fsts import Fsts
from linear import Linear
from lazySelect import LazySelect
import numpy as np
import time as tm

N_SAMPLES = 1000    # 生成数据集的样本数量
K = 500             # 要在数据集中选择的第k小的元素

# --------------- 打印字典内容 --------------- #
# 作用：格式化并输出字典的内容
# 传入一个字典对象，存储键值对
def printDict(dic):
    # 遍历字典的每个键
    for key in dic.keys():
        # 打印键值对
        print(f"{key}: {dic[key]}")

# --------------- 加载数据 --------------- #
def data(n_samples):
    # 打印数据加载信息
    print('Data Loading...')
    # 记录开始时间
    time_start = tm.time()
    # 生成数据集
    corpus = DataGenerator(n_samples).load()
    # 记录结束时间
    time_end = tm.time()
    # 打印数据加载完成信息
    print('Data Loaded!')
    print(f'Number of Samples: {len(corpus)}')
    print(f'Time: {time_end - time_start}s')
    # 返回生成的数据集
    return corpus

# fisrt sort then select
# --------------- 先排序后直接抽取选择算法 --------------- #
def fstsMethod(corpus, k):
    # 记录开始时间
    time_start = tm.time()
    # 使用 Fsts 类初始化先排序后直接抽取选择算法
    fsts = Fsts(corpus, k)
    # 运行先排序后直接抽取选择算法，传入表示数据的三种类型
    result = fsts.run(["uniform", "normal", "zipf"])
    # 记录结束时间
    time_end = tm.time()
    # 打印先排序后直接抽取选择算法结果
    print('===========Fsts Method Result===========')
    printDict(result)
    print(f'Time: {time_end - time_start}s')
    # 返回先排序后直接抽取选择算法结果和运行时间
    return result, time_end - time_start

# --------------- 线性时间中位数选取算法 --------------- #
def linearMethod(corpus, k):
    # 记录开始时间
    time_start = tm.time()
    # 使用 Linear 类初始化线性时间中位数选取算法
    linear = Linear(corpus, k)
    # 运行线性时间中位数选取算法，传入表示数据的三种类型
    result = linear.run(["uniform", "normal", "zipf"])
    # 记录结束时间
    time_end = tm.time()
    # 打印线性时间中位数选取算法结果
    print('===========Linear Method Result===========')
    printDict(result)
    print(f'Time: {time_end - time_start}s')
    # 返回线性时间中位数选取算法结果和运行时间
    return time_end - time_start

# --------------- lazySelect 随机算法 --------------- #
def lazyMethod(corpus, k):
    # 记录开始时间
    time_start = tm.time()
    # 使用 LazySelect 类初始化 lazySelect 随机算法
    lazy = LazySelect(corpus, k)
    # 运行 lazySelect 随机算法，传入表示数据的三种类型
    result = lazy.run(["uniform", "normal", "zipf"])
    # 记录结束时间
    time_end = tm.time()
    # 打印 lazySelect 随机算法结果
    print('===========Lazy Method Result===========')
    printDict(result)
    print(f'Time: {time_end - time_start}s')
    # 返回 lazySelect 随机算法结果和运行时间
    return result, time_end - time_start

# --------------- 主程序 --------------- #
if __name__ == "__main__":
    # 生成数据集
    corpus = data(N_SAMPLES)
    # 初始化算法运行时间列表
    fstsTime = []
    linearTime = []
    lazyTime = []
    # 初始化错误计数
    error = 0
    # 循环运行10次
    for _ in range(10):
        # 打印当前循环次数
        print(f'=============Epoch {_+1}=============')
        # 运行先排序后直接抽取选择算法，返回结果和运行时间
        correct, time = fstsMethod(corpus, K)
        # 将运行时间添加到先排序后直接抽取选择算法运行时间列表中
        fstsTime.append(time)
        # 运行线性时间中位数选取算法，返回运行时间
        linearTime.append(linearMethod(corpus, K))
        # 运行 lazySelect 随机算法，返回结果和运行时间
        result, time = lazyMethod(corpus, K)
        # 将运行时间添加到 lazySelect 随机算法运行时间列表中
        lazyTime.append(time)
        # 计算错误次数
        error += int(correct["uniform"] != result["uniform"]) \
                 + int(correct["normal"] != result["normal"]) \
                 + int(correct["zipf"] != result["zipf"])
    # 打印总结
    print('=============Conclusion=============')
    print(f"Fsts: {np.mean(fstsTime)}")
    print(f"Linear: {np.mean(linearTime)}")
    print(f"Lazy: {np.mean(lazyTime)}")
    print(f"Accuracy: {1. - error/30.}")
