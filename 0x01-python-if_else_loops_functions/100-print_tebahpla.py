#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    offset = 96 if i % 2 == 0 else 64
        print("{}".format(chr(offset+i)), end="")
