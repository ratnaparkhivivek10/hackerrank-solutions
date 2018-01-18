import numpy as np

rows, columns = list(map(int, input().split(' ')))

print(np.array([list(map(int, input().split(' '))) for _ in range(rows)]).min(axis=1).max())
