# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

scr_bar = Scrollbar(root)
scr_bar.pack(side=RIGHT,fill=Y)

lb = Listbox(root,yscrollcommand=scr_bar.set)
lb.pack(side=LEFT,fill=BOTH)


for x in range(300):
    lb.insert(END,x)

scr_bar.config(command=lb.yview)





root.mainloop()