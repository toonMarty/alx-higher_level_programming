#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        print('{} arguments.'.format(len(sys.argv) - 1))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))

    for i in range(len(sys.argv)):
        if sys.argv[i] != sys.argv[0]:
            print('{}: {}'.format(i, sys.argv[i]))
