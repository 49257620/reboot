# encoding: utf-8
# Author: LW

from tkinter import *


root = Tk()

text_1 = Text(root,width=30,height=60)
text_1.pack()

text_1.insert(INSERT,'I love \n')
text_1.insert(END,'XXXXXXXX')

img_1= PhotoImage(file='1.gif')


def show():
    text_1.image_create(END,image=img_1)
btn1 = Button(text_1,text='点我',command=show)

text_1.window_create(INSERT,window=btn1)



root.mainloop()