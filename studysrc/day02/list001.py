# encoding: utf-8
"""
list 基本操作

"""
nums = [1, 'ww', 3, 4, .5, 5.]

print(nums)
print(type(nums))
# 访问元素
print(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
print(nums[-1], nums[-2], nums[-3], nums[-4], nums[-5], nums[-6])
print(nums[::3])

# 修改
nums[-1] = 10
print('mod', nums)

# 删除
del nums[1]
print('del', nums)

# 遍历元素
print('******************list 遍历元素******************')
for i in nums:
    print(i)

# 字符串转换列表
print('******************字符串转换列表******************')
print(list('abcdefg123456'))

# list 转 bool
print('******************list 转 bool******************')
print(bool([1, 2]))
print(bool([]))

# list 转 int
# int() argument must be a string, a bytes-like object or a number, not 'list'
# print(int([1, 2]))

# list 转 string
print('******************list  转 string******************')
print(str([1, 2, 'ww']))
print(list("[1, 2, 'ww']"))

# list 四则运算
print('******************list 四则运算******************')
print([1, 2, 3] + ['a', 'b', 'c'])
print(['a', 'b', 'c'] * 4)

# range生成list
print('******************range生成list******************')
print(list(range(10)))
print(list(range(6, 10)))
print(list(range(0, 10, 3)))
print('双数:', list(range(0, 10, 2)))
print('单数:', list(range(1, 10, 2)))
print('倒序:', list(range(9, -1, -1)))

# list长度 最大值 最小值 和
print('******************list长度 最大值 最小值 和******************')
nums = [1, 66, 3, 4, .5, 5.]
print('长度:', len(nums))
print('最大:', max(nums))
print('最小:', min(nums))
print('总数:', sum(nums))

sum_nums = 0

for i in nums:
    sum_nums += i
print('总数:', sum_nums, '平均数:', sum_nums / len(nums))

# list查找是否存在在list中
print('******************list查找是否存在在list中******************')
chk = 66
for i in nums:
    if i == chk:
        print('遍历判断: True')
        break
print('链表推导式方法:', list(x for x in nums if x == chk))
print('in 方法:', chk in nums)

