#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        print('0{}, '.format(i), end='')
    elif 99 >= i > 9:
        print('{}, '.format(i), end='')
