N = int(input())
stack = []
for _ in range(N):
    tc = list(map(int, input().split(' ')))
    if tc[0] == 1:
        stack.append(tc[-1])
    if tc[0] == 2:
        stack.pop()
    if tc[0] == 3:
        print(max(stack))
