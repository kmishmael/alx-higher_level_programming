#!/usr/bin/python3
import random
number = random.randint(-10, 10)
res = ''
if number == 0:
    res = '{} is zero'
elif number > 0:
    res = '{} is positive'
else:
    res = '{} is negative'
print(res.format(number))
