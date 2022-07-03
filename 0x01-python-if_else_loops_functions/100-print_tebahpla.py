#!/usr/bin/python3
for i in range(97, 123).__reversed__():

    if i % 2 == 0:
        print('{}'.format(chr(i)), end='')
    if i % 2 == 1:
        print('{}'.format(chr(i).upper()), end='')
