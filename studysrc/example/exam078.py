# encoding: utf-8
"""
【程序78】
题目：找到年龄最大的人，并输出。请找出程序中有什么问题。dict 最大最小问题
1.程序分析：
2.程序源代码
"""

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

print(person.items())
print(person.keys())
print(person.values())

print(max(zip(person.keys(),person.values())))
print(max(zip(person.values(),person.keys())))

print(min(person.items(), key=lambda x: x[1]))
print(min(person.items()))
print(max(person.items(), key=lambda x: x[1]))
print(max(person.items()))

