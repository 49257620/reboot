# encoding: utf-8
"""
【程序66】
题目：输入3个数a,b,c，按大小顺序输出。　　　
1.程序分析：利用指针方法。
2.程序源代码：
"""
a, b, c = 8, 1, 0

if a >= b:
    a, b = b, a
if a >= c:
    a, c = c, a
if b >= c:
    b, c = c, b

print(a, b, c)

l = [5,5,8,10,1,3,7,20,0,100]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] >= l[j]:
            l[i],l[j] = l[j],l[i]

print(l)