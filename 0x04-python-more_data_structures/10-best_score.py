#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    if a_dictionary:
        val = -9999999
        for k, v in a_dictionary.items():
            if val < v:
                val = v
                key = k
    return key
