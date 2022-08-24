#!/usr/bin/python3
def _uppercase(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)

def uppercase(string):
    string_new = ""
    for character in string:
        string_new += "%c" % _uppercase(character)
    print("{:s}".format(string_new))
