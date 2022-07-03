#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return len(sentence), None

    else:
        for i in range(len(sentence)):
            first_char = sentence[0]

    return len(sentence), first_char
