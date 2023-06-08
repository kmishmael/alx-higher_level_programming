#!/usr/bin/python3
import sys
if __name__ == '__main__':
    ac = len(sys.argv) - 1
    sum = 0
    for i in range(0, ac):
        sum += int(sys.argv[i + 1])
    print('{0}'.format(sum))
