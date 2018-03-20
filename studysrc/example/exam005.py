# encoding: utf-8
"""
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
2.程序源代码：
"""
'''

x = int(input('please input x :'))
y = int(input('please input y :'))
z = int(input('please input z :'))


n = x

if x > y:
    n = x
    x = y
    y = n

if x > z:
    n = x
    x = z
    z = n

if y > z:
    n = y
    y = z
    z = n

print(x, y, z)
'''
l = []
for i in range(3):
    l.append(int(input('please input a number :')))

l.sort()
print(l)
