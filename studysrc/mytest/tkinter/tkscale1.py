# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

Scale(root , from_=0,to_=42).pack()
Scale(root, from_=10 ,to_=120,orient=HORIZONTAL).pack()


root.mainloop()