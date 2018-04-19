# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

lb = Listbox(root)
lb.pack()

for x in ['aaa','bbb','ccc','ddd']:
    lb.insert(END,x)

lb.delete(1)

btn1 = Button(root,text='删除',command=lambda x=lb:x.delete(ACTIVE))
btn1.pack()

root.mainloop()