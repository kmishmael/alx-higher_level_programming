#!/usr/bin/python3
for i in range(100):
    print('{}'.format(i), end='')
    if i != 99:
        print(', ', end='')
    else:
        print('\n', end='')
