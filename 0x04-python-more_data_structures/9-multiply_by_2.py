#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys = sorted(new_dict.keys())
    for key in keys:
        val = new_dict[key] * 2
        new_dict[key] = val
    return new_dict
