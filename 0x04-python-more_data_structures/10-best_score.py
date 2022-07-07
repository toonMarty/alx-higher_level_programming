#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        key_sort = list(a_dictionary.values())
        key_sort.sort()
        a = key_sort[len(key_sort) - 1]
        for key in a_dictionary:
            if a == a_dictionary[key]:
                return key

