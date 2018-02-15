a = input()
seta = set(map(int, input().split(' ')))
b = input()
setb = set(map(int, input().split(' ')))


sym = set()
sym.update(seta.difference(setb), setb.difference(seta))
           
for item in sorted(sym):
    print(item)