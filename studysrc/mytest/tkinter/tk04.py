# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()

img1 = PhotoImage(file='1.gif')
label1 = Label(root,
               text='测试内容内容\n换行内容内容',
               justify=LEFT,
               image=img1,
               compound=CENTER,
               font=('微软雅黑', 20),
               fg='white')

label1.pack()

mainloop()
