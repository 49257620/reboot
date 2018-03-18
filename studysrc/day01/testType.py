# encoding utf-8

print(type(1))
print(type(1.0))
print(type(''))

name = 'Liu wei'
age = 30
desc = 'My name is ' + name + ' and I am ' + str(age) + ' years old.'

print(type(name))

print(int('1'))
print(int(1.1))
print(float(1))
print(float('1'))
print(float('1.1'))

print(str(1))
print(str(1.1))
print(str(name))

print(desc)

name = input('请输入名字:')
age = input('请输入年龄:')

desc = 'My name is ' + name + ' and I am ' + age + ' years old.'

print(desc)
