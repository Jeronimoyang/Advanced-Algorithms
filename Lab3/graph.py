import numpy as np
# 定义 RandomGraph 类，用于生成随机加权图，并使用 Prim 算法计算最小生成树权值
class RandomGraph:
    # --------------- 构造函数 --------------- #
    def __init__(self, n: int):
        # 存储顶点数 n
        self.n = n
        # 创建邻接矩阵 graph，初始值全为 0，大小为 n*n
        # 该矩阵用于存储顶点之间的边权值
        self.graph = np.zeros((n, n))

    # --------------- randomize 方法 --------------- #
    # 生成一个 n 顶点随机图，任意两个顶点之间边的权值均匀分布于 (0, 1)
    def randomize(self):
        # 生成 n*n 的随机矩阵，元素值均匀分布于 (0, 1)
        self.graph = np.random.rand(self.n, self.n)
        # 将矩阵转换为下三角矩阵，对角线及其上三角元素值为 0
        self.graph = np.tril(self.graph, -1)  
        # 将下三角矩阵变成对称矩阵，构造无向图
        self.graph += self.graph.T  
        # 将对角线元素值设为无穷大，即不考虑自环
        np.fill_diagonal(self.graph, np.inf)  

    # --------------- prim 方法 --------------- #
    # Prim 算法计算最小生成树权值
    def prim(self):
        # 初始化 n
        n = self.n
        # 初始化 visited 数组为 False，表示顶点是否加入 MST
        visited = [False] * n
        # 从第 0 号定点开始构造 MST
        visited[0] = True
        # 初始化 dist 数组，存储 MST 中顶点到其余顶点的最短距离
        dist = self.graph[0].copy()
        # 初始化最小生成树的总权值
        mst = 0
        # 依次加入 n-1 个顶点
        for _ in range(n - 1):
            # 选择距离 MST 最近的顶点 u
            u = np.argmin(dist)
            # 更新 MST 的总权值
            mst += dist[u]
            # 将顶点 u 加入 MST
            dist[u] = np.inf
            # 更新 MST 中其他顶点到 MST 的最短距离
            visited[u] = True
            # 更新 dist 数组
            for v in range(n):
                # 如果顶点 v 未加入 MST 且 u-v 之间的边权值小于 dist[v]
                if not visited[v] and self.graph[u, v] < dist[v]:
                    # 更新 dist[v] 为 u-v 之间的边权值
                    dist[v] = self.graph[u, v]
        # 返回 MST 的总权值
        return mst
    
    # --------------- kruskal 方法 --------------- #
    # Kruskal 算法计算最小生成树权值
    def kruskal(self):
        # 初始化 n
        n = self.n
        # 初始化 edges 数组，存储图中所有边的信息
        edges = []
        # 遍历邻接矩阵，将边的信息加入 edges 数组
        for i in range(n):
            for j in range(i+1, n):
                if self.graph[i, j] != np.inf:
                    edges.append((i, j, self.graph[i, j]))
        # 按照边的权值从小到大排序
        edges.sort(key=lambda x: x[2])
        # 初始化 parent 数组，存储顶点的父节点
        parent = list(range(n))
        # 记录树的深度
        rank = [0] * n
        # --------------- 查找操作 --------------- #
        # 用于查找顶点 x 所属的连通分量的根节点
        def find(x):
            # 如果 x 不是根节点，则递归查找其根节点
            if parent[x] != x:
                parent[x] = find(parent[x])
            # 返回 x 的根节点
            return parent[x]
        
        # --------------- 合并操作 --------------- #
        def union(x, y):
            # 查找 x 和 y 的根节点
            root_x = find(x)
            root_y = find(y)
            # 如果 x 和 y 不在同一个连通分量中，则合并
            if root_x != root_y:
                # 如果 x 的树深度小于 y 的树深度，则将 x 的根节点设为 y
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                # 如果 x 的树深度大于 y 的树深度，则将 y 的根节点设为 x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                # 如果 x 和 y 的树深度相等，则将其中一个设为另一个的根节点，并更新树深
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                # 返回 True 表示合并成功
                return True
            # 返回 False 表示 x 和 y 已在同一个连通分量中
            return False
        # kruskal 算法计算最小生成树的总权值
        # 初始化 mst 为 0，表示最小生成树的总权值
        mst = 0
        # 记录已加入 MST 的边数
        edge_count = 0
        # 遍历 edges 数组，即所有边的信息
        for u, v, w in edges:
            # 如果 u 和 v 不在同一个连通分量中，则将 u-v 加入 MST
            if union(u, v):
                mst += w
                edge_count += 1
                if edge_count == n - 1:
                    break
        # 返回 MST 的总权值
        return mst