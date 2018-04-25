#!/bin/python3

import sys
from functools import reduce

def lonely_integer(a):
    return reduce(lambda x, y: x^y, a)
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))