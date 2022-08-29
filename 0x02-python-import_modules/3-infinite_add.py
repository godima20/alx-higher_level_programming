#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    answer = 0
    for i in range(0, len(argv)):
        if i > 0:
            answer += int(argv[i])
    print("{:d}".format(answer))
