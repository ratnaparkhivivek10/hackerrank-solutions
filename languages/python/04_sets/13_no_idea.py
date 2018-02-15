a, b = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
A = set(list(map(int, input().split(' '))))
B = set(list(map(int, input().split(' '))))

happiness = 0
for item in arr:
    if item in A:
        happiness+=1
    if item in B:
        happiness-=1
        
print(happiness)