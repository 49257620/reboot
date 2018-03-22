# encoding: utf-8
"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
1.程序分析：谭浩强的书中答案有问题。　　　　　　
2.程序源代码：
"""
l = [7, 1, 4, 2, 9, 9, 3, 0, -1, 100]
print(max(l))
print(min(l))
print(l.index(9))
print(l[l.index(max(l))])
'''
l[0], l[l.index(max(l))] = l[l.index(max(l))], l[0]
l[len(l) - 1], l[l.index(min(l))] = l[l.index(min(l))], l[len(l) - 1]
'''
max_idx = l.index(max(l))
min_idx = l.index(min(l))

l[0], l[max_idx] = l[max_idx], l[0]
l[-1], l[min_idx] = l[min_idx], l[-1]

print(l)
