#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    a = dir(hidden_4)
    for i in range(len(dir(hidden_4))):
        if not a[i].__contains__('__'):
            print(a[i])
