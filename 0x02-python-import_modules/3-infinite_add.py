#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    total = 0
    for i in range(len(sys.argv)):
        if sys.argv[i] != sys.argv[0]:
            total = total + int(sys.argv[i])

    print(total)
