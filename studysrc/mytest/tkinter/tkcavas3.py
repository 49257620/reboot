# encoding: utf-8
# Author: LW


from tkinter import *


root = Tk()

w = Canvas(root,width=200,height=100)
w.pack()

line1 = w.create_line(0,0,200,100,fill='green',width=3)
line2 = w.create_line(0,100,200,0,fill='green',width=3)
rect1 = w.create_rectangle(40,20,160,80,fill='green')
rect1 = w.create_rectangle(65,35,135,65,fill='yellow')

w.create_text(100,50,text='TEST')

root.mainloop()