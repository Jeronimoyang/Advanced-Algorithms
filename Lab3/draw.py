import matplotlib.pyplot as plt
from mpmath import zeta

# --------------- 绘制 Prim 算法的运行时间随图规模变化的曲线 --------------- #
def draw_time(runtimes):
    n_list, runtimes = zip(*runtimes)
    plt.figure(figsize=(10, 6))
    plt.plot(n_list, runtimes, marker='o', linestyle='-', color='b', label="runtime")
    plt.xlabel('N-value')   
    plt.ylabel('Running Time (seconds)')
    plt.title('Running Time of Prim Algorithm vs. N-value') 
    plt.legend()
    plt.grid(True)

    save_path = f"./pic/runtime.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Save the runtime.png: {save_path}")

# --------------- 绘制 Prim 算法的 MST 权值随图规模变化的曲线 --------------- #
def draw_weights(mst_weights):
    n_list, mst_weights = zip(*mst_weights)
    plt.figure(figsize=(10, 6))
    plt.plot(n_list, mst_weights, marker='o', linestyle='-', color='b', label="mst_weights")
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