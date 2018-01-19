import numpy as np

n, m, p = list( map(int, input().split(' ')) )
a1 = np.array([input().split(' ') for _ in range(n)]).astype(int)
a2 = np.array([input().split(' ') for _ in range(m)]).astype(int)

print(np.concatenate((a1, a2), axis=0))
