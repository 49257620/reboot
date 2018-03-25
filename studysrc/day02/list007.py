# encoding: utf-8
# author = ‘LW’
"""
获取两个list中相同的元素到第三个列表中
保证第二个练习中第三个列表中元素不重复

"""
nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]
nums = []
for i in nums_1:
    if i in nums_2 and i not in nums:
        nums.append(i)

print(nums)