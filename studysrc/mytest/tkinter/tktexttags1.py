# encoding: utf-8
# Author: LW

from tkinter import *


root = Tk()

txt1 = Text(root , width=30,height=5)
txt1.pack()

txt1.insert(INSERT,'abcdeftghiklmnopqrstuvwxyz')

txt1.tag_add('tag1','1.2','1.7','1.13')
txt1.tag_add('tag2','1.2','1.7','1.13')
txt1.tag_configure('tag1',background='yellow',foreground='red')
txt1.tag_configure('tag2',foreground='blue')



root.mainloop()