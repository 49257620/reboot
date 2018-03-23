# encoding: utf-8
"""
【程序97】
题目：文件写入。
1.程序分析：　　　　　
2.程序源代码：
"""

str = """你好，测试
换行回车
在写一行！"""

fp = open("C:/test.txt", 'w',-1,'utf-8')
fp.write(str)
fp.close()
