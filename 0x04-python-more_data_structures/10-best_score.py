#!/usr/bin/python3
def best_score(a_dictionary):
    for key in a_dictionary:
        if key in a_dictionary:
            key_sort = list(a_dictionary)
            key_sort.sort()
            return key_sort[len(key_sort) - 1]
        else:
            return None
