#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
res = 'Last digit of {} is {} and '.format(number, last_digit)
if last_digit < 6:
    res = res + 'is less than 6'
    if last_digit == 0:
        res = res + ' and is 0'
    else:
        res = res + ' and not 0'
else:
    res = res + 'is greater than 5'
print(res)
