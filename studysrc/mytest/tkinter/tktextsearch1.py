# encoding: utf-8
# Author: LW

from tkinter import *
import hashlib

root = Tk()

txt1 = Text(root , width=30,height=5)
txt1.pack()

txt1.insert(INSERT,'abcdeftghiklmnopqrstuvwxyzbcdf')
contents = txt1.get('1.0',END)

strart = 1.0

while True:
    pos = txt1.search('5', strart, END)
    if not pos:
        break
    print('pos:',pos)
    strart = pos + '+1c'



root.mainloop()