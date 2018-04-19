# encoding: utf-8
# Author: LW

from tkinter import *
import webbrowser


root = Tk()

txt1 = Text(root , width=30,height=5)
txt1.pack()

txt1.insert(INSERT,'abcdeftghiklmnopqrstuvwxyz')

txt1.tag_add('link','1.2','1.9')

txt1.tag_config('link',foreground='red',underline=True)

def mouse_in(event):
    txt1.config(cursor='arrow')

def mouse_out(event):
    txt1.config(cursor='xterm')

def r1_click(event):
    webbrowser.open('http://www.baidu.com')

txt1.tag_bind('linl','<Enter>',mouse_in)
txt1.tag_bind('link','<Leave>',mouse_out)
txt1.tag_bind('link','<Button-1>',r1_click)

root.mainloop()