#!/usr/bin/python3
for num in range(0, 100):
    num_str = str(num)
    if len(num_str) == 1:
        print(f"0{num:d}".format(num), end='')
        print(", ", end='')
        continue
    if num == 99:
        print(f"{num:d}".format(num), end='')
        continue
    print(f"{num:d}".format(num), end=', ')
