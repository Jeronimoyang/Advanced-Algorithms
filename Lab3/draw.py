import matplotlib.pyplot as plt
from mpmath import zeta

# --------------- 绘制算法的运行时间随图规模变化的曲线 --------------- #
def draw_time(prim_runtimes, kruskal_runtimes):
    n_list, prim_runtimes = zip(*prim_runtimes)
    n_list, kruskal_runtimes = zip(*kruskal_runtimes)
    plt.figure(figsize=(10, 6))
    plt.plot(n_list, prim_runtimes, marker='o', linestyle='-', color='b', label="prim")
    plt.plot(n_list, kruskal_runtimes, marker='o', linestyle='-', color='r', label="kruskal")
    plt.xlabel('N-value')   
    plt.ylabel('Running Time (seconds)')
    plt.title('Running Time of Algorithm vs. N-value') 
    plt.legend()
    plt.grid(True)

    save_path = f"./pic/runtime.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Save the runtime.png: {save_path}")

# --------------- 绘制 MST 权值随图规模变化的曲线 --------------- #
def draw_weights(prim_mst_weights, kruskal_mst_weights):
    n_list, prim_mst_weights = zip(*prim_mst_weights)
    #n_list, kruskal_mst_weights = zip(*kruskal_mst_weights)
    plt.figure(figsize=(10, 6))
    plt.plot(n_list, prim_mst_weights, marker='o', linestyle='-', color='b', label="weight")
    #plt.plot(n_list, kruskal_mst_weights, marker='o', linestyle='-', color='r', label="kruskal")
    Apery_const = zeta(3)
    plt.plot([0, n_list[-1]], [Apery_const, Apery_const], linestyle='--', c='gray')
    plt.xlabel('N-value')
    plt.ylabel('Mean weight of MST')
    plt.title('Mean weight of MST vs. N-value')
    plt.legend()
    plt.grid(True)

    save_path = f"./pic/weights.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Save the weights.png: {save_path}")