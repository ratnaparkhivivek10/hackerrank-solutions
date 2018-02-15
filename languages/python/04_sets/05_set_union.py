nA = input()
A = set(map(int, input().split(' ')))

nB = input()
B = set(map(int, input().split(' ')))

print(len(A.union(B)))