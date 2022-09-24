#!/usr/bin/python3
def no_c(my_string):
    rem_char = "c"
    rem_char2 = "C"

    new_str = ""

    for i in my_string:
        if i != rem_char and i != rem_char2:
            new_str += i

        res = new_str
    return str(res)
