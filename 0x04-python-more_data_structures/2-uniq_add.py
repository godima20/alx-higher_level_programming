#!/usr/bin/python3
def uniq_add(my_list=[]):
    ready = []
    sum = 0
    if my_list:
        for i in my_list:
            if i not in ready:
                sum += i
                ready.append(i)
    return sum
