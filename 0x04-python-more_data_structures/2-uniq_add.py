#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for idx, el in enumerate(my_list):
        if el in my_list[:idx]:
            continue
        sum += el
    return sum
