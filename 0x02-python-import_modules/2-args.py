#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(f"0 arguments.")
    elif len(sys.argv) == 2:
        print(f"1 argument:")
    else:
        print(f"{len(sys.argv) - 1:d} arguments:".format(len(sys.argv) - 1))
    argv = len(sys.argv)
    for i in range(1, argv):
        print(f"{i:d}: {sys.argv[i]:s}".format(i, sys.argv[i]))
