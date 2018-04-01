# encoding: utf-8
# author = ‘LW’


me = {'name': 'll', 'age': 30, 'address': '中国北京'}

print('原始：', me)
me['sex'] = '男'
print('修改：', me)

del me['sex']
print('删除：', me)

for k in me:
    print('{0}:{1}'.format(k, me[k]))

me_list = [('name', 'lll'), ('age', 30), ('tel', '138000000xxxxx')]
print('list转dict：', dict(me_list))

print('直接生成dict：', dict(name='llll', age=29, sex=1))

# len max min in
print('len:', len(me))
print('max:', max(me))
print('min:', min(me))
print('in :', 'age' in me)
