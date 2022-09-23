#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx not in range(len(my_list)):
            return my_list
        elif idx < 0:
            return my_list
        else:
            my_list.insert(idx, element)
            my_list.pop(idx + 1)
            return my_list
