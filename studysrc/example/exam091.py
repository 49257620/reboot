# encoding: utf-8
"""
 【程序91】
题目：时间函数举例1
1.程序分析：
2.程序源代码：
"""

import time

print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))


start = time.time()
for i in range(1):
    print(i+1)
    time.sleep(1)
    end = time.time()

print(end - start)

print('*'*20)

start = time.clock()
print(start)
for i in range(5):
    print(i+1)
    time.sleep(0.5)
end = time.clock()
print('different is %6.3f' % (end - start))