#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)).__reversed__():
        print("{}".format(my_list[i]))
