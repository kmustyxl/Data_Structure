# -*- coding:utf-8 -*-
def Fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return Fib(n-1) + Fib(n-2)
