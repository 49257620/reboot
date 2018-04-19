# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

lb = Listbox(root)
lb.pack()

lb.insert(0,'haha')
lb.insert(1,'hehe')
lb.insert(END,'xixi')



root.mainloop()