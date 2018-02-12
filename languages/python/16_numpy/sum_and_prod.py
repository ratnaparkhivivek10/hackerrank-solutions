import numpy as np

N, M = list(map(int, input().split(' ')))

A = []

for _ in range(N):
    A.append(list(map(int, input().split(' '))))
    
print(np.prod(np.array(A).sum(axis=0)))
