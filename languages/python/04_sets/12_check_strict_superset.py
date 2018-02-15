A = set(map(int, input().split(' ')))
n = int(input())
issup = []

for _ in range(n):
    B = set(map(int, input().split(' ')))
    issup.append(A.issuperset(B))
    
print(all(issup))