#!/usr/bin/python3
"""
This is the 3-say_my_name module

The 3-say_my_name module supplies one function, say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the first and last names of a person
    Args:
        param first_name(str): person's first name
        param last_name(str): person's last name

    Returns:
        nothing
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if first_name == '':
        raise TypeError('first_name cannot be empty')
    if first_name == ' ':
        raise TypeError('first_name cannot be an empty string')

    '''
    if first_name.__contains__('[') or first_name.__contains__('(') \
            or first_name.__contains__('{') or \
            first_name.__contains__(']') or first_name.__contains__(')') \
            or first_name.__contains__('}'):
        raise TypeError('first_name can only be a sequence of '
                        'ASCII alphabet characters')


    if last_name.__contains__('[') or last_name.__contains__('(') \
            or last_name.__contains__('{') or \
            last_name.__contains__(']') or last_name.__contains__(')') \
            or last_name.__contains__('}'):
        raise TypeError('last_name can only be a sequence of '
                        'ASCII alphabet characters')
    '''
    if not first_name.isalpha():
        raise TypeError('first_name can only be a sequence of '
                        'ASCII alphabet characters')

    if not last_name.isalpha() and last_name != '':
        raise TypeError('last_name can only be a sequence of '
                        'ASCII alphabet characters')

    print('My name is {} {}'.format(first_name, last_name))
