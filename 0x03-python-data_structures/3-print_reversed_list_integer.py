#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    str = "{}"
    for i in range(len(my_list)).__reversed__():
        print(str.format(my_list[i]))
