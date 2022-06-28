#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

las = int(repr(number)[-1])


if las > 5:
    if number < 0:
        print(f'Last digit of {number} is {-las} and is less than 6 and not 0')
    else:
        print(f'Last digit of {number} is {las} and is greater than 5')

elif las < 6 and las != 0:
    if number < 0:
        print(f'Last digit of {number} is {-las} and is less than 6 and not 0')

    elif number > 0:
        print(f'Last digit of {number} is {las} and is less than 6 and not 0')

elif las == 0:
    print(f'Last digit of {number} is {las} and is 0')
else:
    TypeError
