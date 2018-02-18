import itertools
print(*itertools.product(list(map(int, input().split())), list(map(int, input().split()))))