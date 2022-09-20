#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z')+1):
    print(chr(alphabets).format(alphabets), end='')
