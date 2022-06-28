#!/usr/bin/python3
for n in range(48, 57):
    for m in range(49, 58):
        if m > n:
            print('{}{}'.format(chr(n), chr(m)), end='')
            if n != 56 or m != 57:
                print(f', ', end='')
