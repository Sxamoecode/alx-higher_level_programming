#!/usr/bin/python3
def print_last_digit(number):
    last_num = number % 10
    if number < 0:
        last_num = (((-1 * number)% 10) * -1)
    return last_num
