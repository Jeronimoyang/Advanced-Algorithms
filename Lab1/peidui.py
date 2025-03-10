pairs = [
    (63, 439),  (421, 222),
    (275, 427),
    (275, 356), (275, 381),
    (356, 381), (356, 427),
    (381, 427), 
    (73, 445),
]

# 用集合去除重复配对
unique_pairs = set()

for pair in pairs:
    # 对每对配对进行排序，确保只保留一个方向的配对
    sorted_pair = tuple(sorted(pair))
    unique_pairs.add(sorted_pair)

# 输出去重后的配对
for pair in unique_pairs:
    print(pair)
