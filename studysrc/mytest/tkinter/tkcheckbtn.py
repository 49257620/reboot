# encoding: utf-8
# Author: LW

from tkinter import *


root = Tk()

v = IntVar()
v.set(1)

c = Checkbutton(root , text='测试一下', variable=v)

c.pack()

l = Label(root,textvariable=v)

l.pack()

root.mainloop()