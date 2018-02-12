import numpy as np
N, M = list(map(int, input().split(' ')))

data = []

for _ in range(N):
    data.append(input().split(' '))
    
data = np.array(data).astype(int)

print(data.mean(axis=1))
print(data.var(axis=0))
print(data.std())
