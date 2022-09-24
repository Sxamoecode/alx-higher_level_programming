#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list(my_list)
    for i in range(len(new_list)):
        if idx not in range(len(new_list)):
            return new_list
        elif idx < 0:
            return new_list
        else:
            new_list.insert(idx, element)
            new_list.pop(idx + 1)
            return new_list
