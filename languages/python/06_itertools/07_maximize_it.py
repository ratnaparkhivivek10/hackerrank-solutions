from itertools import product

def fmax(itr, m):
    s = 0
    for item in itr:
        s += item*item
    return s % m

K, M = list(map(int, input().split(' ')))
data = [list(map(int, i)) for i in [input().split(' ')[1:] for _ in range(K)]]
#print(data)
a = max([fmax(item, M) for item in product(*data)])
#constrainted_data = [list(filter(lambda x: x<=10**9, e)) for e in data]
#print(constrainted_data)
print(a)