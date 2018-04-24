#!/bin/python3

import sys

n = int(input().strip())
data = list(map(int, input().strip().split(' ')))

swap = 0
for _ in range(len(data) - 1):
	for i in range(len(data) - 1):
		if data[i] > data[i+1]:
			data[i+1], data[i] = data[i], data[i+1]
			swap += 1
	if swap == 0:
		break
        
print('Array is sorted in {0} swaps.'.format(swap))
print('First Element: {0}'.format(data[0]))
print('Last Element: {0}'.format(data[-1]))
