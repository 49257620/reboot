# encoding: utf-8
# Author: LW

mylist = [1,2,3,4,5,6,7,8]

def myfun():
    mylist.pop()
    mylist.append(10)

myfun()
print(mylist)