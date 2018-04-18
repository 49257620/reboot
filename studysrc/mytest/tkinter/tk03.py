# encoding: utf-8
# Author: LW

from tkinter import *

root = Tk()
root.title('label 和 图片')

label_1 = Label(root, text='重要的提示信息！\n我要换一行显示啦啦啦！', justify=LEFT, padx=10)
label_1.pack(side=LEFT)

img_1 = PhotoImage(file='1.gif')
img_lable_1 = Label(root, image=img_1)
img_lable_1.pack(side=RIGHT)

root.mainloop()
