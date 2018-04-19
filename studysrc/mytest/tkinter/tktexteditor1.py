# encoding: utf-8
# Author: LW

from tkinter import *
import hashlib

root = Tk()

txt1 = Text(root , width=30,height=5)
txt1.pack()

txt1.insert(INSERT,'abcdeftghiklmnopqrstuvwxyz')
contents = txt1.get('1.0',END)


def getSig(contents):
    m = hashlib.md5(contents.encode())
    return  m.digest()

old_sig = getSig(contents)

def check():
    contents = txt1.get('1.0', END)
    if old_sig == getSig(contents):
        print('OK')
    else:
        print('NONO')

Button(root,text='检查',command=check).pack()


root.mainloop()