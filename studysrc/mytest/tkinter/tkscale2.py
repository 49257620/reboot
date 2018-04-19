# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

s1 = Scale(root , from_=0,to_=42)
s1.pack()
s2 = Scale(root, from_=10 ,to_=120,orient=HORIZONTAL)
s2.pack()

def show():
    print(s1.get(),s2.get())
Button(root,text='打印位置',command=show).pack()

root.mainloop()