import matplotlib.pyplot as plt

def draw_time_cost(ew_time, eo_time, oe_time):
    sample_num, ew_time_cost = zip(*ew_time)
    sample_num, eo_time_cost = zip(*eo_time)
    sample_num, oe_time_cost = zip(*oe_time)
    plt.figure(figsize=(10, 6))
    plt.plot(sample_num, ew_time_cost, marker='o', linestyle='-', color='b', label="Exact Weight")
    plt.plot(sample_num, eo_time_cost, marker='o', linestyle='-', color='r', label="Extended Olken")
    plt.plot(sample_num, oe_time_cost, marker='o', linestyle='-', color='g', label="Online Exploration")
    plt.xlabel('Sample Num')   # X轴标签
    plt.ylabel('Time Cost (s)')     # Y轴标签
    plt.title('Sample Num vs. Time Cost (s)')  # 图像标题
    plt.legend()
    plt.grid(True)
    
    save_path = f"./pic/runtime.png"  # 可修改保存路径
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # dpi=300 提高清晰度
    print(f"Save the runtime.png: {save_path}")