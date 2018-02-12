import numpy as np
n, m = [int(item) for item in input().split(" ")]

l = []
for r in range(n):
    m = input()
    l.append([int(item) for item in m.split(" ")])
l = np.array(l)
print(np.transpose(l))
print(l.flatten())