#!/usr/bin/python3
import sys
if __name__ == '__main__':
    ac = len(sys.argv) - 1
    if ac == 0:
        print('{0} arguments.'.format(ac))
    elif ac == 1:
        print('{0} argument:'.format(ac))
    else:
        print('{0} arguments:'.format(ac))
    for i in range(0, ac):
        print('{0}: {1}'.format(i + 1, sys.argv[i + 1]))
