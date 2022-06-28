#!/usr/bin/python3
def uppercase(str2):
    str1 = ''
    for c in range(len(str2)):
        if 'a' <= str2[c] <= 'z':
            str1 = str1 + chr((ord(str2[c]) - 32))
        else:
            str1 = str1 + str2[c]

    print(str1)
