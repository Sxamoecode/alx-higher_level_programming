#!/usr/bin/python3
def no_c(my_string):
    for ch in my_string:
        strg = ""
        if ch != 'c' or ch != 'C':
            strg += ch
        print(str(strg))

no_c('Charcccjkl')