# encoding: utf-8
"""
【程序22】
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
　　　比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出
　　　三队赛手的名单。
1.程序分析：　　　　　
2.程序源代码：
"""

for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        for k in range(ord('x'), ord('z') + 1):
            if (i != j) and (j != k) and (i != k):
                if i == ord('x') or k == ord('x') or k == ord('z'):
                    continue
                else:
                    print('a -', chr(i), ' b -', chr(j), ' c -', chr(k))
