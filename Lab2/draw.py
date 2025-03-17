import matplotlib.pyplot as plt

# --------------- 绘制 k 值对三种算法运行时间的关系图 --------------- #
def draw_k_time(Fsts_time, Linear_time, Lazy_time):
    K_list, fsts_time = zip(*Fsts_time)
    K_list, linear_time = zip(*Linear_time)
    K_list, lazy_time = zip(*Lazy_time)
    plt.figure(figsize=(10, 6))
    plt.plot(K_list, fsts_time, marker='o', linestyle='-', color='b', label="Fsts Time")
    plt.plot(K_list, linear_time, marker='o', linestyle='-', color='r', label="Linear Time")
    plt.plot(K_list, lazy_time, marker='o', linestyle='-', color='g', label="Lazy Select Time")
    plt.xlabel('K-value')   # X轴标签
    plt.ylabel('Running Time (seconds)')     # Y轴标签
    plt.title('Running Time vs. K-value')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = f"./pic/k_runtime.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the k_runtime.png: {save_path}")

# --------------- 绘制 k 值对算法准确率的关系图 --------------- #
def draw_k_accuracy(Accuracy):
    K_list, accuracy = zip(*Accuracy)
    plt.figure(figsize=(10, 6))
    plt.plot(K_list, accuracy, marker='o', linestyle='-', color='b', label="Accuracy")
    plt.xlabel('K-value')   # X轴标签
    plt.ylabel('Accuracy of Lazy Select')     # Y轴标签
    plt.title('Accuracy of Lazy Select vs. K-value')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = f"./pic/k_accuracy.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the k_accuracy.png: {save_path}")

# --------------- 绘制 lazySelect 随机算法中的关键参数对运行时间的关系图 --------------- #
def draw_theta_time(Lazy_time):
    Theta_list, lazy_time = zip(*Lazy_time)
    plt.figure(figsize=(10, 6))
    plt.plot(Theta_list, lazy_time, marker='o', linestyle='-', color='b', label="Lazy Select Time")
    plt.xlabel('Theta-value')   # X轴标签
    plt.ylabel('Running Time (seconds)')     # Y轴标签
    plt.title('Running Time vs. Theta-value')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = f"./pic/theta_runtime.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the theta_runtime.png: {save_path}")

# --------------- 绘制 lazySelect 随机算法中的关键参数对准确率的关系图 --------------- #
def draw_theta_accuracy(Accuracy):
    Theta_list, accuracy = zip(*Accuracy)
    plt.figure(figsize=(10, 6))
    plt.plot(Theta_list, accuracy, marker='o', linestyle='-', color='b', label="Accuracy")
    plt.xlabel('Theta-value')   # X轴标签
    plt.ylabel('Accuracy of Lazy Select')     # Y轴标签
    plt.title('Accuracy of Lazy Select vs. Theta-value')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = f"./pic/theta_accuracy.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the theta_accuracy.png: {save_path}")