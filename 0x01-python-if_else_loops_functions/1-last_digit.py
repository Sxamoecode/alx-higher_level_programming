#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
num_int = num_str[-1]
last_digit = int(num_int)                                                                             if number < 0:                                                                                            last_digit = -last_digit
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is \
greater than 5\n".format(number, last_digit), end='')
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and \
is 0\n".format(number, last_digit), end='')
else:
    print(f"Last digit of {number:d} is \
{last_digit:d} and is less \
than 6 and not 0\n".format(number, last_digit), end='')
