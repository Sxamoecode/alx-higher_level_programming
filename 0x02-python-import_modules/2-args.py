#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print(f"0 arguments")
elif len(sys.argv) == 2:
    print(f"1 argument: {sys.argv[1]}")
else:
    print(f"{len(sys.argv) - 1:d} arguments:".format(len(sys.argv) - 1))
argv = len(sys.argv)
for i in range(argv):
    print(f"{i+1:d}: {sys.argv[i+1]:s}".format(i+1, sys.argv[i+1]))
