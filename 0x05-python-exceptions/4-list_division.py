#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = max(my_list_1, my_list_2)
    for i in range(list_length):
        try:
            res[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
            res[i] = 0
        except ZeroDivisionError:
            print('division by 0')
            res[i] = 0
        except IndexError:
            print('out of range')
        finally:
            res[len(res) - 1] = 0

    return res
