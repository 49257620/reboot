# encoding: utf-8
# Author: LW

from tkinter import *



LANG = [('java',1),
        ('C++',2),
        ('Python',3),
        ('PHP',4)]
root = Tk()

group = LabelFrame(root,text='请选择语言:' ,padx=5,pady=5)
group.pack(padx=10,pady=10)

v=IntVar()
v.set(1)
# indicatoron=False  取消圆点改为按钮
# anchor=W 左对齐
# fill=X 横向填充
for x,y in LANG:
    Radiobutton(group, text=x, variable=v, value=y).pack(anchor=W)



root.mainloop()