from itertools import permutations
seq, r = input().split(' ')
[print(''.join(item)) for item in sorted(list(permutations(seq, int(r))))]
    