#!/usr/bin/python3
def print_last_digit(number):
    last_num = number % 10
    if number < 0:
        last_num = -last_num
    return last_num
