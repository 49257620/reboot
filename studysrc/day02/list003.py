# encoding: utf-8
# author = ‘LW’

"""
list 基本操作- 切片
切片用于复制list
"""
# 切片是一个全新的list，不是原list的引用
# 引用实例 l1 == l3
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1
print(l1 == l2, l1 == l3)
# 修改l1 导致 l3数据变化，说明l1与l3引用统一地址
l1[1] = 0

print(l1, l2, l3)
print(l1 == l2, l1 == l3)

# 切片操作
print('******************list切片操作******************')
ll = list(range(10))
print('原始：', ll)
print('反转：', ll[::-1])
print('奇数：', ll[1::2])
print('偶数：', ll[::2])
print('奇数反向：', ll[::-2])
print('偶数反向：', ll[-2::-2])

# 切片修改原list
print('******************切片修改原list******************')
ll[1:3] = ['a', 'b', 'c']
ll[1:1] = [11, 22, 33]
ll[1:7] = []
print(ll)
print(id(ll),id(ll[1:3]))
