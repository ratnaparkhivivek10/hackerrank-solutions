import numpy as np

n, m = list( map(int, input().split()) )
print(np.eye(n, m, k=0))
