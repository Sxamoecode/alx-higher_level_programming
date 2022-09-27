#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    rev = my_list
    for items in rev:
        print("{:d}".format(items))
    return
