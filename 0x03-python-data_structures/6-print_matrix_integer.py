#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for val in rows:
            if val == rows[-1]:
                print("{:d}".format(val), end='')
                print()
                continue
            print("{:d}".format(val), end=' ')
