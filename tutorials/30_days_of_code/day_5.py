#!/bin/python3

import sys


n = int(input().strip())

for i in range(1, 10+1):
    print('{0} x {1} = {2}'.format(n, i, n*i))