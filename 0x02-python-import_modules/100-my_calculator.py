#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    ac = len(sys.argv) - 1
    if ac != 3:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        res = add(a, b)
    elif operator == '-':
        res = sub(a, b)
    elif operator == '*':
        res = mul(a, b)
    elif operator == '/':
        res = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print('{0} {1} {2} = {3}'.format(a, operator, b, res))
