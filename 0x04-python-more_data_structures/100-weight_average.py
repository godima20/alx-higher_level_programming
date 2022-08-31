#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    res1, res2 = 0, 0
    for i, j in my_list:
        res1 += i * j
        res2 += j
        return (res1 / res2)

