#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        number = -number
    a = number % 10
    if a < 0:
        a = -a

    print(a, end='')
    return a
