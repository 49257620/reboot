# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

Scale(root , from_=0,to_=42,tickinterval=5,resolution=5 ,length=200).pack()
Scale(root, from_=10 ,to_=120,tickinterval=10,resolution=10,length=600,orient=HORIZONTAL).pack()


root.mainloop()