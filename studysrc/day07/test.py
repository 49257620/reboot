# encoding: utf-8
# Author: LW


r = [[1], [2, 3], [4, 5, 6]]
r1 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

def my_fun(r):
    while len(r) > 1:
        sub_list = [r.pop(0)]
        sub_list.append(r.pop(0))
        result_list = []
        for x in sub_list[0]:
            for y in sub_list[1]:
                templist = []
                if type(x) == int:
                    templist.append(x)
                else:
                    templist.extend(x)
                templist.append(y)
                result_list.append(templist)
        r.insert(0, result_list)
    return r[0]


print(my_fun(r))
print(my_fun(r1))
"""
result_list = []

for x in r[0]:
    for y in r[1]:
        templist = []
        templist.append(x)
        templist.append(y)
        result_list.append(templist)

print(result_list)

for x in result_list:
    for y in r[2]:
        templist = []
        templist.extend(x)
        templist.append(y)
        print(templist)

"""

"""
result_list = r[0]
for x in result_list:
    for y in r[1]:
        tmplist = []
        tmplist.append(x)
        tmplist.append(y)
        result_list.append(tmplist)
print(result_list)
"""
"""
for x in range(len(r)):
    for y in range(len(r[x])):
        print('-'*10,x,y,'-'*10)
        
"""
