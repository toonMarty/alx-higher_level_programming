#!/usr/bin/python3
"""
This is the 5-text_indentation module

The 5-text_indentation module supplies one function, text_indentation()
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of the
    characters: ., ?, and :
    Args:
        param text(str): The text to indent
    Returns:
        nothing
    """
    text_list = list(text)

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in range(len(text_list)):
        if i != len(text_list) - 1:
            if text_list[i] == '.' or text_list[i] == '?' or \
                    text_list[i] == ':':
                text_list[i + 1] = '\n\n'
    print(''.join(text_list), end='')
