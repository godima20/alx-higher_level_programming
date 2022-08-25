#!/bin/usr/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{:d} arguments:".format(argc))
    elif num == 1:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    for i in range(0, len(argv)):
        if i > 0:
            print("{:d}: {:s}".format(index, argv[index]))
