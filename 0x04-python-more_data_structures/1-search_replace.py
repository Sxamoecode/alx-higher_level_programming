#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(0, len(new_list)):
        if new_list[i] == search:
            new_list.insert(i, replace)
            new_list.pop(i+1)
            continue
    return new_list
