#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return 0, 0

    elif len(tuple_a) == 0 and len(tuple_b) < 2:
        for i in range(len(tuple_b)):
            new_tuple = (int(tuple_b[i]), 0)
            return new_tuple

    elif len(tuple_b) == 0 and len(tuple_a) < 2:
        for i in range(len(tuple_a)):
            new_tuple = (int(tuple_a[i]), 0)
            return new_tuple

    elif len(tuple_a) < 2 and len(tuple_b) < 2:
        for i in range(len(tuple_a)):
            for j in range(len(tuple_b)):
                new_tuple = (int(tuple_a[i]) + int(tuple_b[j]), 0)
                return new_tuple

    elif len(tuple_a) == 0:
        for j in range(len(tuple_b)):
            new_tuple = (0 + int(tuple_b[j]), 0 + int(tuple_b[j + 1]))
            return new_tuple

    elif len(tuple_b) == 0:
        for i in range(len(tuple_a)):
            new_tuple = (int(tuple_a[i]) + 0, int(tuple_a[i + 1]) + 0)
            return new_tuple

    elif len(tuple_a) < 2:
        for i in range(len(tuple_a)):
            for j in range(len(tuple_b)):
                new_tuple = (int(tuple_a[i]) + int(tuple_b[j]),
                             0 + int(tuple_b[i + 1]))
                return new_tuple

    elif len(tuple_b) < 2:
        for i in range(len(tuple_a)):
            for j in range(len(tuple_b)):
                new_tuple = (int(tuple_a[i]) + int(tuple_b[j]),
                             int(tuple_a[i + 1]) + 0)
                return new_tuple
