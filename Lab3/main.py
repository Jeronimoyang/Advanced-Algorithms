from graph import RandomGraph
import time
from draw import draw_time, draw_weights
import numpy as np

def main():
    # 创建一个 n_list 数组，表示不同的图规模
    n_list = np.arange(16, 1024, 16)
    # 定义 iter_num 表示每个图规模的图生成和算法运行次数
    iter_num = 10
    # 定义 runtimes 和 mst_weights 两个列表，分别用于存储运行时间和 MST 权值
    prim_runtimes = []
    prim_mst_weights = []
    kruskal_runtimes = []
    kruskal_mst_weights = []
    # 遍历 n_list 数组，即对不同的图规模 n 进行测试
    for n in n_list:
        print(f"---------- The graph scale is {n} vertices ----------")
        # 创建 RandomGraph 类的实例，表示一个 n 顶点的随机图
        graph = RandomGraph(n)
        # 初始化 mst_weight 为 0
        prim_mst_weight = 0
        kruskal_mst_weight = 0
        # 初始化 runtime 为 0
        prim_runtime = 0
        kruskal_runtime = 0
        # 进行 iter_num 次 Prim 算法的运行
        for num in range(iter_num):
            # 随机化 graph，生成一个 n 顶点的随机加权图
            graph.randomize()

            # 计算 Prim 算法的起始时间
            prim_start_time = time.time()
            # 运行 Prim 算法，计算最小生成树的权值
            prim_mst_weight += graph.prim()
            # 计算 Prim 算法的结束时间
            prim_end_time = time.time()
            # 计算 Prim 算法的运行时间
            prim_runtime += prim_end_time - prim_start_time

            # 计算 Kruskal 算法的起始时间
            kruskal_start_time = time.time()
            # 运行 Kruskal 算法，计算最小生成树的权值
            kruskal_mst_weight += graph.kruskal()
            # 计算 Kruskal 算法的结束时间
            kruskal_end_time = time.time()
            # 计算 Kruskal 算法的运行时间
            kruskal_runtime += kruskal_end_time - kruskal_start_time

        # 计算 Prim 算法的平均运行时间和 MST 权值
        prim_runtimes.append((n, (prim_runtime/iter_num)))
        prim_mst_weights.append((n, (prim_mst_weight/iter_num)))
        print(f"Average prim runtime: {prim_runtime/iter_num} seconds")
        print(f"Average prim mst_weight: {prim_mst_weight/iter_num}")
        # 计算 Kruskal 算法的平均运行时间和 MST 权值
        kruskal_runtimes.append((n, (kruskal_runtime/iter_num)))
        kruskal_mst_weights.append((n, (kruskal_mst_weight/iter_num)))
        print(f"Average kruskal runtime: {kruskal_runtime/iter_num} seconds")
        print(f"Average kruskal mst_weight: {kruskal_mst_weight/iter_num}")
    print("---------- Plotting data images ----------")
    # 绘制算法的运行时间随图规模变化的曲线
    draw_time(prim_runtimes, kruskal_runtimes)
    # 绘制 MST 权值随图规模变化的曲线
    draw_weights(prim_mst_weights, kruskal_mst_weights)


if __name__ == '__main__':
    main()