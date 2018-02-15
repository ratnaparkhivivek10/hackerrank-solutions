n = int(input())
s = set(map(int, input().split())) 
num_commands = int(input())

for _ in range(num_commands):
    command, *inpt = input().split(' ')
    if command == 'pop':
        s.pop()
    if command == 'remove':
        s.remove(int(*inpt))
    if command == 'discard':
        s.discard(int(*inpt))

print(sum(s))