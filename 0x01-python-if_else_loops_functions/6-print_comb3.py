#!/usr/bin/python3
for digit1 in range(0, 9):
    for digit2 in range(digit1+1, 10):
        if digit1 == 8 and digit2 == 9:
            print(f"{digit1:d}{digit2:d}".format(digit1, digit2), end='\n')
            continue
        print(f"{digit1:d}".format(digit1), end='')
        print(f"{digit2:d}".format(digit2), end=', ')
