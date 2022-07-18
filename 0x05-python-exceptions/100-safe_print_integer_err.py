#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write('Exception: {}'.format(err))
        return False

    return True