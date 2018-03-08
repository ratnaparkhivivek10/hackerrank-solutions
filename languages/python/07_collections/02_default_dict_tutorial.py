from collections import defaultdict
outdict = defaultdict(list)

n, m = list(map(int, input().split(' ')))

A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

for i, item in enumerate(A, 1):
    outdict[item].append(i)

for item in B:
    if outdict[item]:
        print(*outdict[item])
    else:
        print(-1)