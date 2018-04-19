# encoding: utf-8
# Author: LW


from tkinter import *
import math as m

root = Tk()

w = Canvas(root,width=200,height=100)
w.pack()


x = 100
y = 50
r = 40
r1 = int(r * m.sin(2*m.pi/5))
r2 = int(r * m.cos(2*m.pi/5))

r3 = int(r * m.sin(m.pi/5))
r4 = int(r * m.cos(m.pi/5))

pos =[
    x - r1,
    y - r2,
    x + r1,
    y - r2,
    x - r3,
    y + r4,
    x,
    y - r,
    x + r3,
    y + r4
]

w.create_polygon(pos,outline='green',fill='yellow')

root.mainloop()