# encoding: utf-8
# Author: LW

from tkinter import *


def fn_callback():
    var.set("换了换了！")


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('重要的提示信息！\n我要换一行显示啦啦啦！')
root.title('label 和 图片')

label_1 = Label(frame1, textvariable=var, justify=LEFT)
label_1.pack(side=LEFT)

img_1 = PhotoImage(file='1.gif')
img_lable_1 = Label(frame1, image=img_1)
img_lable_1.pack(side=RIGHT)

my_btn = Button(frame2, text='点我换字', command=fn_callback)
my_btn.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

root.mainloop()
