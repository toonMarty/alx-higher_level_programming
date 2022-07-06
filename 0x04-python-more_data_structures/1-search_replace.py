#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if search == my_list[i]:
            new_list.remove(search)
            new_list.insert(i, replace)
    return new_list
