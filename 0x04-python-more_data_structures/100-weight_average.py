#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    if my_list:
        weight_sum = 0
        summ = 0
        for x in my_list:
            weight_sum = weight_sum + x[1]
        result = summ / weight_sum
    return result

