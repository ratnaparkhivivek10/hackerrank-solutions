#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
total = []
for i in range(len(arr)-2):
	for j in range(len(arr)-2):
		s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
		total.append(s)
        
        
print(max(total))