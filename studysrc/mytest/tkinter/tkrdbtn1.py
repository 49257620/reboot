# encoding: utf-8
# Author: LW

from tkinter import *

LANG = [('java',1),
        ('C++',2),
        ('Python',3),
        ('PHP',4)]
root = Tk()

v=IntVar()
v.set(1)
# indicatoron=False  取消圆点改为按钮
# anchor=W 左对齐
# fill=X 横向填充
for x,y in LANG:
    Radiobutton(root, text=x, variable=v, value=y,indicatoron=False).pack(anchor=W,fill=X)



root.mainloop()