# encoding: utf-8
# Author: LW

class Ractangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        if name == "s":
            self.x = value
            self.y = value
        else:
            super().__setattr__(name, value)

    def getArea(self):
        return self.x * self.y



a = Ractangle(4,5)

a.s = 10
a.x = 20

print(a.getArea())

a.s = 100

a.a = 100
print(a.__dict__)
print(a.getArea())