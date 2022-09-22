#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    list_argv = []
    n = len(sys.argv)
    for values in range(1, len(sys.argv)):
        list_argv.append(sys.argv[values])
    Sum = 0
    for i in range(0, len(list_argv)):
        Sum = Sum + int(list_argv[i])
    print("Sum: ", Sum)
