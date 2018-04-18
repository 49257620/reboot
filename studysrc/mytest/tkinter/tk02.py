# encoding: utf-8
# Author: LW

import tkinter as tk


class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.hi_btn = tk.Button(frame, text='打招呼', bg='black', fg='white', command=self.say_hi)
        self.hi_btn.pack()

    def say_hi(self):
        print('大家好！！！')


root = tk.Tk()
root.title('窗口程序')

app = APP(root)

root.mainloop()
