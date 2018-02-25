# -*- coding:utf-8 -*-
init_card = [0 for i in range(13)]
init_card[0] = 1 #The first card is 1
next_number = 2 #The number needed to count that after the first card
pos = 0 #The location of current card
for i in range(1,13):
    count_number = 0
    while count_number < next_number:
        if init_card[(pos + 1)%len(init_card)] == 0:
            count_number += 1
            pos = (pos + 1) % len(init_card)
        else:
            pos = (pos + 1) % len(init_card)
    init_card[pos] = next_number
    next_number += 1

print(init_card)
