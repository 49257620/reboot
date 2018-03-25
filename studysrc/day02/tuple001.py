# encoding: utf-8
# author = ‘LW’
"""
元祖 ：不可变列表
"""

# 一个元素的元组
print('(1):', type((1)), '(1,):', type((1,)), '():', type(()))

# 元组不可变
a = (1, 2, 3,)
# a[0] = 10 # TypeError: 'tuple' object does not support item assignment

# 元组切片
print(a[0:2])
# a[0:0] = 10 # 不可以修改

# 元组转换
print('元组转字符串', str(a))
print('元组转list', list(a))
print('list转元组', tuple([1, 2, 3]))
print('(1, 2, 3,)转布尔:', bool(a))
print('()转布尔:', bool(()))
# print('布尔转元组:', tuple(True))
print('字符串转元组：', tuple('abcdf'))

# 方法
print('元组长度:', len(a))
print('元组最大:', max(a))
print('元组最小:', min(a))
print('元组总数:', sum(a))

# 运算
print('元组乘法:', a * 3)
print('元组加法:', a + a)
# print('元组减法:', a-a)


# 遍历
for i in a:
    print('遍历元组 a :', i)
