# encoding: utf-8
# Author: LW

from tkinter import *


root = Tk()

text_1 = Text(root,width=30,height=5)
text_1.pack()

text_1.insert(INSERT,'I love \n')
text_1.insert(END,'XXXXXXXX')


root.mainloop()