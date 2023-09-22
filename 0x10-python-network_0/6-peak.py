#!/usr/bin/python3
"""Defines a peak-finding algorithm.
"""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers
    """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    j = int(length / 2)
    list_int = list_of_integers

    if j - 1 < 0 and j + 1 >= length:
        return list_int[j]
    elif j - 1 < 0:
        return list_int[j] if list_int[j] > list_int[j + 1] else list_int[j + 1]
    elif j + 1 >= length:
        return list_int[j] if list_int[j] > list_int[j - 1] else list_int[j - 1]

    if list_int[j - 1] < list_int[j] > list_int[j + 1]:
        return list_int[j]

    if list_int[j + 1] > list_int[j - 1]:
        return find_peak(list_int[j:])
    return find_peak(list_int[:j])
