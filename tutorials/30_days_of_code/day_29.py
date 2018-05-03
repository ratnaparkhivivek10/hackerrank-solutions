#!/bin/python3

import sys
from itertools import combinations, starmap


t = int(input().strip())
for _ in range(t):
    n, k = list(map(int, input().strip().split(' ')))
    data = filter(lambda x: x<k, list(starmap(lambda x, y: x & y, combinations(range(1, n+1), 2))))
    print(max(data))