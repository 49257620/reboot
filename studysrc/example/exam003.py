# encoding: utf-8
"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
　　　　　　的结果满足如下条件，即是结果。请看具体分析：
2.程序源代码：
"""
import math

for i in range(200):
    x = math.sqrt(i + 100)
    y = math.sqrt(i + 168)
    if x == math.floor(x) and y == math.floor(y):
        print(i)

print(math.sqrt(156 + 100))
print(math.sqrt(156 + 168))
