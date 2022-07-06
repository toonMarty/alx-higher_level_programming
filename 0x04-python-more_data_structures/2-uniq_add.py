#!/usr/bin/python3
def uniq_add(my_list=[]):
    aux_list = []
    sums = 0
    for i in range(len(my_list)):
        if my_list[i] not in aux_list:
            aux_list.append(my_list[i])

    for i in range(len(aux_list)):
        sums += aux_list[i]
    return sums
