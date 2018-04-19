# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

v = StringVar()


def test():
    if e1.get() == 'lw':
        print('ok')
        return True
    else:
        print('no')
        e1.delete(0, END)
        return False

def test2():
    print('hahaha')
    return  True

e1 = Entry(root, textvariable=v, validate='focusout', validatecommand=test,invalidcommand=test2)
e1.pack()
e2 = Entry(root)
e2.pack()

root.mainloop()
