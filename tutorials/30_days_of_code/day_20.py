#!/bin/python3

import sys

n = int(input().strip())
data = list(map(int, input().strip().split(' ')))

swap = 0
for i in range(1, len(data)):
	for j in range(len(data) - i):
		if data[j] > data[j+1]:
			data[j+1], data[j] = data[j], data[j+1]
			swap += 1
	if swap == 0:
		break
        
print('Array is sorted in {0} swaps.'.format(swap))
print('First Element: {0}'.format(data[0]))
print('Last Element: {0}'.format(data[-1]))