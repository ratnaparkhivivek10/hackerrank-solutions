#!/bin/python3

import sys


N = int(input().strip())

if N%2 == 0:
    if N in range(2, 5+1):
        print('Not Weird')
    if N in range(6, 20+1):
        print('Weird')
    if N > 20:
        print('Not Weird')
else:
     print('Weird')
