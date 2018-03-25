# encoding: utf-8
# author = ‘LW’
"""
list 相关函数
"""

# append
ll = list(range(10))

print('原始：', ll)
ll.append(10)
ll.append('x')
ll.append('xyx')  # 以一个元素放入list中
print('append后：', ll)

# extend
ll.extend([13, 14, 15])
ll.extend('x')
ll.extend('xyz')  # 遍历字符串 作为多个元素extend到list中

print('extend后：', ll)

# clear
print("清除前：", ll, id(ll))
ll.clear()
print("清除后：", ll, id(ll))

# copy
ll = list(range(10))
ll_eq = ll
ll_copy = ll.copy()
ll_copy1 = ll[:]
print("复制list对象 :", id(ll), id(ll_eq), id(ll_copy), id(ll_copy1))

# count index
print('count:', ll.count(4), 'index:', ll.index(4))
ll.append(4)
print('count:', ll.count(4), 'index:', ll.index(4))
print('count:', ll.count(100))

# pop
print('before pop:', ll)
ll.pop()
ll.pop(0)
print('after pop:', ll)

# remove
ll.append(4)
print('before remove:', ll)
ll.remove(4)
print('after remove:', ll)
# ll.remove(100) #list.remove(x): x not in list

# reverse
print('before reverse:', ll)
ll.reverse()
print('after reverse:', ll)

# sort
ll.append(4)
print('before sort:', ll)
ll.sort()
print('after sort 正序:', ll)
ll.sort(reverse=True)
print('after sort 倒序:', ll)
