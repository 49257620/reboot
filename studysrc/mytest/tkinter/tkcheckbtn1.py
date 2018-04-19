# encoding: utf-8
# Author: LW

from tkinter import *


root = Tk()

OPTIONS = ['AA','BBB','CC','DDDD']
var = []

for x in OPTIONS:
    var.append(IntVar())
    chkbtn = Checkbutton(root,text=x,variable=var[-1])
    chkbtn.pack(anchor=W)
    # chkbtn.pack(side=LEFT)

root.mainloop()