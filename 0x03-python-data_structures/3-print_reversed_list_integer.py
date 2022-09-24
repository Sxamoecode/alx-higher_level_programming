#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for items in my_list[::-1]:
        print(f"{items}".format(items))
    return items
