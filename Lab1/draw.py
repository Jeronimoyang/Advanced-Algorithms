import matplotlib.pyplot as plt

# --------------- 求解相似度 --------------- #
def jaccard_similarity(s1: set, s2: set) -> float:
    return len(s1 & s2) / len(s1 | s2)

# --------------- 绘制哈希函数数量与运行时间关系图 --------------- #
def draw_time(results_time):
    hash_funcs_list, times = zip(*results_time)
    plt.figure(figsize=(10, 6))
    plt.plot(hash_funcs_list, times, marker='o', linestyle='-', color='b', label="MinHash Running Time")
    plt.xlabel('Number of Hash Functions')   # X轴标签
    plt.ylabel('Running Time (seconds)')     # Y轴标签
    plt.title('MinHash Running Time vs. Number of Hash Functions')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = "./pic/minhash_runtime.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the minhash_runtime.png: {save_path}")

# --------------- 绘制哈希函数数量与相似度关系图 --------------- #
def draw_sim(results_sim):
    hash_funcs_list, sims = zip(*results_sim)
    plt.figure(figsize=(10, 6))
    plt.plot(hash_funcs_list, sims, marker='o', linestyle='-', color='b', label="MinHash Running Time")
    plt.xlabel('Number of Hash Functions')   # X轴标签
    plt.ylabel('Jaccard Similarity of MinHash and Naive')     # Y轴标签
    plt.title('Jaccard Similarity of MinHash and Naive vs. Number of Hash Functions')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = "./pic/minhash_similarity.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the minhash_similarity.png: {save_path}")