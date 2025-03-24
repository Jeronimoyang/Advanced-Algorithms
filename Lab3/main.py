from graph import RandomGraph
import time
from draw import draw_time, draw_weights
import numpy as np

def main():
    # 创建一个 n_list 数组，表示不同的图规模
    n_list = np.arange(16, 1040, 16)
    # 定义 iter_num 表示每个图规模的图生成和 Prim 算法运行次数
    iter_num = 10
    # 定义 runtimes 和 mst_weights 两个列表，分别用于存储运行时间和 MST 权值
    runtimes = []
    mst_weights = []
    # 遍历 n_list 数组，即对不同的图规模 n 进行测试
    for n in n_list:
        print(f"---------- The graph scale is {n} vertices ----------")
        # 创建 RandomGraph 类的实例，表示一个 n 顶点的随机图
        graph = RandomGraph(n)
        # 初始化 mst_weight 为 0
        mst_weight = 0
        # 计算 Prim 算法的起始时间
        start_time = time.time()
        # 进行 iter_num 次 Prim 算法的运行
        for num in range(iter_num):
            #print(f"{num}th calculation")
            # 随机化 graph，生成一个 n 顶点的随机加权图
            graph.randomize()
            # 运行 Prim 算法，计算最小生成树的权值
            mst_weight += graph.prim()
        # 计算 Prim 算法的结束时间
        end_time = time.time()
        # 计算 Prim 算法的平均运行时间和 MST 权值
        runtimes.append((n, ((end_time - start_time)/iter_num)))
        mst_weights.append((n, (mst_weight/iter_num)))
        print(f"Average runtime: {(end_time - start_time)/iter_num} seconds")
        print(f"Average mst_weight: {mst_weight/iter_num}")
    print("---------- Plotting data images ----------")
    # 绘制 Prim 算法的运行时间随图规模变化的曲线
    draw_time(runtimes)
    # 绘制 MST 权值随图规模变化的曲线
    draw_weights(mst_weights)


if __name__ == '__main__':
    main()