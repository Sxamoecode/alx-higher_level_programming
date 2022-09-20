#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            ch = str[i]
            ch = ord(ch)
            ch = ch - 32
            ch = chr(ch)
            str = str[:i] + ch + str[i+1:]
        return str
