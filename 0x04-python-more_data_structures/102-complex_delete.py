#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        to_delete = []
        for k, V in a_dictionary.items():
            if V == Value:
                to_delete.append(k)
        for k in to_delete:
            del a_dictionary[k]
        return a_dictionary
