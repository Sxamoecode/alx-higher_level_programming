#!/usr/bin/python3
for num in range(0, 100):
    if len(num) == 1:
        print(f"0{num:d}".format(num), end='')
    print(f"{num:d}".format(num), end=', ')
