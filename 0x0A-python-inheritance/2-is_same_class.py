#!/usr/bin/python3
"""Check if for similar classes
"""


def is_same_class(obj, a_class):
    """
    function that returns true if classes are same
    :param obj: class to be compared
    :param a_class: class to compare with
    :return: True
    """
    if isinstance(obj, a_class):
        return True
    return False


a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
