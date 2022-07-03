#!/usr/bin/python3
def remove_char_at(str, n):
    str_to_list = list(str)
    for i in range(len(str)):
        if i == n:
            str_to_list[i] = ''
    return ''.join(str_to_list)
