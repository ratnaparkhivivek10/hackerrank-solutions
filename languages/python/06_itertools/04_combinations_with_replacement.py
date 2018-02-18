from itertools import combinations_with_replacement as cwr
seq, r = input().split(' ')
[print(''.join(item)) for item in cwr(sorted(seq), int(r))]
