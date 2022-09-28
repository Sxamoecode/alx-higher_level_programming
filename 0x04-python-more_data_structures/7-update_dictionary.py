#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    add_dict = {key: value}
    a_dictionary.update(add_dict)
    return a_dictionary
