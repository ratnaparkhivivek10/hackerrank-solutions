#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

neg, zero, pos = 0, 0, 0
for n in arr:
    if n < 0:
        neg += 1
    if n == 0:
        zero += 1
    if n > 0:
        pos += 1

print(round(pos/len(arr), 6))
print(round(neg/len(arr), 6))
print(round(zero/len(arr), 6))