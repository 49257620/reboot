# encoding: utf-8
# Author: LW

data =  {}

data[('192,168.0,1','/fffffff.html','200')] = data.setdefault(('192,168.0,1','/fffffff.html','200'),0)+1

print(data)

