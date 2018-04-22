# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’


def fun_factorial(num):
    if num < 0:
        return None
    result = 1
    for x in range(1, num + 1):
        result *= x
    return result


print(fun_factorial(-1))
print(fun_factorial(0))
print(fun_factorial(5))


def fun_factorial_recursion(num):
    return num * fun_factorial_recursion(num - 1) if num > 0 else 1 if num == 0 else None


print(fun_factorial_recursion(-1))
print(fun_factorial_recursion(0))
print(fun_factorial_recursion(5))
