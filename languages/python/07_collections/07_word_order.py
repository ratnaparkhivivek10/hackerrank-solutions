from collections import OrderedDict

n = int(input())
count = OrderedDict() 

for w in [input() for _ in range(n)]:
    count[w] = count.get(w, 0) + 1
    
print(len(count.keys()))
print(*count.values())