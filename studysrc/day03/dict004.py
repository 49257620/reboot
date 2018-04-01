# encoding: utf-8
# author = ‘LW’
"""
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__',
 '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
 'pop', 'popitem', 'setdefault', 'update', 'values']

"""

me = {'name': 'll', 'age': 30, 'address': '中国北京'}

me_1 = me.copy()
# 清空字典
me.clear()

print(me)
print(me_1)
# pop 只少一个参数,key 不存在报错
print(me_1.pop('name'))
print(me_1.pop('name1', 'N/A'))

me.setdefault('tel', '132********')
print(me)

me.setdefault('tel', '186********')
print(me)

print(me.get('aaa', 'N/A'))

me['tel'] = None
print(me)

me = {'name': 'll', 'age': 30, 'address': '中国北京'}

for k, v in me.items():
    print('{0}:{1}'.format(k, v))

ll = [1, 2, 3, 4, 5, 6]

for x in enumerate(ll):
    print(x)

for k, v in enumerate(ll):
    print('{0}:{1}'.format(k, v))

my_dict = dict.fromkeys(['a', 'b', 'c'], 'NN')
print(my_dict)

# update
print('before update:', me)

me_update = {'age': 40, 'address': '上海', 'sex': 1}

me.update(me_update)
print('after update:', me)
