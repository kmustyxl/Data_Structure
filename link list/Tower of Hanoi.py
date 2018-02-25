# -*- coding:utf-8 -*-
def Hanoi(n,x,y,z):
    if n == 1:
        print(x+'-->'+z)
    else:
        Hanoi(n-1,x,z,y)
        print(x + '-->' + z)
        Hanoi(n-1,y,x,z)
Hanoi(3,'x','y','z')