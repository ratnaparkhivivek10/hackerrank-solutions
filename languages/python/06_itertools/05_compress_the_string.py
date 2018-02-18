from itertools import groupby
seq = input()

for k, v in groupby(seq):
    lst = []
    lst.append(len(list(v)))
    lst.append(int(k))
    print(tuple(lst), end='')
    print(' ', end='')
    