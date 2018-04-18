# encoding: utf-8
# Author: LW

import tkinter as tk

app = tk.Tk()
app.title('此处显示标题')

label1 = tk.Label(app, text='我的第一个窗口程序！')
label1.pack()

app.mainloop()
