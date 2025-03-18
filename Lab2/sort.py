# 定义 MergeSort 类，实现归并排序算法
class MergeSort:
    # --------------- 构造函数 --------------- #
    def __init__(self):
        # 不执行任何操作
        pass
    
    # --------------- 静态方法，不依赖 self --------------- #
    @staticmethod
    # 合并两个有序数组
    def merge(list_left, list_right):
        # 初始化左右指针
        l, r = 0, 0
        # 初始化新列表，用于存储合并后的有序数组
        new_list = []
        # 循环遍历左右两个有序数组，直到其中一个数组处理完毕
        while l < len(list_left) and r < len(list_right):
            # 比较左右两个数组的当前元素，将较小的元素添加到新列表中
            if list_left[l] <= list_right[r]:
                new_list.append(list_left[l])
                # 左指针右移
                l += 1
            else:
                new_list.append(list_right[r])
                # 右指针右移
                r += 1
        # 将剩余元素添加到新列表中
        new_list += list_left[l:]
        new_list += list_right[r:]
        # 返回合并后的有序数组
        return new_list

    # --------------- 运行函数 --------------- #
    def run(self, mylist):
        # 如果数组长度小于等于1，直接返回
        if len(mylist) <= 1:
            return mylist
        # 计算数组中间位置，用于分割数组成左右两部分
        mid = len(mylist) // 2
        # 递归调用 run 函数，对左部分数组进行排序
        list_left = self.run(mylist[:mid])
        # 递归调用 run 函数，对右部分数组进行排序
        list_right = self.run(mylist[mid:])
        # 返回合并后的有序数组
        return self.merge(list_left, list_right)