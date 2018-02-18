from itertools import combinations
seq, r = input().split(' ')

lst = []
for r in range(1, int(r)+1):
    lst.extend(combinations(sorted(seq), r))#combinations are created after sorting seq
    
for item in [''.join(item) for item in lst]:
    print(item)