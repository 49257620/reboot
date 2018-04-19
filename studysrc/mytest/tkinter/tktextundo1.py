# encoding: utf-8
# Author: LW

from tkinter import *
import hashlib

root = Tk()

txt1 = Text(root , width=30,height=5,undo=True)
txt1.pack()

txt1.insert(INSERT,'abcdeftghiklmnopqrstuvwxyzbcdf')

def undo1():
    txt1.edit_undo()

Button(root,text='撤销',command=undo1).pack()


root.mainloop()