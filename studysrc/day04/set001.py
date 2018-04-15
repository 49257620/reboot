# encoding: utf-8
# author = ‘LW’

nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]
print('数据1：', nums_1)
print('数据2：', nums_2)
print('交集 &：', list(set(nums_1) & set(nums_2)))
print('并集 |：', list(set(nums_1) | set(nums_2)))
print('差集 -：', list(set(nums_1) - set(nums_2)))
print('对差集 ^：', list(set(nums_1) ^ set(nums_2)))
