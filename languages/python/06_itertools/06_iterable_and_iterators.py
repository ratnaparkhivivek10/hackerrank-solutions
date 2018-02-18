from itertools import combinations
n = int(input())
data = input().split()
k = int(input())

total = list(combinations(data, k))

a_list = list(filter(lambda c: 'a' in c, total))

print("{0:.3}".format(len(a_list)/len(total)))