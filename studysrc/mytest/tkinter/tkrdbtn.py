# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

v=IntVar()
v.set(3)

Radiobutton(root,text='ONE',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='TWO',variable=v,value=2).pack(anchor=W)
Radiobutton(root,text='THREE',variable=v,value=3).pack(anchor=W)



root.mainloop()