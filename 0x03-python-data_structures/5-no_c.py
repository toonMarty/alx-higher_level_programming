#!/usr/bin/python3
def no_c(my_string):
    str_to_list = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            str_to_list[i] = ''
    return ''.join(str_to_list)
