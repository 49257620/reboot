# encoding utf-8

x = 1
y = 1

while x < 10:
    y = 1
    while y <= x:
        space = '';
        if x * y < 10:
            space = ' '
        print(str(x) + ' * ' + str(y) + ' =' + space + str(x * y), end='  ')
        y += 1
    print()
    x += 1
