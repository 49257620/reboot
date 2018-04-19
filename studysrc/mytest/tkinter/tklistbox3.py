# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

lb = Listbox(root,height=20)
lb.pack()

for x in range(30):
    lb.insert(END,x)


btn1 = Button(root,text='删除',command=lambda x=lb:x.delete(ACTIVE))
btn1.pack()

root.mainloop()