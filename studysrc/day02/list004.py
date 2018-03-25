# encoding: utf-8
# author = ‘LW’
"""
1.找出 nums=[6, 11, 7, 9, 4, 2, 1]中最大的数字
2.排序
"""
# 方法一， 使用max获取最大值 ，直接交换
nums = [6, 11, 7, 9, 4, 2, 1]

nums[nums.index(max(nums))], nums[-1] = nums[-1], nums[nums.index(max(nums))]
print('**********方法一， 使用max获取最大值 ，直接交换**********')
print(nums)

# 方法二， 遍历，然后两两比较
nums = [6, 11, 7, 9, 4, 2, 1]

for idx in range(0, len(nums) - 1):
    if nums[idx] > nums[idx + 1]:
        nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
print('**********方法二， 遍历，然后两两比较**********')
print(nums)

# 排序-冒泡排序

nums = [6, 11, 7, 9, 4, 2, 1]

for j in range(len(nums) - 1):
    for idx in range(len(nums) - 1 - j):
        if nums[idx] > nums[idx + 1]:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
print('**********排序-冒泡排序**********')
print(nums)
