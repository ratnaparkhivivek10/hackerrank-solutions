from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    op, *e = input().rstrip().split(' ')
    if op == 'append':
        d.append(*e)
    if op == 'appendleft':
        d.appendleft(*e)
    if op == 'pop':
        d.pop()
    if op == 'popleft':
        d.popleft()

print(*d)   