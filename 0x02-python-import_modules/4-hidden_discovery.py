#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    names = [i for i in names if '__' not in i]
    for name in names:
        print(name)
