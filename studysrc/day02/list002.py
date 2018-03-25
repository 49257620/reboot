# encoding: utf-8
# author = ‘LW’
"""
练习：最大的元素是谁和他对应的索引是多少
"""

nums = [5, 8, 7, 10, 20, 2, 6, 9]

# 获取最大值及index
max_val = 0
max_idx = 0
idx = 0
for i in nums:
    if i > max_val:
        max_val = i
        max_idx = idx
    idx += 1

print('1 max value:', max_val, 'max index:', max_idx)

# 不保存最大值，仅记录index，使用index获取值再进行判断
max_idx = 0
idx = 0
for i in nums:
    if i > nums[max_idx]:
        max_idx = idx
    idx += 1

print('2 max value:', nums[max_idx], 'max index:', max_idx)

# 使用len判断长度,以len为索引进行循环遍历，以index进行取值
max_val = 0
max_idx = 0
for i in range(len(nums) - 1):
    if nums[i] > max_val:
        max_val = nums[i]
        max_idx = i

print('3 max value:', max_val, 'max index:', max_idx)
