N = int(input())
phoneBook = {}
for _ in range(N):
    name, number = input().split(' ')
    phoneBook[name] = number
    
for _ in range(N):
    name = input()
    if name in phoneBook:
        print('{0}={1}'.format(name, phoneBook.get(name)))
    else:
        print('Not found')
