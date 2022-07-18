#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException as err:
        print('Exception: {}'.format(err))
        return None
