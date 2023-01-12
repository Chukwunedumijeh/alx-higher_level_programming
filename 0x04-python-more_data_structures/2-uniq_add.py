#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for y in set(my_list):
        result += y
    return (result)
