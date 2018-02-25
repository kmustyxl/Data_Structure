# -*- coding:utf-8 -*-
#主要利用冲突函数检测冲突，如果冲突则回溯，递归用到python的yield语句，该语句涉及python的生成器。
def conflict(state, col):
    #冲突函数, row=行, col=列
    row = len(state)
    for i in range(row):
        if abs(state[i] - col) in (0, row - i):
            return True
    return False

def queens(num=8, state=()):
    #生成器函数
    for pos in range(8):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result
for solution in queens():
    print(solution)
