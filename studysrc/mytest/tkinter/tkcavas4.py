# encoding: utf-8
# Author: LW


from tkinter import *


root = Tk()

w = Canvas(root,width=200,height=100)
w.pack()


rect1 = w.create_rectangle(40,20,160,80,dash=(4,4))
w.create_oval(40,20,160,80,fill='yellow')


w.create_text(100,50,text='TEST')

root.mainloop()