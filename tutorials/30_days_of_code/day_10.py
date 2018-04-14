#!/bin/python3

import sys


n = int(input().strip())

print(len(max(bin(n)[2:].split('0'), key=len)))


# Other approach
data = '111111111111100011100101111001010101011111111'

temp = one = 0
for i in data:
    if i == '1':
        one += 1
    else:
        if one > temp:
            temp = one
            one = 0

if one > temp:
    temp = one

print(temp)
