#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict =\
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0

    for i in range(len(roman_string)):
        for key in roman_dict:
            if roman_string[i] == key:
                val += roman_dict[key]
                if i != len(roman_string) - 1:
                    if roman_string[i] < roman_string[i + 1] and \
                            len(roman_string) == 2:
                        val -= 2
                else:
                    if len(roman_string) == range(1, 15):
                        val -= 20
            elif roman_string[i] == key:
                val += roman_dict[key]
    return abs(val)
